#!/usr/bin/env python3
"""PART IV-b — Competitive Analysis, slides 27–33 (completes the heart).
Generates 2 charts, builds 7 slides with notes + spec. Validated on save."""
import sys
sys.path.insert(0,"/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

H=Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
NAVY="#0A1628";TEAL="#00C9A7";GOLD="#FFB800";AMBER="#F2A83B";CORAL="#E05A6B";MUTED="#5B6B7C";INK="#1B2B3C";GREY="#C9D2DA"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"figure.dpi":150})

# ── chart: coverage heat map (archetype × function, MID-MARKET lens) ──
funcs=["Cust Ops","Sales","HR","Finance","Procure","Security","Legal","Analytics","Eng","Ops"]
arch=["Incumbent","AI-native","Managed/BPO","Global SI","Horizontal plat.","DataStaqAI"]
# 0 none · 1 partial · 2 strong  (mid-market coverage)
M=np.array([
 [1,1,1,1,1,1,1,1,1,1],   # incumbent: AI as add-on everywhere, weak for mid-market
 [1,1,0,1,0,1,1,1,1,0],   # AI-native: enterprise-first; mid-market thin
 [1,0,0,0,0,0,0,0,0,1],   # managed/BPO: pockets only
 [0,0,0,0,0,0,0,0,0,0],   # global SI: Global-2000 only, ~0 for mid-market
 [1,1,1,1,1,1,1,1,1,1],   # horizontal platform: DIY toolkit, partial everywhere
 [2,2,2,2,2,2,2,2,2,2],   # DataStaqAI: done-for-you across
])
fig,ax=plt.subplots(figsize=(8.6,3.9))
from matplotlib.colors import ListedColormap
cmap=ListedColormap(["#EEF2F5",AMBER,TEAL])
ax.imshow(M,cmap=cmap,vmin=0,vmax=2,aspect="auto")
ax.set_xticks(range(len(funcs))); ax.set_xticklabels(funcs,fontsize=9,rotation=30,ha="right")
ax.set_yticks(range(len(arch))); ax.set_yticklabels(arch,fontsize=9)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        lab={0:"–",1:"◐",2:"●"}[M[i,j]]
        ax.text(j,i,lab,ha="center",va="center",fontsize=9,color=(NAVY if M[i,j]==2 else MUTED))
ax.set_title("Mid-market coverage by archetype × function  (● strong · ◐ partial · – none)",fontweight="bold",color=NAVY,fontsize=11,loc="left")
for sp in ax.spines.values(): sp.set_visible(False)
ax.set_xticks(np.arange(-.5,len(funcs),1),minor=True); ax.set_yticks(np.arange(-.5,len(arch),1),minor=True)
ax.grid(which="minor",color="white",linewidth=2); ax.tick_params(which="minor",length=0)
fig.tight_layout(); fig.savefig(H/"chart_coverage.png"); plt.close(fig)

# ── chart: disruption matrix (2x2 bubble) ──
# x: competitive openness (1 crowded → 3 open) ; y: AI disruption readiness (1→3)
F=[("Engineering",3.0,3.0,27,GOLD),("HR",2.2,3.0,8,TEAL),("Finance",2.1,3.0,12,TEAL),
   ("Analytics",2.0,2.7,10,TEAL),("Procurement",2.2,2.5,9,TEAL),("Customer Ops",1.2,3.0,16,TEAL),
   ("Sales",1.6,2.9,12,TEAL),("Legal",1.2,2.9,9,TEAL),("Security",1.6,3.0,8,AMBER),("Operations",2.0,2.1,7,AMBER)]
fig,ax=plt.subplots(figsize=(8.6,5.0))
ax.axvspan(2.0,3.4,color=TEAL,alpha=0.08); ax.axhspan(2.6,3.4,color=TEAL,alpha=0.06)
for name,x,y,tam,c in F:
    ax.scatter(x,y,s=80+tam*16,color=c,edgecolor=NAVY,linewidth=0.8,alpha=0.85,zorder=3)
    ax.annotate(name,(x,y),xytext=(6,5),textcoords="offset points",fontsize=8.5,color=INK)
ax.set_xlim(0.7,3.4); ax.set_ylim(1.8,3.35)
ax.set_xticks([1,2,3]); ax.set_xticklabels(["Crowded\n(high competition)","","Open lane\n(low competition)"])
ax.set_yticks([2,2.5,3]); ax.set_yticklabels(["Lower","","High AI\ndisruption"])
ax.set_xlabel("Competitive openness →"); ax.set_ylabel("AI disruption readiness →")
ax.set_title("Disruption matrix: bubble = market size · color = DataStaqAI posture\nTop-right (open + disruptable) is where to lead — Engineering (BUILD) sits alone",fontweight="bold",color=NAVY,fontsize=11,loc="left")
for sp in ["top","right"]: ax.spines[sp].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=GOLD,label="BUILD"),Patch(color=TEAL,label="INTEGRATE"),Patch(color=AMBER,label="DEPLOY/KEEP")],fontsize=8,loc="lower left",frameon=False)
fig.tight_layout(); fig.savefig(H/"chart_disruption.png"); plt.close(fig)

# ── deck ──
d=Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 4: Competitive Analysis"); b=d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def band(s,y,txt,h=Inches(0.7),fill=None,col=None,size=13.5):
    d.rect(s,d.M,y,d.CW,h,fill or b.NAVY,radius=0.03)
    d.text(s,txt,d.M+Inches(0.25),y,d.CW-Inches(0.5),h,size=size,color=col or b.WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)

# 27 coverage heat map
s=d.slide(fill=b.WHITE)
d.header(s,"Map coverage by archetype × function and one row lights up — the mid-market is unserved",
         "Every existing archetype is partial-or-none for the mid-market; DataStaqAI is the only full row")
s.shapes.add_picture(str(H/"chart_coverage.png"),d.M,Inches(1.8),width=Inches(11.0))
band(s,Inches(6.1),"Incumbents add-on, AI-natives go enterprise, SIs ignore the middle, platforms are DIY. The done-for-you "
     "mid-market row is empty — until DataStaqAI fills it.",h=Inches(0.95))
d.footer(s,27,46)
notes(s,("This heat map is the single most efficient proof in the chapter: it shows, in one glance, that the mid-market is "
 "structurally unserved across every function. Read the rows as archetypes and the columns as the ten business "
 "functions, with each cell scored for how well that archetype serves a mid-market buyer in that function — solid means "
 "strong, half means partial, dash means none. The incumbent row is a uniform 'partial' because they bolt AI on as an "
 "add-on everywhere but re-architect nowhere. The AI-native row is a patchwork of partial-and-none because they go "
 "enterprise-first and skip the middle. The managed/BPO row lights up only in a couple of pockets like customer "
 "operations. The global-SI row is essentially all dashes for the mid-market, because they serve the Global 2000 by "
 "design. The horizontal-platform row is uniform 'partial' — a do-it-yourself toolkit that still leaves the buyer to "
 "deliver. And then the DataStaqAI row is the only one that is solid across the board, because done-for-you mid-market "
 "delivery is exactly the position the others vacate. The visual punch is intentional: the eye sees a cool, sparse grid "
 "with one hot row. Caution the audience that the scoring is judgment, not a measured index — but the pattern is robust "
 "and consistent with every prior slide's evidence. The strategic message is that DataStaqAI is not claiming to be "
 "better at any one function than the specialist who owns that column; it is claiming to be the only player serving the "
 "row — mid-market delivery — across all of them. That is a category position, not a feature race. The next slide names "
 "the specific white-space pockets this map implies and turns them into where-to-play priorities."))

# 28 white-space analysis
s=d.slide(fill=b.WHITE)
d.header(s,"The white space is four reinforcing pockets — and they compound into one defensible position",
         "Each pocket is a gap a funded competitor structurally won't fill")
ws=[("1 · Mid-market done-for-you","The empty 2x2 cell: too big for SMB tools, too small for AI-natives + SIs"),
    ("2 · The delivery layer","Integration + workflow + governance + operation — unowned below the Global 2000"),
    ("3 · Governed context","The semantic/evidence layer that makes agents accurate — the unglamorous real work"),
    ("4 · Owned-outcome BUILD plays","Legacy + low-code escape: owned code, lowest density, rivals Global-2000-only")]
xs=[Inches(0.6),Inches(6.73)]; ys=[Inches(1.95),Inches(4.0)]
for i,(t,x) in enumerate(ws):
    cx=xs[i%2]; cy=ys[i//2]
    d.rect(s,cx,cy,Inches(5.95),Inches(1.85),b.SOFT,radius=0.05,shadow=True)
    d.rect(s,cx,cy,Inches(0.12),Inches(1.85),b.TEAL)
    d.text(s,t,cx+Inches(0.3),cy+Inches(0.2),Inches(5.4),Inches(0.5),size=14,color=b.NAVY,bold=True,shrink=True)
    d.text(s,x,cx+Inches(0.3),cy+Inches(0.78),Inches(5.4),Inches(0.95),size=12,color=b.INK,shrink=True,ls=1.06)
band(s,Inches(6.1),"Alone each pocket is a niche. Together — mid-market + delivery + governed context + owned code — they are a "
     "category position no single competitor is built to occupy.",h=Inches(0.95))
d.footer(s,28,46)
notes(s,("Convert the heat map into a concrete white-space thesis by naming four pockets and, crucially, showing they "
 "reinforce one another. Pocket one is the mid-market done-for-you cell from the segmentation 2x2: companies too big for "
 "self-serve SMB tools and too small for the AI-natives and global SIs. Pocket two is the delivery layer itself — "
 "integration, workflow, governance and operation — which is unowned below the Global 2000. Pocket three is governed "
 "context: the semantic layer that makes text-to-SQL accurate, the source-grounded provenance that makes GRC evidence "
 "real — the unglamorous work that determines whether an agent actually functions, and which no product ships for the "
 "mid-market. Pocket four is the owned-outcome BUILD plays — legacy modernization and low-code escape — where the "
 "deliverable is code the client owns, competitive density is lowest, and the rivals are Global-2000-only. The strategic "
 "move on this slide is the synthesis in the band: any one of these pockets, alone, is a niche a competitor could "
 "eventually contest. But together they are mutually reinforcing and form a category position. Mid-market focus makes "
 "the delivery economics work; delivery requires governed context; governed context plus delivery is exactly what the "
 "BUILD plays need; and all of it is aimed at the segment the funded players concede. No single competitor is built to "
 "occupy all four at once — the incumbent won't do delivery, the AI-native won't do mid-market, the SI won't do the "
 "economics, the platform won't do the outcome. That compounding is the moat. The next slide turns these pockets into a "
 "ranked where-to-play scorecard so the strategy is actionable, not just defensible."))

# 29 where-to-play scorecard heat map
s=d.slide(fill=b.WHITE)
d.header(s,"Where to play: scored by pain, mid-market gap, competitive openness and our fit",
         "Engineering, Finance, HR and Analytics rank highest; scoring is judgment, not measured")
cols=["Function","Pain","Mid-mkt gap","Openness","Our fit","Priority"]
rows=[("Engineering","H","H","H","H","TOP"),("Finance","H","H","M","H","HIGH"),("HR","H","H","M","H","HIGH"),
      ("Analytics","H","H","M","H","HIGH"),("Procurement","M","H","M","M","HIGH"),("Security","H","M","L","M","MED"),
      ("Legal","H","H","L","M","MED"),("Customer Ops","H","M","L","M","MED"),("Sales","M","M","L","M","MED"),
      ("Operations","M","M","M","M","MED")]
cmapc={"H":b.TEAL,"M":b.AMBER,"L":b.GRID}
pcol={"TOP":b.GOLD,"HIGH":b.TEAL,"MED":b.GRID}
x0=Inches(0.6); cw=[Inches(2.4),Inches(1.5),Inches(2.0),Inches(1.7),Inches(1.5),Inches(1.6)]
def cx(j): return Inches(0.6+sum(c.inches for c in cw[:j]))
y=1.75; rh=0.42
for j,c in enumerate(cols):
    d.rect(s,cx(j),Inches(y),cw[j],Inches(rh),b.NAVY)
    d.text(s,c,cx(j),Inches(y),cw[j],Inches(rh),size=10.5,color=b.WHITE,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
for r in rows:
    y+=rh
    d.rect(s,cx(0),Inches(y),cw[0],Inches(rh),b.SOFT)
    d.text(s,r[0],cx(0)+Inches(0.1),Inches(y),cw[0]-Inches(0.2),Inches(rh),size=10.5,color=b.INK,bold=True,anchor=MSO_ANCHOR.MIDDLE,align=PP_ALIGN.LEFT,shrink=True)
    for j in range(1,5):
        v=r[j]; d.rect(s,cx(j),Inches(y),cw[j],Inches(rh),cmapc[v])
        d.text(s,v,cx(j),Inches(y),cw[j],Inches(rh),size=10.5,color=b.NAVY if v!="L" else b.MUTED,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    d.rect(s,cx(5),Inches(y),cw[5],Inches(rh),pcol[r[5]])
    d.text(s,r[5],cx(5),Inches(y),cw[5],Inches(rh),size=10,color=b.NAVY,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
band(s,Inches(6.55),"Lead with Engineering (BUILD) → land Finance/HR/Analytics (INTEGRATE) → attach Security/Ops (DEPLOY).",h=Inches(0.5),size=12.5)
d.footer(s,29,46)
notes(s,("This is the chapter's actionable centerpiece: a where-to-play scorecard that ranks the ten functions on four "
 "factors and assigns a priority. The factors are pain intensity (how acute the problem is), mid-market gap (how "
 "unserved the middle is), competitive openness (inverse of how crowded the lane is), and our fit (how well DataStaqAI's "
 "model maps to the work). Cells are colored high-teal, medium-amber, low-grey, and the priority pill on the right "
 "synthesizes them. Engineering scores high on all four and earns the TOP priority, because it is the one BUILD play — "
 "low competitive density, owned-code outcome, acute pain, perfect fit. Finance, HR and Analytics come next at HIGH: "
 "severe pain, a wide mid-market gap, reasonable openness, and strong INTEGRATE fit. Procurement also rates HIGH on the "
 "strength of its mid-market gap. Security, Legal, Customer Ops and Sales rate MEDIUM — not because the pain is small "
 "(it is often acute) but because the lanes are crowded with funded natives, so they are land-on-signal rather than "
 "lead-with plays. Operations is MEDIUM as a KEEP/enrichment lane. Be explicit that this scoring is judgment derived "
 "from the research, labeled as such, not a measured index — that honesty is what makes it credible to a skeptical "
 "buyer or investor. The sequencing instruction in the band is the takeaway: lead with Engineering to establish "
 "delivery credibility you can't buy, land Finance, HR and Analytics for volume, and attach Security and Operations as "
 "fast deploy-and-tune wins. The next three slides stress-test this with a SWOT, a disruption matrix, and the explicit "
 "reasons competitors stop short, before the chapter closes on why DataStaqAI wins."))

# 30 SWOT
s=d.slide(fill=b.WHITE)
d.header(s,"SWOT: the strengths and opportunities are structural; the risks are real and managed",
         "An honest read — the threats are why focus and speed matter")
def q(cx,cy,t,lines,fill,tc):
    d.rect(s,cx,cy,Inches(5.95),Inches(2.15),fill,radius=0.05,shadow=True)
    d.text(s,t,cx+Inches(0.2),cy+Inches(0.14),Inches(5.5),Inches(0.4),size=13.5,color=tc,bold=True)
    d.text(s,[{"text":x,"bullet":True,"space_before":4,"size":11,"color":b.INK if fill!=b.NAVY else b.LIGHT_TEAL} for x in lines],
           cx+Inches(0.2),cy+Inches(0.62),Inches(5.5),Inches(1.45),shrink=True,ls=1.04)
q(Inches(0.6),Inches(1.95),"STRENGTHS",["Engineering economics: agents+subagents+MCPs at ~$2–5k/mo","Owns the outcome (and the code, in BUILD plays)","Integration + governance depth; aligned with the SoR"],b.SOFT,b.ACCENT)
q(Inches(6.73),Inches(1.95),"WEAKNESSES",["Delivery capacity scales with team (services flavor)","Brand/trust vs Accenture-class SIs is nascent","Depends on third-party agents (supply risk)"],b.SOFT,b.CORAL)
q(Inches(0.6),Inches(4.2),"OPPORTUNITIES",["The empty mid-market done-for-you cell","Incumbent-forced migrations (CPQ EOS) + AI-natives conceding via managed tiers","80% of orgs can't self-automate (integration+skills)"],b.NAVY,b.TEAL)
q(Inches(6.73),Inches(4.2),"THREATS",["AI-natives / SIs pushing down-market over time","Incumbents bundling 'good enough' agents","Price floors collapsing → margin pressure"],b.SOFT,b.AMBER)
d.footer(s,30,46)
notes(s,("Give an honest SWOT, because a deck that only lists strengths loses a sophisticated audience. The strengths are "
 "structural: engineering economics — agents, subagents and thousands of MCP integrations delivered at roughly "
 "$2–5k/month, which is a fundamentally different cost base than an SI's billable teams or an AI-native's white-glove "
 "services; ownership of the outcome, and in the BUILD plays the actual code; and depth in integration and governance "
 "while being aligned with, not opposed to, the systems of record. The weaknesses are equally real and worth naming "
 "first to build trust: delivery capacity scales with the team, giving the model a services flavor that must be "
 "engineered down with reusable agents and templates; brand and trust against Accenture-class incumbents is nascent and "
 "must be earned deal by deal; and reliance on third-party agents introduces supply risk if a key vendor changes terms. "
 "The opportunities restate the thesis as external forces: the empty mid-market done-for-you cell, incumbent-forced "
 "migrations like Salesforce CPQ's End-of-Sale, AI-natives conceding the gap through managed tiers, and the survey "
 "finding that ~80% of organizations cannot fully automate because of integration and skills gaps. The threats are the "
 "honest risks that justify urgency: AI-natives and SIs could push down-market over time, incumbents could bundle "
 "'good enough' agents into existing contracts, and collapsing price floors could pressure margins. The strategic "
 "conclusion to deliver is that the strengths and opportunities are structural and durable while the threats are "
 "time-based — which is precisely why focus (lead with the BUILD plays) and speed (land the mid-market while the window "
 "is open) are the right responses. The disruption matrix on the next slide visualizes where that focus should go."))

# 31 disruption matrix
s=d.slide(fill=b.WHITE)
d.header(s,"Disruption matrix: lead where high disruptability meets an open lane",
         "Engineering sits alone in the top-right; the crowded REPLACE lanes are land-on-signal")
s.shapes.add_picture(str(H/"chart_disruption.png"),d.M,Inches(1.8),width=Inches(8.6))
pts=[("TOP-RIGHT = LEAD","Open + disruptable: Engineering (BUILD), Finance/HR/Procurement (INTEGRATE)"),
     ("TOP-LEFT = LAND ON SIGNAL","Disruptable but crowded: Customer Ops, Legal, Sales, Security"),
     ("BUBBLE = MARKET SIZE","Big markets aren't always the open ones — pick openness over size")]
yy=2.0
for t,x in pts:
    d.rect(s,Inches(9.35),Inches(yy),Inches(3.35),Inches(1.45),b.SOFT,radius=0.05,shadow=True)
    d.text(s,t,Inches(9.5),Inches(yy+0.12),Inches(3.05),Inches(0.35),size=11,color=b.ACCENT,bold=True,shrink=True)
    d.text(s,x,Inches(9.5),Inches(yy+0.5),Inches(3.05),Inches(0.85),size=10.5,color=b.INK,shrink=True,ls=1.05)
    yy+=1.55
d.footer(s,31,46)
notes(s,("The disruption matrix turns the where-to-play logic into a picture an executive can hold in memory. The "
 "horizontal axis is competitive openness, from crowded on the left to open lane on the right; the vertical axis is AI "
 "disruption readiness, from lower at the bottom to high at the top; each bubble is a function, sized by market size and "
 "colored by DataStaqAI posture — gold for BUILD, teal for INTEGRATE, amber for DEPLOY/KEEP. The shaded top-right "
 "quadrant is where to lead: high disruptability meeting low competition. Engineering sits there essentially alone, "
 "which is the visual restatement of why it is the TOP priority — a highly disruptable, owned-code opportunity in an "
 "open lane. Finance, HR, Procurement and Analytics cluster just inside the lead zone as strong INTEGRATE plays. The "
 "top-left holds the lanes that are highly disruptable but crowded with funded natives — Customer Ops, Legal, Sales, "
 "and Security — which is why they are land-on-signal rather than lead-with: enter when a specific buyer signal appears "
 "(a CPQ End-of-Sale, a SOC-analyst job posting, a legal 'which-tools' review) and win on integration and price rather "
 "than trying to out-build the category leader. The most important interpretive point, captured in the right-hand "
 "callouts, is that bubble size and openness are not correlated — the biggest markets (Customer Ops, Finance) are often "
 "the more crowded ones, so the discipline is to prioritize openness over raw size, because an open lane with engineering "
 "economics beats a giant crowded lane where you would be the sixth-best agent. This matrix and the scorecard agree, "
 "which is the point: two independent views converge on the same sequence. The final two slides explain why the "
 "competitors can't simply follow us into these lanes, and then synthesize why DataStaqAI wins."))

# 32 why competitors stop short
s=d.slide(fill=b.WHITE)
d.header(s,"Why competitors stop short — each is structurally, not temporarily, blocked from the cell",
         "These are business-model constraints; a roadmap update won't fix them")
reasons=[("Incumbents","Seat revenue makes self-disruption irrational → AI stays an add-on"),
         ("AI-natives","Venture economics demand enterprise ACVs → mid-market is uneconomic to serve directly"),
         ("Managed / BPO","Labor-cost scaling caps margin → can't reach engineering economics"),
         ("Global SIs","Cost base + sales motion built for $1M+ Global-2000 deals"),
         ("Horizontal platforms","Sell tools, not outcomes → the delivery is still the buyer's problem")]
y=1.95
for t,x in reasons:
    d.rect(s,d.M,Inches(y),d.CW,Inches(0.82),b.SOFT,radius=0.04,shadow=True)
    d.rect(s,d.M,Inches(y),Inches(2.6),Inches(0.82),b.NAVY,radius=0.04)
    d.text(s,t,d.M+Inches(0.18),Inches(y),Inches(2.3),Inches(0.82),size=13,color=b.TEAL,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    d.text(s,x,d.M+Inches(2.85),Inches(y),Inches(9.0),Inches(0.82),size=12.5,color=b.INK,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    y+=0.92
band(s,Inches(6.55),"Every barrier is a business-model constraint, not a capability gap — which is why the cell stays open.",h=Inches(0.5),size=12.5)
d.footer(s,32,46)
notes(s,("This slide answers the killer investor question — 'if this is such a good opportunity, why won't the well-funded "
 "competitors just take it?' — by showing that each is blocked by a business-model constraint, not a capability gap, "
 "which is the difference between a defensible position and a temporary head start. Incumbents are blocked because their "
 "revenue is the seat; self-disruption is irrational, so their AI stays an add-on no matter how good the technology "
 "gets. AI-natives are blocked because venture-scale economics demand large enterprise ACVs and winner-take-most "
 "capture; serving a mid-market company directly, with its messy systems and modest budget, is uneconomic for a company "
 "priced at fifteen billion dollars — so they hand it to partners or skip it. Managed and BPO players are blocked "
 "because their costs scale with labor, capping margins below what engineering economics achieve, so they cannot match "
 "DataStaqAI's price-for-outcome at scale. Global SIs are blocked because their cost base and sales motion are built for "
 "million-dollar Global-2000 transformation deals; a $2–5k/month mid-market engagement is below their floor. And "
 "horizontal platforms are blocked because they sell tools, not outcomes, so the delivery — the hard part — remains the "
 "buyer's problem. The unifying point, and the reason this is a durable thesis rather than a race, is that none of these "
 "barriers is fixed by a roadmap update or a price cut; each is woven into how the competitor makes money. That is what "
 "keeps the mid-market delivery cell open long enough for DataStaqAI to own it. The final slide of the chapter "
 "synthesizes the whole argument into why DataStaqAI wins."))

# 33 why DataStaqAI wins
s=d.slide(fill=b.NAVY)
d.rect(s,0,0,d.W,Inches(0.16),b.TEAL)
d.text(s,"Why DataStaqAI wins",d.M,Inches(0.5),d.CW,Inches(0.7),size=28,color=b.WHITE,bold=True)
d.rect(s,d.M,Inches(1.28),Inches(1.45),Inches(0.05),b.TEAL)
pill=[("Owns the empty cell","The only done-for-you player built for the mid-market — a category position, not a feature"),
      ("Engineering economics","Agents+subagents+MCPs at ~$2–5k/mo undercut SIs on cost and AI-natives on price"),
      ("Rides, doesn't fight","Wires best-of-breed agents into the SoR — never out-builds the funded natives or wrappers the model eats"),
      ("Owned outcomes + governed context","Delivers resolved tickets, owned code, audit-ready evidence — the layer competitors underfund")]
xs=[d.M,Inches(6.73)]; ys=[Inches(1.6),Inches(3.95)]
for i,(t,x) in enumerate(pill):
    cx=xs[i%2]; cy=ys[i//2]
    d.rect(s,cx,cy,Inches(5.95),Inches(2.05),b.NAVY_2,radius=0.05,shadow=True)
    d.rect(s,cx,cy,Inches(0.12),Inches(2.05),b.TEAL)
    d.text(s,t,cx+Inches(0.3),cy+Inches(0.2),Inches(5.4),Inches(0.5),size=15,color=b.GOLD,bold=True,shrink=True)
    d.text(s,x,cx+Inches(0.3),cy+Inches(0.85),Inches(5.4),Inches(1.05),size=12.5,color=b.LIGHT_TEAL,shrink=True,ls=1.06)
d.text(s,"The competition optimized the model and the agent. DataStaqAI owns the delivery layer the mid-market can't buy "
         "anywhere else.",d.M,Inches(6.25),d.CW,Inches(0.8),size=14.5,color=b.WHITE,bold=True,shrink=True)
d.footer(s,33,46,dark=True)
notes(s,("Close the competitive chapter by synthesizing everything into four reasons DataStaqAI wins, stated as a position "
 "rather than a boast. First, it owns the empty cell: it is the only done-for-you player built for the mid-market, which "
 "is a category position — a place on the map — not a feature that can be copied. Second, engineering economics: "
 "delivering with agents, subagents and thousands of MCP integrations at roughly $2–5k/month undercuts the systems "
 "integrators on cost and the AI-natives on price simultaneously, a combination neither can match because of their own "
 "structures. Third, it rides rather than fights: by wiring best-of-breed agents into the customer's systems of record, "
 "it never has to out-build the funded natives or bet on a wrapper that the next model release will eat — it benefits "
 "from their R&D instead of competing with it. Fourth, it delivers owned outcomes and governed context: resolved "
 "tickets, owned code, audit-ready evidence, built on the semantic and provenance layer that the competitors underfund "
 "because it has services-like economics they avoid. Tie it together with the closing line — the competition optimized "
 "the model and the agent; DataStaqAI owns the delivery layer the mid-market cannot buy anywhere else. Remind the "
 "audience that this conclusion is earned, not asserted: the heat map showed the empty row, the segmentation showed the "
 "empty cell, the archetype analysis showed why each competitor vacates it, the scorecard and disruption matrix showed "
 "where to lead, and the stop-short slide showed the barriers are structural. That is the case the rest of the book now "
 "operationalizes — the business model in Chapter 5, the path to $5–10M in Chapter 6, and the investment thesis in "
 "Chapter 7."))

out=H/"DataStaqAI-Book-Ch4b-Competitive-B.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)
defs=[("27","Coverage heat map — the mid-market row is the only one that lights up","Archetype×function heat map"),
      ("28","White space is four reinforcing pockets → one category position","4 white-space cards"),
      ("29","Where to play — scored by pain, gap, openness, fit","Scorecard heat map (10×4 + priority)"),
      ("30","SWOT — strengths/opportunities structural; threats time-based","4-quadrant SWOT"),
      ("31","Disruption matrix — lead where disruptability meets an open lane","2x2 bubble chart"),
      ("32","Why competitors stop short — business-model constraints, not capability","Reason rows by archetype"),
      ("33","Why DataStaqAI wins — owns the delivery layer for the mid-market","4 pillar cards (navy)")]
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 4 (b) — Competitive Analysis, Slides 27–33\n","Diagram-forward; headline · viz · 300w notes. Scoring labeled as judgment.\n"]
for (n,hl,vz),t in zip(defs,nt):
    spec+=[f"\n## Slide {n} — {hl}\n",f"**Recommended visualization.** {vz}\n",f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter4b-Competitive.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter4b-Competitive.md")
