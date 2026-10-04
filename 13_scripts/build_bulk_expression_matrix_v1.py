import csv
from pathlib import Path
from collections import defaultdict

BASE = Path("/home/student/Desktop/CEIF")
ROOT = BASE / "16_multiomics_acquisition_v1"

MANIFEST = ROOT / "manifests/ceif_core_acquisition_manifest_v1.tsv"
AUDIT = ROOT / "logs/raw_md5_audit_v1.tsv"

OUTDIR = BASE / "04_bulk_transcriptomics"
OUTDIR.mkdir(parents=True, exist_ok=True)

META_OUT = OUTDIR / "bulk_sample_metadata_v1.tsv"
MATRIX_OUT = OUTDIR / "bulk_counts_unstranded_v1.tsv"

# ------------------------------------------------------------------
# Load manifest metadata by GDC file ID
# ------------------------------------------------------------------
manifest = {}

with open(MANIFEST, encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        if r["modality"] != "bulk_transcriptomics":
            continue

        manifest[r["gdc_file_id"]] = r

# ------------------------------------------------------------------
# Only process MD5-verified files
# ------------------------------------------------------------------
verified = []

with open(AUDIT, encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        if (
            r["status"] == "VERIFIED"
            and r["modality"] == "bulk_transcriptomics"
        ):
            fid = r["gdc_file_id"]

            if fid in manifest:
                verified.append((r, manifest[fid]))

# ------------------------------------------------------------------
# Read expression files
# ------------------------------------------------------------------
samples = {}
gene_values = defaultdict(dict)

for idx, (audit, meta) in enumerate(verified, 1):

    path = Path(audit["local_path"])

    sample_id = meta["sample_id"]
    case_id = meta["case_id"]

    if not path.is_file():
        continue

    # Avoid accidental duplicate sample columns.
    if sample_id in samples:
        continue

    samples[sample_id] = {
        "dataset_id": meta["dataset_id"],
        "cancer_type": meta["cancer_type"],
        "tcga_project": meta["tcga_project"],
        "case_id": case_id,
        "sample_id": sample_id,
        "sample_submitter_id": meta["sample_submitter_id"],
        "sample_type": meta["sample_type"],
        "gdc_file_id": meta["gdc_file_id"],
        "file_name": meta["file_name"],
    }

    with open(path, encoding="utf-8", errors="replace") as fh:

        header = None

        for line in fh:

            line = line.rstrip("\n")

            if not line:
                continue

            if line.startswith("#"):
                continue

            fields = line.split("\t")

            if header is None:
                header = fields

                required = {
                    "gene_id",
                    "gene_name",
                    "gene_type",
                    "unstranded",
                }

                missing = required - set(header)

                if missing:
                    raise RuntimeError(
                        f"Missing columns in {path.name}: {sorted(missing)}"
                    )

                gene_idx = header.index("gene_id")
                name_idx = header.index("gene_name")
                type_idx = header.index("gene_type")
                count_idx = header.index("unstranded")

                continue

            if len(fields) <= count_idx:
                continue

            gene_id = fields[gene_idx]

            if gene_id.startswith("N_"):
                continue

            try:
                count = float(fields[count_idx])
            except ValueError:
                continue

            gene_values[gene_id][sample_id] = count

    if idx % 100 == 0:
        print(
            f"PROCESSED {idx}/{len(verified)} | "
            f"samples={len(samples)} | genes={len(gene_values)}"
        )

# ------------------------------------------------------------------
# Write sample metadata
# ------------------------------------------------------------------
meta_fields = [
    "dataset_id",
    "cancer_type",
    "tcga_project",
    "case_id",
    "sample_id",
    "sample_submitter_id",
    "sample_type",
    "gdc_file_id",
    "file_name",
]

with open(META_OUT, "w", encoding="utf-8", newline="") as f:

    w = csv.DictWriter(
        f,
        fieldnames=meta_fields,
        delimiter="\t"
    )

    w.writeheader()

    for sid in sorted(samples):
        w.writerow(samples[sid])

# ------------------------------------------------------------------
# Write gene × sample matrix
# ------------------------------------------------------------------
sample_ids = sorted(samples)

with open(MATRIX_OUT, "w", encoding="utf-8", newline="") as f:

    w = csv.writer(f, delimiter="\t")

    w.writerow(
        ["gene_id"] + sample_ids
    )

    for gene_id in sorted(gene_values):

        vals = gene_values[gene_id]

        w.writerow(
            [gene_id] +
            [vals.get(sid, 0) for sid in sample_ids]
        )

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
print("=" * 100)
print("CEIF — BULK EXPRESSION MATRIX V1")
print("=" * 100)
print(f"VERIFIED INPUT FILES : {len(verified)}")
print(f"UNIQUE SAMPLES       : {len(samples)}")
print(f"UNIQUE GENES         : {len(gene_values)}")
print(f"MATRIX               : {MATRIX_OUT}")
print(f"SAMPLE METADATA      : {META_OUT}")
print("=" * 100)
print("RAW FILES            : UNMODIFIED")
print("GENOMICS             : SKIPPED / CONTROLLED ACCESS")
print("=" * 100)
