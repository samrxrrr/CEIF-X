from pathlib import Path
import csv
import hashlib
import os
import sys
import time
import requests

BASE = Path.home() / "Desktop" / "CEIF"
ROOT = BASE / "16_multiomics_acquisition_v1"

MANIFEST = ROOT / "manifests" / "ceif_core_acquisition_manifest_v1.tsv"
RAW = ROOT / "raw" / "03_GENOMICS"
LOGDIR = ROOT / "logs"
LOGFILE = LOGDIR / "gdc_genomics_acquisition_v2.tsv"

GDC_URL = "https://api.gdc.cancer.gov/data/{}"

RAW.mkdir(parents=True, exist_ok=True)
LOGDIR.mkdir(parents=True, exist_ok=True)

with open(MANIFEST, newline="", encoding="utf-8") as fh:
    all_rows = list(csv.DictReader(fh, delimiter="\t"))

rows = [
    r for r in all_rows
    if r["modality"].strip() == "genomics_mutation"
]

if not rows:
    raise RuntimeError("No genomics_mutation records found in manifest.")

required = [
    "dataset_id",
    "tcga_project",
    "modality",
    "gdc_file_id",
    "file_name",
    "file_size",
    "md5sum",
    "case_id",
    "sample_id",
]

missing = [x for x in required if x not in rows[0]]
if missing:
    raise RuntimeError(f"Manifest missing columns: {missing}")

token = os.environ.get("GDC_TOKEN", "").strip()

if not token:
    for p in [
        Path.home() / ".gdc_token",
        Path.home() / ".gdc_token.txt",
        BASE / ".gdc_token",
    ]:
        if p.exists():
            token = p.read_text().strip()
            break

headers = {
    "User-Agent": "CEIF-GDC-HPC-Genomics-Acquisition/2.0"
}

if token:
    headers["X-Auth-Token"] = token

session = requests.Session()
session.headers.update(headers)

if not LOGFILE.exists():
    with open(LOGFILE, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh, delimiter="\t").writerow([
            "index",
            "gdc_file_id",
            "dataset_id",
            "tcga_project",
            "file_name",
            "expected_bytes",
            "actual_bytes",
            "expected_md5",
            "computed_md5",
            "status",
            "elapsed_seconds",
            "timestamp",
        ])

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().lower()

def log(row):
    with open(LOGFILE, "a", newline="", encoding="utf-8") as fh:
        csv.writer(fh, delimiter="\t").writerow(row)

def fmt_size(n):
    if n >= 1024**3:
        return f"{n/1024**3:.2f} GiB"
    if n >= 1024**2:
        return f"{n/1024**2:.2f} MiB"
    if n >= 1024:
        return f"{n/1024:.2f} KiB"
    return f"{n} B"

def fmt_speed(n, sec):
    if sec <= 0:
        return "N/A"
    return fmt_size(n / sec) + "/s"

print("=" * 100, flush=True)
print("CEIF — GDC → HPC GENOMICS ACQUISITION V2", flush=True)
print("=" * 100, flush=True)
print(f"MANIFEST        : {MANIFEST}", flush=True)
print(f"GENOMICS FILES  : {len(rows)}", flush=True)
print(f"DESTINATION     : {RAW}", flush=True)
print(f"LOG             : {LOGFILE}", flush=True)
print("MODE            : DOWNLOAD + MD5 VERIFY + SAFE RENAME", flush=True)
print("=" * 100, flush=True)

verified_existing = 0
downloaded = 0
failed = 0

for i, r in enumerate(rows, 1):

    fid = r["gdc_file_id"].strip()
    fname = r["file_name"].strip()
    dataset = r["dataset_id"].strip()
    project = r["tcga_project"].strip()
    expected_md5 = r["md5sum"].strip().lower()
    expected_bytes = int(float(r["file_size"])) if r["file_size"].strip() else 0

    dataset_dir = RAW / dataset
    dataset_dir.mkdir(parents=True, exist_ok=True)

    final_path = dataset_dir / fname
    partial_path = final_path.with_name(final_path.name + ".partial")

    print(
        f"[{i}/{len(rows)}] {dataset} | {project} | {fname}",
        flush=True
    )

    # Existing verified file
    if final_path.exists():
        try:
            actual = final_path.stat().st_size

            if expected_bytes and actual != expected_bytes:
                print(
                    f"    EXISTING SIZE MISMATCH "
                    f"expected={fmt_size(expected_bytes)} "
                    f"actual={fmt_size(actual)}",
                    flush=True
                )
            else:
                computed = md5_file(final_path)

                if computed == expected_md5:
                    print(
                        f"    ALREADY VERIFIED | "
                        f"{fmt_size(actual)} | MD5 OK",
                        flush=True
                    )

                    log([
                        i, fid, dataset, project, fname,
                        expected_bytes, actual,
                        expected_md5, computed,
                        "ALREADY_VERIFIED",
                        0,
                        time.strftime("%Y-%m-%dT%H:%M:%S"),
                    ])

                    verified_existing += 1
                    continue

                print("    EXISTING MD5 MISMATCH — redownloading", flush=True)

        except Exception as e:
            print(f"    EXISTING FILE CHECK FAILED: {e}", flush=True)

    if partial_path.exists():
        print("    Removing stale partial file", flush=True)
        try:
            partial_path.unlink()
        except Exception as e:
            print(f"    FAILED: {e}", flush=True)
            failed += 1
            continue

    url = GDC_URL.format(fid)

    start = time.time()
    total = 0
    md5 = hashlib.md5()

    try:
        with session.get(
            url,
            stream=True,
            timeout=(30, 1800)
        ) as resp:

            resp.raise_for_status()

            print(
                f"    HTTP {resp.status_code} | "
                f"starting transfer",
                flush=True
            )

            with open(partial_path, "wb") as out:

                last_report = time.time()

                for chunk in resp.iter_content(
                    chunk_size=8 * 1024 * 1024
                ):
                    if not chunk:
                        continue

                    out.write(chunk)
                    md5.update(chunk)
                    total += len(chunk)

                    now = time.time()

                    if now - last_report >= 5:
                        elapsed = now - start
                        print(
                            f"    PROGRESS {fmt_size(total)} | "
                            f"{fmt_speed(total, elapsed)} | "
                            f"{elapsed:.0f}s",
                            flush=True
                        )
                        last_report = now

        elapsed = max(time.time() - start, 0.001)
        computed = md5.hexdigest().lower()

        if expected_bytes and total != expected_bytes:
            raise RuntimeError(
                f"SIZE mismatch expected={expected_bytes} actual={total}"
            )

        if expected_md5 and computed != expected_md5:
            raise RuntimeError(
                f"MD5 mismatch expected={expected_md5} computed={computed}"
            )

        partial_path.rename(final_path)

        log([
            i, fid, dataset, project, fname,
            expected_bytes, total,
            expected_md5, computed,
            "VERIFIED",
            round(elapsed, 3),
            time.strftime("%Y-%m-%dT%H:%M:%S"),
        ])

        downloaded += 1

        print(
            f"    VERIFIED | {fmt_size(total)} | "
            f"{fmt_speed(total, elapsed)} | "
            f"MD5 OK",
            flush=True
        )

    except Exception as e:

        try:
            if partial_path.exists():
                partial_path.unlink()
        except Exception:
            pass

        elapsed = time.time() - start

        log([
            i, fid, dataset, project, fname,
            expected_bytes, total,
            expected_md5, "",
            f"FAILED: {e}",
            round(elapsed, 3),
            time.strftime("%Y-%m-%dT%H:%M:%S"),
        ])

        failed += 1

        print(
            f"    FAILED | {e}",
            flush=True
        )

print()
print("=" * 100, flush=True)
print("CEIF — GENOMICS ACQUISITION COMPLETE", flush=True)
print("=" * 100, flush=True)
print(f"MANIFEST RECORDS : {len(rows)}", flush=True)
print(f"DOWNLOADED       : {downloaded}", flush=True)
print(f"ALREADY VERIFIED : {verified_existing}", flush=True)
print(f"FAILED           : {failed}", flush=True)
print(f"DESTINATION      : {RAW}", flush=True)
print(f"LOG              : {LOGFILE}", flush=True)
print("=" * 100, flush=True)
