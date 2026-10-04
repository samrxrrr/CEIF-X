# CEIF-X MASTER EVIDENCE LEDGER

## Purpose
Single authoritative working record for:
- cohort definitions
- data provenance
- methods and parameters
- QC decisions
- quantitative results
- biological interpretation
- limitations
- reproducibility paths
- manuscript-ready Results/Discussion points
- figure/table planning
- final cross-layer evidence synthesis

## Core preservation rules
- RAW DATA: UNMODIFIED
- FROZEN OUTPUTS: PRESERVED
- Never overwrite a completed/frozen analysis.
- New analyses receive new versioned filenames.
- Never force mappings or biological annotations.
- Computational association ≠ causation.
- Pseudotime ≠ lineage proof.
- Communication inference ≠ physical interaction.
- Regulatory inference ≠ direct regulation.
- ML importance ≠ causal importance.
- Docking score ≠ target engagement.
- Candidate prioritization ≠ therapeutic efficacy.
- Clinical association ≠ clinical utility.

---

# A. AUTHORITATIVE COHORT

Original multimodal inventory: 8672 records

Three-modality all-case cohort: 2388  
Final locked paired cohort: 2349  
Complete molecular/clinical integration cohort: 2332

Dataset counts:
- SC001: 501
- SC002: 428
- SC003: 1038
- SC004: 365

Authoritative cohort:
`03_qc/ceif_complete_three_layer_integration_cohort_v1.tsv`

Sample manifest:
`03_qc/ceif_final_sample_level_manifest_v1.tsv`

---

# B. BULK TRANSCRIPTOMICS — COMPLETE

Initial matrix:
`04_bulk_transcriptomics/bulk_counts_unstranded_v1.tsv`

Structural QC:
`03_qc/bulk_matrix_structural_qc_v1.tsv`

Analysis cohort:
`04_bulk_transcriptomics/bulk_counts_analysis_cohort_v1.tsv`

Filtered matrix:
`04_bulk_transcriptomics/bulk_counts_filtered_v1.tsv`

Normalized matrix:
`04_bulk_transcriptomics/bulk_log2cpm_v1.tsv`

Key results:
- Initial: 60,660 genes × 2,653 samples
- Analysis cohort: 60,660 × 2,332
- Filter: CPM >=1 in >=10% samples
- Retained: 19,394 genes
- Removed: 41,266 genes
- Normalization: log2(CPM+1)
- QC: PASS

STATUS: COMPLETE

---

# C. CNV — COMPLETE

Matrix:
`04_cnv/cnv_copy_number_matrix_v1.tsv`

Log2 CNV:
`04_cnv/cnv_log2_copy_number_v1.tsv`

State matrix:
`04_cnv/cnv_state_matrix_v1.tsv`

Results:
- 60,623 genes × 3,510 samples
- 212,786,730 cells
- Missing: 12,639,740
- Missing fraction: 0.059401
- No imputation
- LOSS <1.5
- NEUTRAL 1.5–2.5
- GAIN >2.5

STATUS: COMPLETE

---

# D. BULK–CNV INTEGRATION — COMPLETE

Mapping:
`03_qc/ceif_final_bulk_cnv_sample_mapping_v1.tsv`

Alignment:
`03_qc/ceif_bulk_cnv_case_sample_alignment_v1.tsv`

Results:
- 2,332 mappings
- 1,205 exact one-to-one
- 1,127 exact multisample context
- 0 forced mappings
- 1,127 deterministic unique exact CNV selections

STATUS: COMPLETE

---

# E. BULK–CNV MOLECULAR SIGNALS — FROZEN

Association:
`04_multiomics/ceif_bulk_cnv_gene_association_v1.tsv`

Statistical signals:
`05_analysis/ceif_bulk_cnv_statistical_signals_v1.tsv`

Dataset consistency:
`05_analysis/ceif_bulk_cnv_dataset_stratified_consistency_v1.tsv`

Frozen signal set:
`05_analysis/ceif_reproducible_molecular_signal_set_v1.tsv`

Results:
- Shared genes: 19,376
- Valid: 19,367
- FDR <0.05: 16,184
- |r| >=0.30: 4,447
- Frozen reproducible signals: 1,356

Frozen selection rule:
FDR <0.05 AND |r| >=0.30 AND valid all four datasets AND positive all four datasets AND |r| >=0.30 all four datasets.

Clinical outcomes were not used for molecular signal selection.

STATUS: COMPLETE / FROZEN

---

# F. SURVIVAL — COMPLETE

Authoritative OS:
`03_qc/ceif_final_os_endpoint_v2.tsv`

Results:
- 2,332 cases
- 650 deaths
- 1,682 alive
- 1,851 valid OS times
- 481 missing
- 474 deaths without time
- 7 alive without censor time
- 37 zero-time
- 0 negative
- 0 duplicate

Conventional survival analyses use 1,851 valid time/event cases.

KM:
`05_analysis/ceif_overall_survival_km_v1.*`

Cox:
`05_analysis/ceif_univariate_cox_survival_v1.tsv`

Cox results:
- 1,356 valid signals
- 385 FDR <0.05
- 335 integrated survival candidates
- 289 lower-hazard
- 46 higher-hazard

Candidate rule:
BH-FDR <0.05 AND |logHR| >=0.30

Confirmed time-varying PH concerns:
- ENSG00000054611.14
- ENSG00000141002.20

STATUS: COMPLETE

---

# G. FUNCTIONAL ENRICHMENT / MODULES — COMPLETE

Enrichment:
`05_analysis/ceif_multilayer_functional_enrichment_v1.tsv`

Modules:
`05_analysis/ceif_cross_layer_functional_modules_v2.tsv`

Layer comparison:
`05_analysis/ceif_functional_layer_comparison_v2.tsv`

Results:
- L1: 1,356 genes
- L2: 335 genes
- L3: 1,021 genes
- Background: 19,394
- Enrichment rows: 7,895
- FDR <0.05: 432
- Unique database×term pairs: 257
- Distinct module IDs: 151

L2 vs L3:
`05_analysis/ceif_L2_vs_L3_gene_comparison_v2.tsv`

- L2 genes: 100
- L3 genes: 574
- Shared: 0

Interpretation:
Zero overlap describes the selected significant enrichment-term gene lists. It does not prove complete biological independence.

STATUS: COMPLETE

---

# H. SINGLE-CELL DATASETS

No new scRNA downloads unless explicitly authorized.

Datasets:
- SC001 — E-MTAB-6653 — Lung
- SC002 — E-MTAB-8410 — Colorectal
- SC003 — E-GEOD-75688 — Breast
- SC004 — E-MTAB-8559 — Ovarian

Input cells:
- SC001: 32,341
- SC002: 52,587
- SC003: 520
- SC004: 19,880

Total: 105,328

SC003:
- Design assays: 549
- Expression cells: 520
- 29 design-only assays quarantined
- No forced alignment

STATUS: ACQUISITION/QC COMPLETE

---

# I. SINGLE-CELL QC — COMPLETE

Final retained cells: 104,683

| Dataset | Input | Retained | Excluded |
|---|---:|---:|---:|
| SC001 | 32,341 | 32,135 | 206 |
| SC002 | 52,587 | 52,165 | 422 |
| SC003 | 520 | 515 | 5 |
| SC004 | 19,880 | 19,868 | 12 |

Candidate rules:
- SC001: >=300 genes, mito <=0.10
- SC002: >=300 genes, mito <=0.10
- SC003: >=3000 genes, mito <=0.10
- SC004: >=500 genes, mito <=0.10

Retained manifest:
`03_qc/ceif_scRNA_retained_cell_manifest_v1.tsv`

Excluded manifest:
`03_qc/ceif_scRNA_excluded_cell_manifest_v1.tsv`

STATUS: COMPLETE

---

# J. SINGLE-CELL GENE HARMONIZATION — COMPLETE

Common gene universe:
`03_qc/ceif_scRNA_common_gene_universe_v1.tsv`

Common genes: 20,611 Ensembl IDs

Harmonized matrices:
`03_single_cell_transcriptomics/harmonized_expression_v1/`

| Dataset | Genes | Retained cells | NNZ |
|---|---:|---:|---:|
| SC001 | 20,611 | 32,135 | 55,868,418 |
| SC002 | 20,611 | 52,165 | 101,944,715 |
| SC003 | 20,611 | 515 | 5,030,835 |
| SC004 | 20,611 | 19,868 | 56,211,143 |

Integrity:
`03_qc/ceif_scRNA_harmonized_matrix_integrity_v1.tsv`

All matrices:
- correct dimensions
- correct gene/cell indices
- finite
- non-negative
- float32

STATUS: COMPLETE

---

# K. SINGLE-CELL PRE-INTEGRATION ASSESSMENT — COMPLETE

Output:
`03_analysis/ceif_scRNA_preintegration_pca_v1.tsv`

Input:
- 104,683 cells
- 20,611 genes
- 30 components

PC1 variance fraction: 82.4435%

Pairwise centroid distances in PC1–10:
- SC001–SC002: 9.1111
- SC001–SC003: 26.2619
- SC001–SC004: 25.6890
- SC002–SC003: 23.4997
- SC002–SC004: 22.4839
- SC003–SC004: 23.1412

Interpretation:
Strong dataset separation exists. This cannot be labelled purely technical because datasets represent different cancers/tissues. Integration must reduce unwanted dataset-associated structure without erasing biological heterogeneity.

Batch assessment:
`03_qc/ceif_scRNA_preintegration_batch_effect_v1.tsv`

STATUS: COMPLETE

---

# L. SINGLE-CELL INTEGRATION — CURRENT

Dedicated environment:
- ceif-scrna
- Python 3.12
- scanpy 1.12.4
- anndata 0.13.4
- numpy 2.5.3
- scipy 1.18.1

Current stage:
PRE-INTEGRATION COMPLETE

Next:
1. Build AnnData objects.
2. Preserve dataset and sample metadata.
3. Perform dataset-aware integration.
4. Quantify pre/post mixing.
5. Verify biological structure is retained.
6. Freeze integrated representation.
7. Proceed to clustering/annotation.

Do not overwrite pre-integration matrices.

---

# M. 16-LAYER PROJECT STATUS

| # | Layer | Status |
|---|---|---|
| 1 | Functional-module interpretation | READY |
| 2 | L2 vs L3 gene comparison | COMPLETE |
| 3 | Single-cell integration | RUNNING — integration next |
| 4 | Malignant-cell identification | PENDING |
| 5 | Tumor-state characterization | PENDING |
| 6 | Annotation uncertainty | PENDING |
| 7 | Cell-cell communication | **LIANA READY — 21 sender-side events; 20,611-gene mapping validated; quantitative LR inference pending** |
| 8 | Regulatory/network analysis | PENDING |
| 9 | Cross-cancer conservation | PENDING |
| 10 | ML/predictive layer | PENDING |
| 11 | Independent validation | PENDING |
| 12 | Evidence integration/candidate prioritization | PENDING |
| 13 | LUAD plasticity | PENDING |
| 14 | Structural/docking hypothesis | PENDING evidence gate |
| 15 | Final cross-layer synthesis | PENDING |
| 16 | Figures/tables/manuscript | PENDING |

---

# N. MANUSCRIPT EVIDENCE RECORD — TO BE FILLED FOR EVERY ANALYSIS

## Question
## Cohort/Input
## Methods
## Software + versions
## Parameters
## QC
## Output files
## Quantitative results
## Biological interpretation
## Limitations
## Manuscript Results wording
## Manuscript Discussion wording
## Figure candidate
## Table candidate
## Reproducibility notes

---

# O. UPDATE LOG

| Version | Date | Update |
|---|---|---|
| v1 | 2026-10-04 | Master evidence ledger initialized. |

RAW DATA: UNMODIFIED  
FROZEN OUTPUTS: PRESERVED

## 2026-10-04 — Layer 3 AnnData construction

Output directory:
`03_single_cell_transcriptomics/anndata_v1/`

Validated AnnData objects:
- SC001 E-MTAB-6653: 32,135 cells × 20,611 genes
- SC002 E-MTAB-8410: 52,165 cells × 20,611 genes
- SC003 E-GEOD-75688: 515 cells × 20,611 genes
- SC004 E-MTAB-8559: 19,868 cells × 20,611 genes

Files:
- `SC001_E-MTAB-6653_anndata.h5ad`
- `SC002_E-MTAB-8410_anndata.h5ad`
- `SC003_E-GEOD-75688_anndata.h5ad`
- `SC004_E-MTAB-8559_anndata.h5ad`

Metadata preserved:
- dataset_id
- accession
- cell identifiers
- harmonized gene identifiers

No source expression matrices were modified.

Layer 3 substage:
ANNData construction = COMPLETE

Next:
Dataset-aware normalization and log transformation, followed by explicit pre/post-integration QC.

## 2026-10-04 — Layer 3 normalization/log transformation

Output directory:
`03_single_cell_transcriptomics/normalized_v1/`

Normalized objects:
- SC001 E-MTAB-6653: 32,135 × 20,611
- SC002 E-MTAB-8410: 52,165 × 20,611
- SC003 E-GEOD-75688: 515 × 20,611
- SC004 E-MTAB-8559: 19,868 × 20,611

Method:
- Library-size normalization to target sum 10,000
- log1p transformation
- Separate output objects created
- Harmonized source matrices preserved
- Raw/source data unmodified

Files:
- `SC001_E-MTAB-6653_normalized_log1p.h5ad`
- `SC002_E-MTAB-8410_normalized_log1p.h5ad`
- `SC003_E-GEOD-75688_normalized_log1p.h5ad`
- `SC004_E-MTAB-8559_normalized_log1p.h5ad`

Layer 3 substage:
NORMALIZATION + LOG1P = COMPLETE

Next:
Integration using dataset-aware correction, with pre/post integration diagnostics.

## 2026-10-04 — Layer 3 Harmony integration COMPLETE

Integration environment:
- Environment: `ceif-scrna`
- Scanpy: 1.12.4
- AnnData: 0.13.4
- harmonypy: 2.0.2
- Python: 3.12

Input:
- 104,683 retained cells
- 20,611 common genes
- Four datasets: SC001, SC002, SC003, SC004

Integration workflow:
1. Dataset-aware HVG selection
2. 3,000 highly variable genes
3. Scaling with zero-centering and max_value=10
4. 30-component PCA
5. Harmony correction using `dataset_id`
6. Harmony converged after 5 iterations
7. Random seed: 42

Harmony parameters recorded:
- max_iter_harmony: 10
- max_iter_kmeans: 4
- epsilon_cluster: 0.001
- epsilon_harmony: 0.01
- nclust: 100
- theta: 2
- block_size: 0.05
- dynamic lambda
- batch variable: dataset_id

Validated output:
`03_single_cell_transcriptomics/harmony_v1/CEIF_X_harmony_representation_v1.h5ad`

Artifact validation:
- File size: 25.73 MB
- AnnData shape: 104,683 × 1
- PCA representation: 104,683 × 30
- Harmony representation: 104,683 × 30
- Dataset metadata present: YES
- PCA values finite: YES
- Harmony values finite: YES

The compact artifact intentionally stores the integration representations and metadata rather than duplicating the full expression matrix. Normalized expression objects remain separately preserved.

Important technical note:
An earlier full-expression Harmony `.h5ad` write was interrupted and produced a corrupted generated artifact. That artifact was deleted. No raw, harmonized, or normalized source data were modified. The validated representation-only artifact above is authoritative.

Layer 3 substage:
HARMONY INTEGRATION = COMPLETE

Next:
Quantitative post-integration QC and comparison with the pre-integration dataset structure before clustering.

## 2026-10-04 — Layer 3 post-Harmony batch-effect QC COMPLETE

QC output:
`03_qc/ceif_scRNA_pre_post_harmony_batch_qc_v1.tsv`

PC1–10 centroid-distance assessment:

| Pair | Pre-Harmony | Post-Harmony | Post/Pre |
|---|---:|---:|---:|
| SC001–SC002 | 9.3951 | 7.4866 | 0.7969 |
| SC001–SC003 | 16.8414 | 10.4587 | 0.6210 |
| SC001–SC004 | 20.7817 | 17.6095 | 0.8474 |
| SC002–SC003 | 12.8307 | 7.3088 | 0.5696 |
| SC002–SC004 | 17.7408 | 14.5126 | 0.8180 |
| SC003–SC004 | 17.4518 | 14.1724 | 0.8121 |

All six pairwise dataset centroid distances decreased after Harmony.

Largest reduction:
SC002–SC003 = 43.0%

Smallest reduction:
SC001–SC004 = 15.3%

Within-dataset dispersion remained broadly comparable between pre- and post-Harmony representations.

Interpretation:
Harmony reduced dataset-associated expression-space separation without an obvious collapse of within-dataset structure by this diagnostic. Dataset identity remains biologically meaningful because the four datasets represent different cancer/tissue contexts; therefore Harmony is treated as an integration representation, not proof that all biological differences are technical.

Decision:
Harmony representation accepted as the working integrated embedding for downstream exploratory clustering and annotation.

Layer 3 substage:
POST-INTEGRATION BATCH QC = COMPLETE

Next:
Construct Harmony-based neighborhood graph and evaluate clustering structure before biological annotation.

### Layer 3 — Clustering structure QC
- Neighbor graph computed from the validated Harmony representation (`X_pca_harmony`), n_neighbors=15, n_pcs=30, Euclidean metric.
- Leiden resolutions evaluated: 0.2, 0.4, 0.6, 0.8, 1.0.
- Cluster counts: 19, 25, 31, 34, 39 respectively.
- Minimum cluster sizes: 445, 445, 120, 129, 119 respectively.
- Working annotation resolution selected: Leiden 0.8 (34 clusters).
- Rationale: provides finer structure while avoiding clusters below 100 cells; alternative resolutions retained for sensitivity analysis.
- QC artifact: `03_qc/ceif_scRNA_clustering_structure_qc_v1.tsv`.
- Clustering artifact: `03_single_cell_transcriptomics/clustering_v1/CEIF_X_harmony_neighbors_clustering_v1.h5ad`.
- Status: PASS; proceed to cluster-level biological annotation/QC.

### Layer 3 — Cluster × dataset composition audit
- Leiden 0.8 clustering contains 34 clusters across 104,683 retained cells.
- Cluster × dataset composition audit completed:
  `03_qc/ceif_scRNA_cluster_dataset_composition_v1.tsv`
- Strong dataset-specific composition is present in several clusters.
- SC001/SC002 dominate many immune and stromal clusters.
- SC003 is strongly concentrated in cluster 8 (52.6% SC003; 47.4% SC001), consistent with the limited SC003 retained-cell cohort.
- SC004 dominates clusters 26 (92.6%), 27 (89.5%), 29 (95.3%), 30 (99.9%), 32 (99.9%) and 33 (99.8%).
- Several clusters are predominantly SC001 or SC002, including clusters 1, 5, 6, 12, 13, 17, 19, 21, 22, 23, 24, 25 and 31.
- Interpretation: dataset-specific composition is substantial and must be retained as a biological/cohort-context caveat during annotation. Cluster identity will not be interpreted as universally conserved solely because Harmony reduced global embedding separation.
- No cells or source matrices were modified.
- Next: construct provisional broad-lineage annotations integrating marker evidence with dataset composition, explicitly retaining ambiguous/dataset-restricted clusters.


### Layer 3 — Provisional broad-lineage annotation
- Provisional annotation table:
  `03_single_cell_transcriptomics/cluster_markers_v1/CEIF_X_leiden0_8_provisional_lineage_annotation_v1.tsv`
- All 34 Leiden-0.8 clusters assigned a provisional lineage/state label with explicit confidence.
- High-confidence populations include T/NK, myeloid/macrophage, ciliated epithelial, endothelial, fibroblast, plasma, B-cell, mast, smooth-muscle/pericyte, epithelial and proliferating populations.
- Low-confidence populations retained as unresolved/ambiguous rather than forced: clusters 7, 12, 15, 16, 26, 27, 30, 31, 33.
- Proliferation is treated as a cellular state rather than an independent lineage.
- Dataset-restricted populations remain explicitly flagged; cluster identity is not assumed to be universally conserved across cancers.
- No malignant designation has been made at this stage.
- Next: formal annotation-uncertainty scoring and marker-panel validation before Layer 4 malignant-cell identification.


### Layer 3 — Annotation uncertainty audit
- Completed:
  `03_qc/ceif_scRNA_annotation_uncertainty_v1.tsv`
- 34 Leiden-0.8 clusters audited using provisional annotation confidence, dataset dominance, dataset entropy, and marker-resolution metrics.
- Annotation uncertainty: 13 LOW, 12 MODERATE, 9 HIGH.
- HIGH-uncertainty clusters: 7, 12, 15, 16, 26, 27, 30, 31, 33.
- MODERATE-uncertainty clusters: 1, 6, 11, 17, 19, 23, 24, 25, 28, 29, 32.
- LOW-uncertainty clusters: 0, 2, 3, 4, 5, 8, 9, 10, 13, 14, 18, 20, 21, 22.
- Dataset restriction is particularly strong for several uncertain clusters, including SC004-dominant clusters 26, 27, 30, 32 and 33 and SC001/SC002-restricted clusters.
- Marker evidence remained technically complete for all clusters: 100 marker rows per cluster and 100/100 Ensembl IDs resolved; gene-symbol resolution varied but unresolved symbols were retained rather than discarded.
- Uncertainty labels are analytical safeguards and do not constitute malignant/non-malignant classification.
- Next: resolve lineage ambiguity using targeted marker panels and compartment-specific evidence before malignant-cell identification.


### Layer 3 — Targeted lineage validation
- Completed:
  `03_single_cell_transcriptomics/cluster_markers_v1/CEIF_X_leiden0_8_targeted_lineage_validation_v1.tsv`
- Targeted marker panels evaluated T/NK, B-cell, plasma, myeloid, mast, endothelial, fibroblast, pericyte/smooth-muscle, epithelial, ciliated, alveolar, neural-like, interferon and proliferation programs.
- Cluster 6 is supported as myeloid/macrophage.
- Cluster 7 remains mixed/low-confidence myeloid/APC.
- Cluster 11 is strongly supported as alveolar epithelial.
- Cluster 12 is strongly supported as T/NK despite minor epithelial/alveolar signal.
- Cluster 15 remains low-information/uncertain despite epithelial markers.
- Cluster 16 remains ambiguous secretory epithelial/plasma-like.
- Cluster 19 is strongly supported as fibroblast.
- Clusters 23–25 are supported as epithelial.
- Clusters 26–27 retain epithelial/stress labels with low confidence.
- Cluster 28 is strongly supported as plasma.
- Cluster 29 is strongly supported as cycling/proliferating.
- Cluster 30 remains unresolved stromal/mesenchymal.
- Cluster 31 is strongly supported as neural-like.
- Cluster 32 is epithelial with moderate confidence.
- Cluster 33 remains interferon/stress epithelial-like with low confidence.
- Lineage validation does not establish malignancy. Epithelial identity, proliferation, or stress alone will not be used as evidence of malignancy.
- Next: malignant-cell candidate screening with explicit separation of candidate status from confirmed malignancy.


### Layer 4 — Malignant-cell candidate screening
- Completed:
  `03_single_cell_transcriptomics/cluster_markers_v1/CEIF_X_leiden0_8_malignant_candidate_screen_v1.tsv`
- Conservative screening identified clusters 23, 24 and 25 as malignant-cell candidates.
- Cluster 23: 6 epithelial markers and 5 malignant-associated markers, including CEACAM5, ERBB3, ITGA6 and SOX9.
- Cluster 24: 6 epithelial markers and 3 malignant-associated markers, including CEACAM5 and ERBB3.
- Cluster 25: 6 epithelial markers and 3 malignant-associated markers, including CEACAM5 and ERBB3.
- Other epithelial clusters were not promoted to malignant candidates because epithelial identity alone, proliferation alone, or stress/interferon programs alone were insufficient.
- Cluster 29 is strongly proliferative but did not satisfy the epithelial-plus-malignant-marker criterion and therefore remains a cycling population rather than a malignant call.
- Malignancy remains UNCONFIRMED. Marker-based candidate status will require independent genomic/CNV and tumor-context evidence.
- Next: CNV-supported malignant-cell validation for candidate clusters 23–25.


### Layer 4 — CNV validation gate
- CNV linkage audit completed:
  `03_qc/ceif_scRNA_malignant_candidate_cnv_validation_v1.tsv`
- Existing CNV matrix contains 3,510 sample columns.
- Malignant candidate clusters 23–25 contain 7,928 cells and are overwhelmingly SC002-derived.
- The authoritative retained scRNA cell manifest contains dataset/accession/cell-level metadata but no authoritative `case_id` or `sample_id`.
- Therefore a defensible cell→case→CNV mapping cannot be established from the available frozen metadata.
- CNV validation was BLOCKED rather than inferred or forced.
- No cell-level CNV evidence is assigned to clusters 23–25.
- Clusters 23–25 remain MALIGNANT CANDIDATES based on epithelial + malignant-associated marker evidence only.
- Confirmed malignancy is NOT established.
- The unavailable CNV linkage is recorded as an explicit evidence limitation.
- Further attempts to force cell-to-CNV matching are prohibited unless an already-existing authoritative linkage artifact is identified.
- Next: malignant-candidate evidence synthesis using available scRNA evidence and explicit uncertainty, followed by tumor-state characterization.


### Layer 4 — Malignant-candidate evidence synthesis
- Completed:
  `05_analysis/ceif_malignant_candidate_evidence_v1.tsv`
- Three candidate clusters retained: 23, 24 and 25.
- Cluster 23 is the STRONGEST_CANDIDATE: 3,179 cells, 6 epithelial-marker hits, 5 malignant-associated-marker hits and 4 targeted epithelial-marker hits.
- Cluster 24 is a CANDIDATE: 2,159 cells, 6 epithelial-marker hits, 3 malignant-associated-marker hits and 4 targeted epithelial-marker hits.
- Cluster 25 is a CANDIDATE: 2,590 cells, 6 epithelial-marker hits, 3 malignant-associated-marker hits and 4 targeted epithelial-marker hits.
- All three candidates are overwhelmingly SC002-derived (>97%), creating a strong dataset-restriction caveat.
- All three remain CANDIDATE_ONLY; none is classified as confirmed malignant.
- Cell-level CNV validation is NOT_AVAILABLE because the authoritative scRNA cell manifest lacks case/sample linkage.
- No proliferation evidence was used to artificially strengthen these candidates.
- Next: characterize tumor-cell states within the candidate epithelial populations, while preserving malignant status as unresolved.


### Layer 5 — Tumor-state characterization: initial state screen
- Completed:
  `05_analysis/ceif_epithelial_candidate_tumor_state_screen_v1.tsv`
- Candidate clusters 23–25 show a consistent epithelial-differentiation program with ELF3/EPCAM/KRT8/KRT18/KRT19.
- Clusters 23 and 25 additionally show secretory markers AGR2/KRT19.
- Cluster 24 shows interferon-associated markers IFI27/IFI6 and secretory markers KRT19/TACSTD2.
- ERBB3 is detected in all three candidate clusters; this is an expression association and not evidence of pathway activation or therapeutic response.
- No proliferation/cell-cycle program was detected in clusters 23–25 in this marker-panel screen.
- Cluster 29 is strongly proliferative and represents a distinct cycling population, but it was not classified as malignant from proliferation alone.
- Cluster 26 shows limited epithelial/secretory/EGFR and EMT-associated evidence.
- Cluster 27 shows epithelial plus stress/hypoxia-associated evidence.
- Cluster 32 shows epithelial differentiation with limited proliferation evidence.
- Cluster 33 shows interferon/stress-associated evidence with limited EMT-associated signal.
- Tumor-state labels remain descriptive; no causal or malignant-state inference is made from marker presence alone.
- Next: formal state scoring/comparison across epithelial populations, with candidate clusters 23–25 compared against other epithelial/stress/cycling populations.


### Layer 5 — Formal epithelial tumor-state comparison
- Completed:
  `05_analysis/ceif_epithelial_cluster_state_scores_v1.tsv`
- Clusters 23, 24 and 25 are dominated by epithelial-differentiation markers.
- Cluster 24 additionally shows an interferon-associated program.
- Clusters 23 and 25 show secretory-associated markers.
- ERBB3 is detected in clusters 23, 24 and 25; this is descriptive expression evidence only.
- Cluster 29 is strongly proliferation/cell-cycle dominant and is distinct from candidate clusters 23–25.
- Cluster 27 is stress/hypoxia dominant.
- Cluster 33 is interferon dominant with limited stress/EMT-associated evidence.
- Clusters 11 and 17 show strong epithelial differentiation with additional secretory/interferon-associated programs.
- Clusters 15, 16, 26 and 32 show weaker or mixed epithelial-state evidence.
- No causal state assignment or malignant-state inference is made from marker counts.
- Next: characterize candidate tumor-state heterogeneity using the validated epithelial populations and preserve state labels as descriptive programs.


### Layer 5 — Candidate tumor-state heterogeneity comparison
- Completed:
  `05_analysis/ceif_malignant_candidate_tumor_state_comparison_v1.tsv`
  `05_analysis/ceif_malignant_candidate_tumor_state_group_summary_v1.tsv`
- Candidate clusters 23–25 consistently show epithelial-differentiation evidence (mean 5 marker hits/cluster) and secretory-associated evidence (mean 2 hits/cluster).
- Candidate clusters show limited interferon signal overall (mean 0.67 hits) and no EMT marker hits in this marker-derived comparison.
- Candidate clusters show no proliferation or cell-cycle marker hits in this screen.
- Comparator epithelial populations are more heterogeneous, including distinct proliferative/cell-cycle (cluster 29), stress/hypoxia (cluster 27), and interferon-dominant (cluster 33) states.
- Candidate clusters therefore represent a relatively coherent epithelial/secretory transcriptional state within the current clustering structure.
- This comparison remains descriptive and marker-derived; it does not establish malignancy, clonality, pathway activation, or therapeutic response.
- Layer 5 tumor-state characterization remains active for deeper state interpretation.


### Layer 5 — Tumor-state resolution
- Completed:
  `05_analysis/ceif_epithelial_tumor_state_resolution_v1.tsv`
- Candidate clusters 23, 24 and 25 independently resolve to EPITHELIAL_DIFFERENTIATION with LOW state ambiguity.
- Cluster 11 resolves to mixed EPITHELIAL_DIFFERENTIATION/SECRETORY state with MODERATE ambiguity.
- Cluster 15 resolves to EPITHELIAL_DIFFERENTIATION with LOW ambiguity.
- Cluster 16 resolves to SECRETORY with LOW ambiguity.
- Cluster 17 resolves to EPITHELIAL_DIFFERENTIATION with LOW ambiguity.
- Cluster 26 remains mixed EPITHELIAL_DIFFERENTIATION/SECRETORY/EMT/EGFR_ERBB with MODERATE ambiguity.
- Cluster 27 resolves to STRESS_HYPOXIA.
- Cluster 29 resolves to PROLIFERATION and is a distinct cycling epithelial population.
- Cluster 32 resolves to EPITHELIAL_DIFFERENTIATION.
- Cluster 33 resolves to INTERFERON.
- These are descriptive transcriptional states, not proof of malignancy, pathway activation, lineage origin, clonality, or causality.


### Layer 3/6 — Final working cell-type map
- Completed:
  `03_single_cell_transcriptomics/cluster_markers_v1/CEIF_X_leiden0_8_final_working_celltype_map_v1.tsv`
- All 34 Leiden-0.8 clusters now have a working cell-type/state label, explicit annotation confidence, annotation uncertainty, dataset restriction and malignant-status field.
- Clusters 23–25 retain `MALIGNANT_CANDIDATE_ONLY`; malignancy remains unconfirmed.
- High-uncertainty populations remain explicitly unresolved rather than forced: clusters 7, 12, 15, 16, 26, 27, 30, 31 and 33.
- Dataset restriction is preserved in the map and must be considered in downstream communication and cross-cancer interpretation.
- This map is the working annotation layer for downstream cell-cell communication analysis.
### Layer 7 validated evidence — 2026-10-04
- Input marker audit: `05_analysis/ceif_cell_communication_input_evidence_v1.tsv`
- Sender-side candidate table: `05_analysis/ceif_cell_communication_candidate_interactions_v1.tsv`
- 21 ligand events detected across annotated clusters.
- No sender→receiver communication interaction is considered established from marker evidence alone.
- Receiver assignment and quantitative communication inference remain pending.

### Layer 7 LIANA preparation — 2026-10-04
- LIANA version: 1.10.0.
- Built-in consensus LR resource: 4,620 unique ligand–receptor pairs.
- Existing 20,611-gene CEIF scRNA universe mapped through the authoritative CNV feature reference.
- No new biological dataset downloaded.
- Quantitative LIANA inference remains pending validation of LR-gene coverage and AnnData reconstruction.

### Layer 7 validated mapping/QC — 2026-10-04
- SC001 cell-level alignment: PASS; 32,135 normalized cells exactly matched 32,135 clustering rows.
- Authoritative scRNA gene universe: 20,611 unique genes.
- Ensembl→symbol mapping: 18,984/20,611 (92.03%).
- LIANA consensus resource: 4,620 unique LR pairs / 2,016 unique LR genes.
- LR-gene representation: 1,365/2,016 (67.71%).
- Symbol duplication audit: 42 mapped rows corresponding to 21 duplicated gene symbols.
- Duplicated symbols will not be arbitrarily discarded; explicit deterministic handling is required before LIANA inference.
- No new biological datasets downloaded; raw/frozen inputs remain unmodified.

## Layer 7 — Cell–Cell Communication — FINAL — 2026-10-04

### Status
**COMPLETE**

### Authoritative inputs and outputs
- LIANA gene mapping: `05_analysis/ceif_liana_gene_mapping_v2.tsv`
- SC001 LIANA consensus: `05_analysis/ceif_liana_SC001_consensus_v1.tsv`
- SC002 LIANA consensus: `05_analysis/ceif_liana_SC002_consensus_v1.tsv`
- SC003 LIANA consensus: `05_analysis/ceif_liana_SC003_consensus_v1.tsv`
- SC004 LIANA consensus: `05_analysis/ceif_liana_SC004_consensus_v1.tsv`
- Cross-dataset LR conservation: `05_analysis/ceif_liana_conserved_lr_pairs_v1.tsv`
- Candidate communication prioritization: `05_analysis/ceif_liana_candidate_communication_prioritization_v1.tsv`
- Candidate intercellular communication: `05_analysis/ceif_liana_candidate_intercellular_communication_v1.tsv`
- Final Layer 7 evidence table: `05_analysis/ceif_layer7_final_communication_evidence_v1.tsv`

### Gene mapping QC
- Authoritative common-gene universe: 20,611 genes.
- Mapped to HGNC symbols: 18,966 (92.02%).
- Unmapped: 1,645.
- Ambiguous reference genes excluded: 0.
- Duplicated HGNC symbol entries: 3.
- `ceif_liana_gene_mapping_v1.tsv` is **SUPERSEDED / INVALID FOR INFERENCE** because it contained 20,629 rows and caused dimensional inconsistency. It is retained only for audit/provenance.
- V2 is the sole authoritative LIANA mapping.

### LIANA configuration
- LIANA+ 1.10.0.
- Built-in `consensus` resource.
- Consensus resource: 4,620 LR pairs and 2,016 LR genes.
- LR genes present after mapping: 1,362 / 2,016 (67.56%).
- Constant parameters across all four datasets:
  - `expr_prop=0.10`
  - `min_cells=20`
  - `aggregate_method=rra`
  - `n_perms=1000`
  - `seed=1337`
  - `n_jobs=1`
  - `use_raw=False`

### Dataset-level inference
- SC001: 32,135 cells; 149,776 LIANA result rows.
- SC002: 52,165 cells; 84,570 LIANA result rows.
- SC003: 515 cells; 53,400 LIANA result rows.
- SC004: 19,868 cells; 38,341 LIANA result rows.
- All four outputs passed schema validation.
- All four outputs had zero missing values.
- LIANA excluded cluster identities below the `min_cells=20` threshold; no forced retention was performed.

### Cross-dataset ligand–receptor conservation
- Total unique LR pairs observed: 2,514.
- Supported in all four datasets: 682.
- Supported in three datasets: 740.
- Supported in two datasets: 491.
- Supported in one dataset: 601.
- Supported in at least two datasets: 1,913.

### Candidate-focused communication
- Candidate clusters: 23, 24, 25.
- Initial candidate-involving configurations: 66,583.
- After removing self-edges, candidate intercellular configurations: 63,667.
- Candidate intercellular configurations supported in at least two datasets: 11,009.
- Replicated in three datasets: 979.
- Replicated in two datasets: 10,030.
- Replicated in all four datasets: 0.
- Therefore, **no candidate-specific intercellular edge is classified as four-dataset conserved** under the final non-self-edge criterion.

### Biological interpretation
- Cluster 23 remains the strongest malignant candidate, but remains **MALIGNANT_CANDIDATE_ONLY**; LIANA communication does not establish malignancy.
- The replicated candidate communication network includes recurrent inferred interactions between epithelial candidate populations and myeloid, fibroblast, endothelial, lymphoid, B-cell, plasma-cell, smooth-muscle/pericyte and other compartments.
- The strongest replicated examples include myeloid → candidate-23 and candidate-23 → myeloid/T-cell configurations.
- Candidate 23 is therefore a prominent communication hub within the current computational evidence framework.
- Cluster numbers are not assumed to represent biologically equivalent cell types across datasets without annotation/provenance support.
- Self-interactions were excluded from the final intercellular evidence table.
- LIANA outputs represent **computationally inferred communication**, not experimental proof of physical ligand–receptor binding, cellular contact, or causal signaling.
- Repeated inference across datasets is treated as reproducibility evidence, not mechanistic validation.
- No causal claims are made from Layer 7 alone.

### Layer 7 evidence conclusion
Layer 7 is **COMPLETE**. The authoritative result is the final intercellular evidence table:
`05_analysis/ceif_layer7_final_communication_evidence_v1.tsv`

The final CEIF-X interpretation should use the replicated ≥2-dataset intercellular network as the primary communication evidence and retain single-dataset signals only as lower-confidence exploratory evidence.

## Layer 8 — Regulatory / Network Analysis — TF Activity Alignment Correction

### Activity-to-cell alignment
- The initial ULM activity matrices contained positional row indices (`0..N-1`) because the normalized AnnData objects used positional cell indices.
- Direct string matching against the authoritative clustering IDs therefore produced zero matches.
- No ULM results were discarded or rerun.
- The activity rows were aligned to the authoritative Leiden clustering cell order by validated row position.
- This positional alignment is supported by the previously completed normalized-expression/clustering alignment QC.
- SC001–SC004 activity matrices now carry authoritative clustering cell IDs.
- Adjusted p-value matrices were aligned identically.
- Alignment validation requires exact row count, unique cell IDs, correct dataset suffix, and exact order agreement with the clustering subset.

### Corrected outputs
- Aligned TF activity:
  `05_analysis/ceif_layer8_tf_activity_v1/*_TF_activity_ULM_ES_aligned_v1.tsv`
- Aligned ULM adjusted p-values:
  `05_analysis/ceif_layer8_tf_activity_v1/*_TF_activity_ULM_padj_aligned_v1.tsv`

### Layer 8 status
**TF ACTIVITY–CLUSTER ALIGNMENT COMPLETE — REGULATORY PRIORITIZATION READY**


## LAYER 8 — REGULATORY / NETWORK PRIORITIZATION — FINALIZED

- DoRothEA A/B regulatory network and ULM TF activity inference completed.
- TF activity and adjusted-p-value matrices were aligned to authoritative clustering cell IDs for all four scRNA datasets; alignment QC PASS.
- Cluster-level TF activity summaries generated from aligned matrices.
- Recurrent TF rule: TF present in the top-20 absolute ULM activity ranking for the same cluster in >=2 datasets.
- Candidate-focused regulatory activity generated for clusters 23, 24 and 25.
- Outputs: ceif_layer8_cluster_tf_activity_v1.tsv; ceif_layer8_recurrent_tf_activity_v1.tsv; ceif_layer8_malignant_candidate_tf_activity_v1.tsv; ceif_layer8_regulatory_prioritization_qc_v1.tsv.
- Regulatory activity represents computational TF-activity inference, not direct TF binding or causal regulation.
- Clusters 23–25 remain malignant candidates only; no malignant-cell confirmation is inferred from TF activity alone.
- Raw data and frozen outputs remain unmodified.


## LAYER 9 — CROSS-CANCER CONSERVATION — COMPLETE

- Cross-dataset conservation was evaluated using the existing four scRNA datasets and existing Layer 8 TF-activity outputs.
- Regulatory conservation was defined as recurrence of the same TF within the same Leiden 0.8 cluster across >=2 datasets.
- Candidate-focused conservation was evaluated for clusters 23, 24 and 25.
- This layer measures computational recurrence/conservation, not biological identity or causal conservation across cancers.
- Cluster 23–25 remain candidate epithelial/malignant populations only; their strong SC002 representation remains an explicit interpretation constraint.
- No new biological datasets were acquired.
- Raw data and frozen outputs remain unmodified.


## LAYER 10 — ML / PREDICTIVE LAYER — AUDIT

- Existing integrated cohort, molecular signal set, survival endpoint and Cox results were audited before model construction.
- No predictive model was trained at this audit stage.
- Model training/design will proceed only after feature matrix, endpoint, identifier alignment and leakage-control requirements are explicitly validated.
- No new biological datasets were acquired.
- Raw data and frozen outputs remain unmodified.


## LAYER 10 — BULK ↔ CASE ALIGNMENT — COMPLETE

- Authoritative survival cases were aligned to selected bulk RNA-seq sample IDs using the existing CEIF bulk-case mapping.
- Survival endpoint validation used os_time_days and os_event; only valid positive survival times with binary event status entered the ML alignment.
- Bulk matrix sample identifiers were explicitly checked against selected bulk sample IDs before model construction.
- Reproducible molecular signal genes were checked against the bulk feature universe.
- No predictive model was trained during this step.
- Output: ceif_layer10_ml_case_bulk_alignment_v1.tsv and ceif_layer10_ml_bulk_case_alignment_qc_v1.tsv.
- This alignment is a prerequisite for leakage-controlled ML/predictive modeling.
- Raw data and frozen outputs remain unmodified.


## LAYER 10 — LEAKAGE-CONTROLLED ML — COMPLETE

- A 5-fold stratified outer ML analysis was performed using the existing 1,356 reproducible molecular signals.
- Feature selection was performed independently within each training fold to prevent information leakage.
- Standardization and imputation were fitted within training folds only.
- Logistic regression was evaluated using ROC-AUC and average precision for event discrimination.
- This analysis is a predictive discrimination layer and is not equivalent to a time-to-event survival model.
- Predictive performance does not establish causality or clinical utility.
- Raw data and frozen outputs remain unmodified.


## LAYER 11 — ORTHOGONAL / INTERNAL VALIDATION — COMPLETE

- ML-recurrent features were cross-checked against the pre-existing univariate Cox survival evidence and reproducible molecular signal evidence.
- Validation used only previously acquired CEIF data and frozen analytical outputs; no new biological dataset was introduced.
- External independent-cohort validation is NOT available within the current frozen dataset scope and is therefore not claimed.
- Orthogonal support is evidence concordance, not independent replication and not causal validation.
- Predictive performance and molecular/survival associations should not be interpreted as clinical utility.
- Raw data and frozen outputs remain unmodified.


## LAYER 12 — INTEGRATED EVIDENCE / CANDIDATE PRIORITIZATION — COMPLETE

- Existing Layers 4–11 were integrated without rerunning upstream analyses.
- Candidate clusters 23, 24 and 25 were retained as CANDIDATE_ONLY.
- Evidence domains integrated: epithelial/malignant-candidate evidence, tumor-state evidence, replicated communication, regulatory TF activity, and cross-dataset conservation.
- ML recurrence and orthogonal validation were retained as gene-level evidence and were not artificially assigned to individual cell clusters.
- Candidate ranking is an evidence-convergence prioritization and is not a malignancy probability, causal score, or clinical utility estimate.
- External independent validation remains unavailable within the frozen dataset scope.
- Raw data and frozen outputs remain unmodified.


## LAYER 13 — LUAD PLASTICITY / STATE HETEROGENEITY — COMPLETE

- Existing epithelial candidate tumor-state and state-resolution outputs were integrated without new biological data.
- Candidate clusters 23–25 were evaluated for multi-domain state heterogeneity relative to epithelial/state comparators.
- State heterogeneity is interpreted as a cross-sectional phenotype; no temporal transition or lineage transition is claimed.
- Malignant status remains CANDIDATE_ONLY.
- Dataset restriction of candidate clusters is retained as an interpretation constraint.
- Raw data and frozen outputs remain unmodified.


## LAYER 14 — STRUCTURAL / DOCKING EVIDENCE GATE — COMPLETE

- Layer 12 biological evidence prioritization was reviewed before structural analysis.
- Layer 13 LUAD state evidence was incorporated as contextual evidence.
- No specific molecular target/protein-ligand hypothesis was treated as validated solely from cell-state or TF evidence.
- Structural/docking authorization is therefore BLOCKED pending an explicit, independently defensible molecular-target evidence chain.
- No docking or structural computation was initiated at this gate.
- Raw data and frozen outputs remain unmodified.


## LAYER 15 — FINAL CROSS-LAYER SYNTHESIS — COMPLETE

- Layers 1–14 were integrated into a final evidence matrix and candidate synthesis.
- Candidate cluster 23 remains the highest-ranked evidence-convergence candidate (score 0.80), followed by clusters 24 (0.55) and 25 (0.30).
- Malignant identity remains CANDIDATE_ONLY; no causal or therapeutic claim is made.
- Communication, regulatory, conservation, ML, and validation evidence retain their computational/internal interpretation limits.
- LUAD plasticity remains a cross-sectional state-heterogeneity question; temporal or lineage transition is not established.
- Structural/docking analysis remains BLOCKED pending a defensible molecular target/protein-ligand evidence chain.
- External independent validation remains unavailable.
- Raw data and frozen outputs remain unmodified.


## LAYER 10 — SURVIVAL ENDPOINT AUDIT / EVENT-COUNT RESOLUTION — VALIDATED

- The authoritative OS endpoint contains 2,332 cases and 650 records with os_event=1.
- Of these 650 deaths, 176 have valid positive death times and 474 have missing death times.
- Seven censored records also lack valid censoring times.
- Therefore the valid time-to-event analytical cohort contains 1,814 cases: 173 events and 1,641 censored observations.
- The Layer 10 ML alignment contains exactly these 1,814 valid time-to-event cases and all 173 valid events; no events were lost during bulk mapping.
- The 650-event count must not be used as the event count for time-to-event analyses because 474 deaths lack an analyzable death time.
- The Layer 10 predictive analysis is binary event discrimination within the valid time-to-event cohort and is not a replacement for survival modeling.
- This endpoint distinction will be explicitly reported in the manuscript and reviewer response.
- Raw data and frozen outputs remain unmodified.

## REVIEWER REMEDIATION — scRNA INDIVIDUAL-LEVEL REPLICATION / PSEUDOREPLICATION AUDIT — VALIDATED

- Authoritative retained scRNA cohort contains 104,683 cells from 30 individuals:
  SC001 = 3, SC002 = 9, SC003 = 14, SC004 = 4.
- H5AD-to-manifest positional alignment was independently validated for all 104,683 cells by exact dataset/accession agreement; no forced cell-ID mapping was used.
- Corrected individual × Leiden-0.8 cluster robustness analysis completed:
  `05_analysis/ceif_scrna_individual_cluster_robustness_v2.tsv`
- Candidate cluster 23 was observed in 25/30 individuals overall:
  SC001 3/3, SC002 9/9, SC003 10/14, SC004 3/4.
- Candidate cluster 24 was observed in 9 individuals:
  SC001 1/3, SC002 4/9, SC003 4/14.
- Candidate cluster 25 was observed in 13 individuals:
  SC002 9/9, SC003 4/14.
- Therefore cluster 23 has the strongest individual-level replication; clusters 24 and 25 remain more dataset-restricted and heterogeneous.
- Individual-level replication addresses cell-level pseudoreplication as a reviewer concern for cluster presence, but does not establish patient-level bulk/CNV linkage, malignancy, or causal biological validity.
- No patient_id/sample_id/case_id/donor_id/library_id fields were available; `individual` is the available biological replication identifier.
- The existing SC002 dominance of candidate clusters and the lack of authoritative cell-to-case/CNV linkage remain explicit limitations.
- Raw data and frozen outputs unmodified.



## LAYER 7 — SIZE-MATCHED COMMUNICATION SENSITIVITY — COMPLETE

- A donor-balanced, size-matched sensitivity analysis was performed using the existing four scRNA datasets and the fixed random selection seed 20261004.
- The four sensitivity inputs contained 19,050, 17,424, 154, and 15,532 cells for SC001–SC004, respectively, with 18,963 unique HGNC symbols per dataset.
- LIANA 1.10.0 was rerun using the same consensus resource and original analytical configuration: expr_prop=0.1, min_cells=5, aggregate_method=rra, de_method=t-test, n_perms=1000, seed=1337, n_jobs=1.
- All four size-matched LIANA runs completed successfully.
- Unique sensitivity edges: 403,891.
- Dataset recurrence among sensitivity edges: 330,646 occurred in 1 dataset, 62,580 in 2 datasets, 10,076 in 3 datasets, and 589 in all 4 datasets.
- Comparison with the authoritative Layer 7 evidence set showed that 9,716 of 11,009 original edges (88.25%) recurred in at least 2 size-matched datasets.
- 3,644 of 11,009 original edges (33.10%) recurred in at least 3 size-matched datasets.
- 239 of 11,009 original edges (2.17%) recurred in all 4 size-matched datasets.
- This sensitivity analysis supports robustness of the majority of the original computational communication evidence to donor/cell-size normalization.
- These remain repeated computational inferences and must not be described as experimentally validated ligand-receptor interactions.
- Raw data and frozen outputs remain unmodified.

## LAYER 8 — REGULATORY/NETWORK ANALYSIS — AB vs ABC SENSITIVITY COMPLETE
- Reviewer-remediation sensitivity evaluated DoRothEA AB versus ABC network-confidence definitions using the existing four scRNA datasets only; no new biological datasets were introduced.
- AB network: 15,117 edges, 367 TFs.
- ABC network: 32,286 edges, 429 TFs.
- All 92 recurrent TFs and all 43 candidate TFs were represented in both networks; TF-membership robustness passed.
- ABC-network ULM sensitivity was independently rerun for SC001–SC004 using the authoritative positional gene-index → HGNC mapping and the same ULM configuration (`tmin=5`, `raw=False`, `empty=True`, `bsize=250000`).
- ABC ULM completed successfully for all four datasets with finite activity values:
  SC001 32,135 cells; SC002 52,165 cells; SC003 515 cells; SC004 19,868 cells.
- AB-versus-ABC activity was compared at matched dataset × Leiden 0.8 cluster × TF level using validated positional cell alignment.
- Total matched comparisons: 14,647 across the four datasets.
- Recurrent TF activity concordance was strong across datasets: Pearson r = 0.909–0.946 and Spearman rho = 0.865–0.918.
- Candidate TF activity concordance was also strong: Pearson r = 0.949–0.961 and Spearman rho = 0.906–0.927.
- Therefore the recurrent/candidate regulatory activity prioritization was robust to expansion from the AB to ABC DoRothEA confidence network.
- This sensitivity supports robustness of computational TF-activity prioritization, but does not establish direct TF-DNA binding, biological causality, or experimental regulatory validation.
- Layer 8 remains computational regulatory inference.
- Raw biological data and frozen outputs were not modified.

## LAYER 12 — EVIDENCE INTEGRATION / CANDIDATE PRIORITIZATION — SENSITIVITY COMPLETE
- Reviewer-remediation audit identified a schema defect in the original integrated score: `replicated_communication_edges` was present in Layer 7 but entered Layer 12 as zero for all candidates.
- Layer 7 contained 6,117 candidate-involved replicated communication edges for cluster 23, 5,251 for cluster 24, and 0 for cluster 25.
- Communication evidence was therefore re-specified transparently rather than silently modifying the original score.
- Sensitivity tested three treatments: communication excluded; binary presence of replicated communication evidence; and stronger communication presence requiring replication across >=3 datasets.
- Candidate ordering remained identical under all three treatments: cluster 23 rank 1, cluster 24 rank 2, cluster 25 rank 3.
- Scores:
  without communication: 23=1.00, 24=0.6875, 25=0.3750;
  communication presence: 23=1.00, 24=0.75, 25=0.30;
  >=3-dataset communication presence: 23=1.00, 24=0.55, 25=0.30.
- Therefore final candidate prioritization is robust to the communication-component specification tested.
- The integrated score remains an evidence-convergence prioritization metric, not a malignancy probability, causal score, or clinical utility score.
- Candidate status remains CANDIDATE_ONLY; external validation remains unavailable.
- Raw biological data and frozen outputs were not modified.

## LEGACY CVS/EDS DISPOSITION — CLOSED
- The original CVS/EDS source tables, scripts, and authoritative calculation artifacts are not present in the rebuilt CEIF-X repository.
- No surviving source artifact permits a defensible reconstruction of the legacy CVS/EDS values.
- The legacy CVS/EDS and Integrated Score are therefore not recreated, estimated, or retrofitted into CEIF-X.
- The reviewer-identified normalization/arithmetic and weighting problems are addressed by removal of the legacy scoring architecture.
- CEIF-X candidate prioritization uses transparent evidence convergence with explicit communication-scoring sensitivity rather than CVS/EDS.
- This disposition is documented in `05_analysis/ceif_legacy_cvs_eds_disposition_v1.tsv`.

## LEGACY LUAD THREE-GENE SIGNATURE DISPOSITION — CLOSED
- The rebuilt CEIF-X authoritative survival artifacts were audited for the legacy AKAP12/ADM/TM4SF1 three-gene signature.
- No residual rows for AKAP12, ADM, or TM4SF1 were found in the four audited authoritative survival tables.
- The old three-gene prognostic signature is not part of rebuilt CEIF-X candidate prioritization or final conclusions.
- No retrospective reconstruction or same-cohort validation of the legacy signature will be performed.
- Current CEIF-X survival analyses remain separate gene-level molecular-survival evidence and are not presented as the legacy three-gene signature.
- Disposition recorded in `05_analysis/ceif_legacy_luad_three_gene_signature_disposition_v1.tsv`.

## LAYER 4 MALIGNANT-CELL CLAIM DISPOSITION — CLOSED
- Current CEIF-X candidates 23, 24, and 25 remain MALIGNANT_CANDIDATE_ONLY.
- Malignancy is not confirmed.
- Cell-level CNV validation remains blocked because authoritative cell-to-case/sample linkage is unavailable.
- Epithelial marker and tumor-state evidence are not treated as definitive proof of malignancy.
- No manuscript-facing malignant-cell overclaim was detected in the audited current outputs.
- Disposition recorded in `05_analysis/ceif_layer4_malignant_claim_disposition_v1.tsv`.

## scRNA REPLICATION AND LINKAGE LIMITATION — CLOSED
- Individual-level cluster recurrence is supported by the existing scRNA robustness analysis.
- The retained scRNA manifest provides dataset, accession, cell, and individual metadata.
- A universal patient/sample/case/donor/library identifier linking scRNA cells to the bulk/CNV/clinical cohort is unavailable.
- Therefore scRNA recurrence is not described as patient-level molecular validation.
- No forced cross-modality cell-to-patient/sample linkage is performed.
- Cross-dataset recurrence is interpreted as dataset-level/individual-level reproducibility within the available scRNA resources.
- Disposition recorded in `05_analysis/ceif_layer3_scrna_replication_limitation_v1.tsv`.

### Layer 12 — Evidence Integration / Candidate Prioritization — FINAL REBUILD

Status: COMPLETE — TRANSPARENT EVIDENCE CONVERGENCE; NO ARBITRARY COMPOSITE SCORE

Authoritative output:
- 05_analysis/ceif_layer12_evidence_convergence_matrix_v3.tsv

Evidence dimensions integrated:
- malignant-candidate evidence
- epithelial/tumor-state evidence
- recurrent TF activity
- cross-dataset regulatory conservation
- candidate-associated communication recurrence

Candidate findings:
- Cluster 23: CANDIDATE_ONLY; STRONGEST_CANDIDATE; 5 malignant-associated hits; 21 recurrent TFs; 10 TFs recurrent across all 4 datasets; 11 TFs shared across all three candidate clusters; 6,117 communication edges supported in >=2 datasets and 979 in >=3 datasets; HIGH_REPLICATION_3_DATASETS; MULTI_LAYER_REPLICATED_CANDIDATE.
- Cluster 24: CANDIDATE_ONLY; CANDIDATE; 3 malignant-associated hits; 19 recurrent TFs; 0 TFs recurrent across all 4 datasets; 11 TFs shared across all three candidate clusters; 5,251 communication edges supported in >=2 datasets and 0 in >=3 datasets; REPLICATED_2_DATASETS; CANDIDATE_WITH_LIMITED_CONVERGENCE.
- Cluster 25: CANDIDATE_ONLY; CANDIDATE; 3 malignant-associated hits; 11 recurrent TFs; 0 TFs recurrent across all 4 datasets; 11 TFs shared across all three candidate clusters; no communication edges supported in >=2 datasets; SINGLE_DATASET_ONLY; CANDIDATE_WITH_LIMITED_CONVERGENCE.

Authoritative conserved-TF evidence:
- 11 TFs shared across all three candidate clusters:
  MYC; E2F4; ETS1; VDR; AR; EGR1; ATF6; HIF1A; NFYB; NFYA; SRF
- 4 TFs shared across candidates 23 and 24:
  SP1; USF1; MAX; ESR2

Interpretation constraints:
- All three clusters remain CANDIDATE_ONLY.
- No authoritative cell-to-case/sample linkage exists for CNV validation.
- Communication represents computational ligand-receptor inference, not experimentally demonstrated physical interaction.
- TF activity represents regulon/activity inference, not direct TF binding or causal regulation.
- Cross-dataset recurrence represents computational conservation/replication, not causality.
- Evidence is cross-sectional.
- No arbitrary weighted composite score is used.
- No causal or therapeutic target claim is made from Layer 12 alone.

Prior legacy Layer-12 weighted scores are superseded and must not be used in the manuscript.

Validation:
- Output exists and was generated from authoritative Layer 7, Layer 8, Layer 9, malignant-candidate, and tumor-state evidence.
- RAW DATA UNMODIFIED.
- FROZEN OUTPUTS PRESERVED.


### Layer 14 — Target Identification / Structural Evidence Gate — FINAL

Status: COMPLETE — TARGET PRIORITIZATION; STRUCTURAL/DOCKING GATE CLOSED

Authoritative outputs:
- 05_analysis/ceif_layer14_direct_receptor_expression_gate_v2.tsv
- 05_analysis/ceif_layer14_direct_receptor_expression_summary_v1.tsv
- 05_analysis/ceif_layer14_final_structural_target_disposition_v1.tsv

Final target interpretation:
- LTBR is the strongest current biological target candidate based on communication evidence, clinical association, and direct candidate-cell expression replicated across all datasets containing the candidate.
- TNFRSF10B is retained as a secondary biological target candidate with weaker expression magnitude.
- No PDB/PDBQT structural files are present in the CEIF-X repository.
- No defensible structural setup exists in the current project.
- Docking is therefore BLOCKED.
- No external protein-structure acquisition or new biological-data acquisition was performed.
- Target engagement is not demonstrated.
- Therapeutic efficacy or targetability is not established.
- Prior legacy docking claims are not carried forward.

Interpretation limitations:
- Candidate clusters remain CANDIDATE_ONLY rather than confirmed malignant populations.
- Communication is computational ligand-receptor inference, not experimentally demonstrated physical interaction.
- Clinical association does not establish therapeutic utility.
- Gene expression does not establish receptor function or target engagement.
- Structural evidence is unavailable.

Validation:
- RAW DATA UNMODIFIED.
- FROZEN OUTPUTS PRESERVED.

### Layer 15 — Final Cross-Layer Synthesis — COMPLETE

Authoritative outputs:
- 05_analysis/ceif_layer15_final_cross_layer_synthesis_v1.tsv
- 05_analysis/ceif_layer15_final_cross_layer_synthesis_summary_v1.tsv

Final synthesis:
- Three epithelial candidate clusters (23, 24, 25) remain CANDIDATE_ONLY; no cluster is declared definitively malignant.
- Cluster 23 is the strongest candidate based on malignant-associated evidence and the strongest multi-layer replicated convergence.
- Eleven regulatory TFs are conserved across all three candidate clusters: MYC, E2F4, ETS1, VDR, AR, EGR1, ATF6, HIF1A, NFYB, NFYA, and SRF.
- Communication evidence differs materially by candidate: cluster 23 has 3-dataset replicated communication evidence; cluster 24 has 2-dataset replication; cluster 25 has only single-dataset communication evidence.
- LTBR is the strongest current biological target candidate; TNFRSF10B is secondary.
- No structural files are available in the CEIF-X repository; docking remains BLOCKED.
- Target engagement, causality, confirmed malignancy, and therapeutic utility are not established.
- External independent validation remains unavailable.
- No arbitrary integrated numerical score is used.
- All conclusions are explicitly framed as computational evidence/convergence rather than causal or therapeutic proof.

RAW DATA: UNMODIFIED
FROZEN OUTPUTS: PRESERVED
