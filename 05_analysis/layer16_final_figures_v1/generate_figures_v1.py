from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

OUT = Path("05_analysis/layer16_final_figures_v1")
OUT.mkdir(parents=True, exist_ok=True)

def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)

# ---------------- FIGURE 1 ----------------
fig, ax = plt.subplots(figsize=(11,7))
ax.axis("off")
steps = [
    ("1", "Four scRNA datasets\n105,328 cells"),
    ("2", "QC + harmonization\n104,683 retained cells"),
    ("3", "34-cluster ecosystem\nannotation + uncertainty"),
    ("4", "Candidate epithelial states\n23 / 24 / 25"),
    ("5", "Regulatory + communication\ncross-dataset recurrence"),
    ("6", "Clinical / ML evidence\ninternal validation"),
    ("7", "Evidence convergence\ncandidate prioritization"),
    ("8", "Target gate\nLTBR prioritized; docking blocked"),
]
for i,(n,t) in enumerate(steps):
    x = (i % 4)*2.6
    y = 1.5 if i < 4 else -0.5
    ax.text(x,y,n,ha="center",va="center",fontsize=18,fontweight="bold",
            bbox=dict(boxstyle="circle,pad=0.35",fill=False))
    ax.text(x,y-0.75,t,ha="center",va="top",fontsize=10)
for x in [1.3,3.9,6.5]:
    ax.annotate("",xy=(x+0.7,1.5),xytext=(x,1.5),
                arrowprops=dict(arrowstyle="->",lw=1.5))
for x in [1.3,3.9,6.5]:
    ax.annotate("",xy=(x+0.7,-0.5),xytext=(x,-0.5),
                arrowprops=dict(arrowstyle="->",lw=1.5))
ax.annotate("",xy=(0,-0.1),xytext=(0,1.15),
            arrowprops=dict(arrowstyle="->",lw=1.5))
ax.set_xlim(-1,9)
ax.set_ylim(-2,2.7)
ax.set_title("CEIF-X analytical framework",fontsize=16,fontweight="bold")
save(fig,"Figure_1_CEIF_X_Analytical_Framework")

# ---------------- FIGURE 2 ----------------
cohort=pd.read_csv(OUT/"Fig2_Cohort_source.tsv",sep="\t")
comp=pd.read_csv(OUT/"Fig2_Cluster_Dataset_Composition_source.tsv",sep="\t")
unc=pd.read_csv(OUT/"Fig2_Annotation_Uncertainty_source.tsv",sep="\t")

fig,axs=plt.subplots(1,3,figsize=(15,5))
axs[0].bar(cohort.dataset_id,cohort.cases)
axs[0].set_title("Retained cells by dataset")
axs[0].set_ylabel("Cells")

axs[1].bar(comp.cluster.astype(str),comp.total)
axs[1].set_title("34-cluster ecosystem")
axs[1].set_xlabel("Leiden cluster")
axs[1].set_ylabel("Cells")
axs[1].tick_params(axis="x",rotation=90)

counts=unc.annotation_uncertainty.value_counts()
axs[2].bar(counts.index,counts.values)
axs[2].set_title("Annotation uncertainty")
axs[2].set_ylabel("Clusters")

save(fig,"Figure_2_scRNA_Ecosystem_Architecture")

# ---------------- FIGURE 3 ----------------
mk=pd.read_csv(OUT/"Fig3_Malignant_Candidate_Markers_source.tsv",sep="\t")
ts=pd.read_csv(OUT/"Fig3_Tumor_State_source.tsv",sep="\t")
cand=mk[mk.cluster.isin([23,24,25])].copy()

fig,axs=plt.subplots(1,2,figsize=(12,5))
x=np.arange(3)
axs[0].bar(x-0.18,cand.epithelial_marker_hits,width=.36,label="Epithelial")
axs[0].bar(x+0.18,cand.malignant_associated_hits,width=.36,label="Malignant-associated")
axs[0].set_xticks(x,cand.cluster.astype(str))
axs[0].set_xlabel("Candidate cluster")
axs[0].set_ylabel("Marker hits")
axs[0].set_title("Candidate epithelial/malignancy evidence")
axs[0].legend()

row=ts.iloc[0:3].copy()
states=["EPITHELIAL_DIFFERENTIATION","SECRETORY","INTERFERON",
        "EMT","STRESS_HYPOXIA","EGFR_ERBB","PROLIFERATION","CELL_CYCLE"]
for i,s in enumerate(states):
    cols=[c for c in ts.columns if c.startswith(s+"_hits")]
    vals=row[cols].apply(pd.to_numeric,errors="coerce").mean(axis=1).values
    axs[1].plot([23,24,25],vals,marker="o",label=s.replace("_"," "))
axs[1].set_xlabel("Candidate cluster")
axs[1].set_ylabel("Mean panel hits")
axs[1].set_title("Tumor-state panel profiles")
axs[1].legend(fontsize=7)

save(fig,"Figure_3_Candidate_Epithelial_States")

# ---------------- FIGURE 4 ----------------
tf=pd.read_csv(OUT/"Fig4_Candidate_TF_Conservation_source.tsv",sep="\t")
tf=tf.sort_values("mean_abs_ULM_ES",ascending=False).head(11)

fig,ax=plt.subplots(figsize=(8,6))
ax.barh(tf.TF[::-1],tf.mean_abs_ULM_ES[::-1])
ax.set_xlabel("Mean absolute ULM enrichment score")
ax.set_ylabel("TF")
ax.set_title("TFs conserved across candidate clusters")
save(fig,"Figure_4_Regulatory_Conservation")

# ---------------- FIGURE 5 ----------------
comm=pd.read_csv(OUT/"Fig5_Communication_source.tsv",sep="\t")
rec=comm.groupby("dataset_support_n").size()
fig,axs=plt.subplots(1,2,figsize=(12,5))
axs[0].bar(rec.index.astype(str),rec.values)
axs[0].set_xlabel("Number of supporting datasets")
axs[0].set_ylabel("Communication edges")
axs[0].set_title("Cross-dataset communication recurrence")

cand_edges=comm[comm.candidate_source.eq(True) | comm.candidate_target.eq(True)] \
    if comm["candidate_source"].dtype==bool else comm
direction=comm.communication_direction.value_counts()
axs[1].bar(direction.index,direction.values)
axs[1].set_ylabel("Edges")
axs[1].set_title("Candidate communication direction")
axs[1].tick_params(axis="x",rotation=25)

save(fig,"Figure_5_Cell_Cell_Communication")

# ---------------- FIGURE 6 ----------------
fold=pd.read_csv(OUT/"Fig6_ML_Fold_Results_source.tsv",sep="\t")
summ=pd.read_csv(OUT/"Fig6_ML_Summary_source.tsv",sep="\t").iloc[0]
km=pd.read_csv(OUT/"Fig6_KM_source.tsv",sep="\t")

fig,axs=plt.subplots(1,3,figsize=(15,5))
axs[0].plot(fold.fold,fold.roc_auc,marker="o")
axs[0].axhline(.5,linestyle="--")
axs[0].set_xlabel("Outer fold")
axs[0].set_ylabel("ROC-AUC")
axs[0].set_title("5-fold ML performance")

axs[1].plot(km.time_days,km.survival_probability)
axs[1].set_xlabel("Time (days)")
axs[1].set_ylabel("Survival probability")
axs[1].set_title("Overall survival")

audit=pd.read_csv(OUT/"Fig6_Endpoint_Audit_source.tsv",sep="\t")
axs[2].bar(audit.cohort_definition,audit.n_cases)
axs[2].set_ylabel("Cases")
axs[2].set_title("Survival endpoint audit")
axs[2].tick_params(axis="x",rotation=45)

save(fig,"Figure_6_Clinical_ML_Evidence")

# ---------------- FIGURE 7 ----------------
ev=pd.read_csv(OUT/"Fig7_Evidence_Convergence_source.tsv",sep="\t")
metrics=[
    "malignant_associated_hits","epithelial_marker_hits","recurrent_TF_count",
    "candidate_conserved_TF_count","communication_edges_2plus",
    "communication_edges_3plus"
]
fig,ax=plt.subplots(figsize=(10,6))
for _,r in ev.iterrows():
    vals=[]
    for m in metrics:
        v=pd.to_numeric(r[m],errors="coerce")
        vals.append(np.log1p(v) if pd.notna(v) else 0)
    ax.plot(metrics,vals,marker="o",label=f"Cluster {int(r.candidate_cluster)}")
ax.set_ylabel("log(1 + evidence count)")
ax.set_title("Evidence convergence across candidate states")
ax.tick_params(axis="x",rotation=35)
ax.legend()
save(fig,"Figure_7_Evidence_Convergence")

# ---------------- FIGURE 8 ----------------
expr=pd.read_csv(OUT/"Fig8_Receptor_Expression_source.tsv",sep="\t")
fig,axs=plt.subplots(1,2,figsize=(12,5))
for target in expr.target.unique():
    q=expr[expr.target.eq(target)]
    axs[0].plot(q.candidate_cluster,q.mean_detection_fraction,
                marker="o",label=target)
axs[0].set_xlabel("Candidate cluster")
axs[0].set_ylabel("Mean detection fraction")
axs[0].set_title("Candidate-cell receptor expression")
axs[0].legend()

gate=pd.read_csv(OUT/"Fig8_Structural_Gate_source.tsv",sep="\t")
status_cols=["communication_evidence","clinical_evidence",
             "direct_candidate_cell_expression","structural_evidence_in_repository",
             "docking_status","target_engagement"]
mat=[]
for _,r in gate.iterrows():
    vals=[]
    for c in status_cols:
        s=str(r[c]).upper()
        vals.append(1 if any(z in s for z in ["PRESENT","AVAILABLE","PRIORITIZED"]) and
                    "NOT_" not in s and "BLOCKED" not in s and "NO" not in s else 0)
    mat.append(vals)
mat=np.array(mat)
axs[1].imshow(mat,aspect="auto")
axs[1].set_xticks(range(len(status_cols)),[x.replace("_"," ") for x in status_cols],rotation=45,ha="right")
axs[1].set_yticks(range(len(gate)),gate.candidate_target)
axs[1].set_title("Target evidence gate")
save(fig,"Figure_8_Target_Gate")

print("L16-R3 FIGURE GENERATION COMPLETE")
for i in range(1,9):
    print(f"Figure {i}: PNG + PDF")
