#!/usr/bin/env python3
"""Vendor-level analysis: funding concentration, valuation leaders, valuation-vs-ARR.
Source: vendors.csv (figures traced to COMPETITIVE_*.md). Blanks = not cleanly disclosed."""
import csv, os
from collections import defaultdict
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

H=os.path.dirname(os.path.abspath(__file__))
NAVY="#0A1628";TEAL="#00C9A7";GOLD="#FFB800";CORAL="#E05A6B";AMBER="#F2A83B";MUTED="#5B6B7C";INK="#1B2B3C"
cc={"Customer":TEAL,"Employee":AMBER,"Creative":CORAL,"Code":GOLD,"Data":"#7FB3FF","Security":NAVY}
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"figure.dpi":140})
def fn(x):
    try:return float(x)
    except:return None
rows=[r for r in csv.DictReader(open(os.path.join(H,"vendors.csv")))]
print("vendors:",len(rows))

# validation
raised_by_cluster=defaultdict(float); n_raised=defaultdict(int)
for r in rows:
    v=fn(r["total_raised_usd_m"])
    if v: raised_by_cluster[r["cluster"]]+=v; n_raised[r["cluster"]]+=1
print("disclosed raised by cluster ($M):",{k:round(v) for k,v in raised_by_cluster.items()})
print("vendors w/ valuation:",sum(1 for r in rows if fn(r["valuation_usd_b"])),
      "| w/ ARR:",sum(1 for r in rows if fn(r["arr_usd_m"])),
      "| w/ raised:",sum(1 for r in rows if fn(r["total_raised_usd_m"])))

# CHART 5: disclosed funding raised by cluster
order=sorted(raised_by_cluster,key=lambda k:-raised_by_cluster[k])
fig,ax=plt.subplots(figsize=(7.6,4.3))
bars=ax.bar(order,[raised_by_cluster[k] for k in order],color=[cc[k] for k in order],width=0.62)
for b,k in zip(bars,order):
    ax.text(b.get_x()+b.get_width()/2,b.get_height()+30,f"${raised_by_cluster[k]/1000:.2f}B\n({n_raised[k]} co.)",ha="center",fontsize=8,color=INK)
ax.set_title("Where VC has concentrated: disclosed funding raised by cluster",fontweight="bold",color=NAVY)
ax.set_ylabel("Sum of disclosed total raised ($M)"); ax.spines[["top","right"]].set_visible(False)
ax.annotate("Security + Customer are the most capitalized lanes →\ncompete on integration, not on out-raising the natives",
            xy=(0.97,0.84),xycoords="axes fraction",ha="right",fontsize=8,color=MUTED)
fig.tight_layout(); fig.savefig(os.path.join(H,"chart5_funding_by_cluster.png")); plt.close(fig)

# CHART 6: top valuations
vv=sorted([r for r in rows if fn(r["valuation_usd_b"])],key=lambda r:fn(r["valuation_usd_b"]))
fig,ax=plt.subplots(figsize=(8.6,5.4))
ax.barh([r["vendor"] for r in vv],[fn(r["valuation_usd_b"]) for r in vv],
        color=[(MUTED if r["type"]!="AI-native" else cc[r["cluster"]]) for r in vv],height=0.66)
for i,r in enumerate(vv): ax.text(fn(r["valuation_usd_b"])+0.3,i,f"${fn(r['valuation_usd_b']):.1f}B",va="center",fontsize=8,color=INK)
ax.set_xlabel("Valuation ($B, most recent disclosed)")
ax.set_title("Valuation leaders: the funded agent-natives DataStaqAI does NOT out-build\n(grey = incumbents; color = AI-native by cluster)",fontweight="bold",color=NAVY,fontsize=11,loc="left")
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(H,"chart6_valuation_leaders.png")); plt.close(fig)

# CHART 7: valuation vs ARR
both=[r for r in rows if fn(r["valuation_usd_b"]) and fn(r["arr_usd_m"])]
fig,ax=plt.subplots(figsize=(8.4,5.0))
for r in both:
    x=fn(r["valuation_usd_b"]); y=fn(r["arr_usd_m"])
    ax.scatter(x,y,s=90,color=cc[r["cluster"]],edgecolor=NAVY,linewidth=0.6,zorder=3,alpha=0.9)
    ax.annotate(r["vendor"],(x,y),xytext=(5,4),textcoords="offset points",fontsize=8,color=INK)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("Valuation ($B, log)"); ax.set_ylabel("ARR ($M, log)")
ax.set_title("Valuation vs ARR: the agent-natives carry rich revenue multiples\n(thin air above the line = the bubble DataStaqAI sells around, not into)",fontweight="bold",color=NAVY,fontsize=11,loc="left")
ax.grid(True,which="both",ls=":",color="#D9DFE5"); ax.spines[["top","right"]].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=cc[c],label=c) for c in cc if any(r['cluster']==c for r in both)],fontsize=7,loc="lower right",frameon=False)
fig.tight_layout(); fig.savefig(os.path.join(H,"chart7_valuation_vs_arr.png")); plt.close(fig)
print("charts:",[f for f in os.listdir(H) if f.startswith('chart5') or f.startswith('chart6') or f.startswith('chart7')])
