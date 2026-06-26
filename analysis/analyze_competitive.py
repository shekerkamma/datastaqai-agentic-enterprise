#!/usr/bin/env python3
"""AI-analyst pass over the competitive dataset: validated findings + branded charts.
Source: competitive_dataset.csv (figures traced to COMPETITIVE_*.md). No invented numbers;
blanks are blanks. Competitive density is labeled judgment, not measured.
"""
import csv, os
from collections import Counter, defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY="#0A1628"; TEAL="#00C9A7"; GOLD="#FFB800"; CORAL="#E05A6B"; AMBER="#F2A83B"; MUTED="#5B6B7C"; INK="#1B2B3C"; LT="#E0F7F1"
plt.rcParams.update({"font.family":"DejaVu Sans","axes.edgecolor":MUTED,"axes.labelcolor":INK,
                     "xtick.color":INK,"ytick.color":INK,"text.color":INK,"figure.dpi":140})

rows=[]
with open(os.path.join(HERE,"competitive_dataset.csv")) as f:
    for r in csv.DictReader(f): rows.append(r)
def fnum(x):
    try: return float(x)
    except: return None

# ── VALIDATION / TIEOUT ───────────────────────────────────────────────────────
assert len(rows)==25, f"expected 25 use cases, got {len(rows)}"
posture=Counter(r["posture"] for r in rows)
pattern=Counter(r["pattern"] for r in rows)
clusters=Counter(r["cluster"] for r in rows)
print("VALIDATION ── 25 use cases:", dict(clusters), "sum", sum(clusters.values()))
print("Posture mix:", dict(posture))
print("Pattern mix:", dict(pattern))
floors={r["use_case"]:fnum(r["ent_floor_k_usd"]) for r in rows if fnum(r["ent_floor_k_usd"])}
print("Enterprise floors known ($K/yr):", floors)
tams=[(r["use_case"],fnum(r["tam_2025_usd_b"])) for r in rows if fnum(r["tam_2025_usd_b"])]
print("TAM known (2025, $B):", {k:v for k,v in tams})

# ── CHART 1: posture mix ──────────────────────────────────────────────────────
fig,ax=plt.subplots(figsize=(7,4.2))
order=["BUILD","INTEGRATE","DEPLOY"]
labels={"BUILD":"BUILD\n(owned code)","INTEGRATE":"INTEGRATE+WORKFLOW\n(wire + own workflow)","DEPLOY":"DEPLOY+TUNE\n(stand up + tune)"}
vals=[posture.get(k,0) for k in order]
cols=[GOLD,TEAL,AMBER]
b=ax.bar([labels[k] for k in order],vals,color=cols,width=0.6)
for rect,v in zip(b,vals): ax.text(rect.get_x()+rect.get_width()/2,v+0.2,str(v),ha="center",fontweight="bold",color=INK)
ax.set_title("DataStaqAI delivery posture across 25 agentic use cases",fontweight="bold",color=NAVY)
ax.set_ylabel("# use cases"); ax.set_ylim(0,max(vals)+2); ax.spines[["top","right"]].set_visible(False)
ax.annotate("INTEGRATE+WORKFLOW dominates → the wedge is wiring agents\ninto systems of record, not building or reselling tools",
            xy=(0.5,0.86),xycoords="axes fraction",ha="center",fontsize=8,color=MUTED)
fig.tight_layout(); fig.savefig(os.path.join(HERE,"chart1_posture_mix.png")); plt.close(fig)

# ── CHART 2: mid-market price-floor gap ───────────────────────────────────────
fl=sorted(floors.items(),key=lambda x:x[1])
fig,ax=plt.subplots(figsize=(8.5,4.6))
ys=range(len(fl))
ax.barh(list(ys),[v for _,v in fl],color=NAVY,height=0.6)
for i,(k,v) in enumerate(fl):
    tag=f"${v:.0f}K/yr" if v>=1 else f"${v*1000:.0f}/yr"
    ax.text(v+4,i,tag,va="center",fontsize=8,color=INK)
ax.set_yticks(list(ys)); ax.set_yticklabels([k for k,_ in fl],fontsize=8)
ax.axvspan(24,60,color=TEAL,alpha=0.22)
ax.text(42,0.15,"DataStaqAI band\n$24–60K/yr",ha="center",va="bottom",fontsize=8,color="#00715e",fontweight="bold")
ax.set_xlabel("Enterprise entry floor ($K/year, where published)")
ax.set_title("The mid-market price-floor gap\nIncumbent floors start far above DataStaqAI's $2–5k/mo band",
             fontweight="bold",color=NAVY,fontsize=12,loc="left")
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(HERE,"chart2_price_floor_gap.png")); plt.close(fig)

# ── CHART 3: TAM by use case (where sourced), colored by cluster ──────────────
cc={"Customer":TEAL,"Employee":AMBER,"Creative":CORAL,"Code":GOLD,"Data":"#7FB3FF","Security":NAVY}
tr=[(r["use_case"],fnum(r["tam_2025_usd_b"]),r["cluster"]) for r in rows if fnum(r["tam_2025_usd_b"])]
tr.sort(key=lambda x:x[1])
fig,ax=plt.subplots(figsize=(8.5,4.8))
ax.barh([t[0] for t in tr],[t[1] for t in tr],color=[cc[t[2]] for t in tr],height=0.62)
for i,t in enumerate(tr): ax.text(t[1]+2,i,f"${t[1]:.0f}B",va="center",fontsize=8,color=INK)
ax.set_xlabel("Market size, 2025 ($B, sourced; not all use cases have a clean TAM)")
ax.set_title("Where the money is: sourced 2025 TAM by use case (color = cluster)",fontweight="bold",color=NAVY)
ax.spines[["top","right"]].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=cc[c],label=c) for c in cc],fontsize=7,loc="lower right",frameon=False)
fig.tight_layout(); fig.savefig(os.path.join(HERE,"chart3_tam_by_usecase.png")); plt.close(fig)

# ── CHART 4: opportunity map — density (judgment) vs pattern, sized by posture ─
dmap={"Low":1,"Med":2,"High":3}
fig,ax=plt.subplots(figsize=(8.5,4.8))
jit={"BUILD":-0.12,"INTEGRATE":0.0,"DEPLOY":0.12}
pcol={"REPLACE":CORAL,"RENEGOTIATE":AMBER,"KEEP":TEAL}
for r in rows:
    x=dmap.get(r["density"],2)+jit.get(r["posture"],0)
    y={"REPLACE":1,"RENEGOTIATE":2,"KEEP":3}[r["pattern"]]
    ax.scatter(x,y+ (0.12 if r["posture"]=="BUILD" else 0),s=120 if r["posture"]=="BUILD" else 60,
               color=pcol[r["pattern"]],edgecolor=NAVY if r["posture"]=="BUILD" else "none",linewidth=1.2,alpha=0.85,zorder=3)
ax.set_xticks([1,2,3]); ax.set_xticklabels(["Low density\n(open lane)","Medium","High density\n(crowded)"])
ax.set_yticks([1,2,3]); ax.set_yticklabels(["REPLACE","RENEGOTIATE","KEEP"])
ax.set_title("Opportunity map: competitive density (judgment) vs wedge pattern\n(ringed = BUILD plays — lowest density, owned-code outcome)",fontweight="bold",color=NAVY,fontsize=10)
ax.axvspan(0.5,1.5,color=TEAL,alpha=0.10)
ax.spines[["top","right"]].set_visible(False); ax.set_xlim(0.5,3.5); ax.set_ylim(0.5,3.7)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=pcol[p],label=p) for p in pcol],fontsize=7,loc="upper right",frameon=False)
fig.tight_layout(); fig.savefig(os.path.join(HERE,"chart4_opportunity_map.png")); plt.close(fig)

print("\nCHARTS written:", [f for f in os.listdir(HERE) if f.endswith('.png')])
