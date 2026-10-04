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
RAW = ROOT / "raw"
LOGDIR = ROOT / "logs"
LOGFILE = LOGDIR / "gdc_local_acquisition_v1.tsv"

GDC_URL = "https://api.gdc.cancer.gov/data/{}"

DEST = {
    "bulk_transcriptomics": "02_BULK_TRANSCRIPTOMICS",
    "genomics_mutation": "03_GENOMICS",
    "cnv": "04_CNV",
    "clinical_survival": "09_CLINICAL",
}

REQUIRED = [
    "dataset_id",
    "tcga_project",
    "modality",
    "gdc_file_id",
    "file_name",
    "md5sum",
    "case_id",
    "sample_id",
]

LOGDIR.mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True)

with open(MANIFEST, newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t"))

if not rows:
    raise RuntimeError("Manifest contains no data rows.")

missing = [x for x in REQUIRED if x not in rows[0]]
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
    "User-Agent": "CEIF-GDC-HPC-Local-Acquisition/1.0"
}

if token:
    headers["X-Auth-Token"] = token

session = requests.Session()
session.headers.update(headers)

if not LOGFILE.exists():
    with open(LOGFILE, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow([
            "gdc_file_id",
            "dataset_id",
            "tcga_project",
            "modality",
            "file_name",
            "local_path",
            "expected_md5",
            "computed_md5",
            "bytes",
            "status",
            "timestamp",
        ])

def log(row):
    with open(LOGFILE, "a", encoding="utf-8", newline="") as fh:
        csv.writer(fh, delimiter="\t").writerow(row)

def verified_already(path, expected_md5):
    if not path.exists() or not path.is_file():
        return False

    if not expected_md5:
        return False

    md5 = hashlib.md5()

    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            md5.update(chunk)

    return md5.hexdigest().lower() == expected_md5.lower()

print("=" * 100)
print("CEIF — GDC → HPC LOCAL ACQUISITION V1")
print("=" * 100)
print(f"MANIFEST : {MANIFEST}")
print(f"RECORDS  : {len(rows)}")
print(f"RAW ROOT : {RAW}")
print(f"LOG      : {LOGFILE}")
print("STORAGE  : LOCAL HPC ONLY")
print("=" * 100)

completed = 0
skipped = 0
failed = 0

for i, r in enumerate(rows, 1):

    fid = r["gdc_file_id"].strip()
    fname = r["file_name"].strip()
    modality = r["modality"].strip()
    dataset_id = r["dataset_id"].strip()
    expected = r["md5sum"].strip().lower()

    folder = DEST.get(modality)

    if not folder:
        print(f"[{i}/{len(rows)}] SKIP unknown modality: {modality}")
        failed += 1
        continue

    dest_dir = RAW / folder / dataset_id
    dest_dir.mkdir(parents=True, exist_ok=True)

    local_path = dest_dir / fname

    if verified_already(local_path, expected):
        print(
            f"[{i}/{len(rows)}] VERIFIED EXISTING | "
            f"{dataset_id} | {modality} | {fname}"
        )
        skipped += 1
        continue

    if local_path.exists():
        try:
            local_path.unlink()
        except Exception as e:
            print(f"    FAILED removing stale file: {e}")
            failed += 1
            continue

    url = GDC_URL.format(fid)

    print(
        f"[{i}/{len(rows)}] DOWNLOAD | "
        f"{dataset_id} | {modality} | {fname}"
    )

    start = time.time()
    md5 = hashlib.md5()
    total = 0

    tmp_path = local_path.with_name(local_path.name + ".partial")

    try:
        if tmp_path.exists():
            tmp_path.unlink()

        with session.get(
            url,
            stream=True,
            timeout=(30, 600)
        ) as resp:

            resp.raise_for_status()

            with open(tmp_path, "wb") as out:

                for chunk in resp.iter_content(
                    chunk_size=1024 * 1024
                ):
                    if not chunk:
                        continue

                    out.write(chunk)
                    md5.update(chunk)
                    total += len(chunk)

        computed = md5.hexdigest().lower()
        elapsed = max(time.time() - start, 0.001)

        if expected and computed != expected:
            try:
                tmp_path.unlink()
            except Exception:
                pass

            raise RuntimeError(
                f"MD5 mismatch expected={expected} computed={computed}"
            )

        tmp_path.rename(local_path)

        log([
            fid,
            dataset_id,
            r["tcga_project"],
            modality,
            fname,
            str(local_path),
            expected,
            computed,
            total,
            "VERIFIED",
            time.strftime("%Y-%m-%dT%H:%M:%S"),
        ])

        completed += 1

        print(
            f"    VERIFIED | "
            f"{total / 1024**2:.2f} MiB | "
            f"{elapsed:.1f}s | "
            f"MD5={computed}"
        )

    except Exception as e:

        try:
            if tmp_path.exists():
                tmp_path.unlink()
        except Exception:
            pass

        log([
            fid,
            dataset_id,
            r["tcga_project"],
            modality,
            fname,
            str(local_path),
            expected,
            "",
            total,
            f"FAILED: {e}",
            time.strftime("%Y-%m-%dT%H:%M:%S"),
        ])

        failed += 1

        print(f"    FAILED | {e}")

print()
print("=" * 100)
print("CEIF — ACQUISITION RUN COMPLETE")
print("=" * 100)
print(f"MANIFEST RECORDS : {len(rows)}")
print(f"VERIFIED         : {completed}")
print(f"ALREADY VERIFIED : {skipped}")
print(f"FAILED           : {failed}")
print(f"LOG              : {LOGFILE}")
print(f"RAW ROOT         : {RAW}")
print("=" * 100)
