#!/usr/bin/env python3
"""PART VI — Path to $5–10M (slides 39–43). Illustrative financial model, labeled.
Generates ARR ramp chart, builds 5 slides + notes + spec. Validated on save."""
import sys
sys.path.insert(0,"/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
H=Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
NAVY="#0A1628";TEAL="#00C9A7";GOLD="#FFB800";AMBER="#F2A83B";MUTED="#5B6B7C";INK="#1B2B3C"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"figure.dpi":150})

# ── ARR ramp chart (illustrative) ──
yrs=["Year 1","Year 2","Year 3"]; rec=[0.4,1.8,5.5]; bld=[0.3,0.7,1.5]
fig,ax=plt.subplots(figsize=(6.3,4.6))
ax.bar(yrs,rec,color=TEAL,label="Recurring managed")
ax.bar(yrs,bld,bottom=rec,color=GOLD,label="Build projects")
for i,(r,bd) in enumerate(zip(rec,bld)):
    ax.text(i,r+bd+0.15,f"${r+bd:.1f}M",ha="center",fontweight="bold",color=INK)
ax.axhspan(5,10,color=MUTED,alpha=0.12)
ax.text(2.35,7.5,"$5–10M\ntarget",ha="center",fontsize=8,color=MUTED)
ax.set_ylabel("Revenue ($M, illustrative)"); ax.set_ylim(0,10.5)
ax.set_title("Illustrative ARR ramp to the $5–10M target",fontweight="bold",color=NAVY,loc="left")
ax.legend(fontsize=8,frameon=False,loc="upper left"); ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); fig.savefig(H/"chart_arr_ramp.png"); plt.close(fig)

d=Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 6: Path to $5–10M"); b=d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def band(s,y,txt,h=Inches(0.7),fill=None,col=None,size=13.5):
    d.rect(s,d.M,y,d.CW,h,fill or b.NAVY,radius=0.03)
    d.text(s,txt,d.M+Inches(0.25),y,d.CW-Inches(0.5),h,size=size,color=col or b.WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
def chips(s,items,y,w=Inches(2.25),gap=2.45,h=Inches(0.95),fill=None):
    for i,it in enumerate(items):
        x=Inches(0.6+gap*i)
        d.rect(s,x,y,w,h,fill or b.NAVY,radius=0.06)
        d.text(s,it,x+Inches(0.1),y,w-Inches(0.2),h,size=10.5,color=b.WHITE,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
        if i<len(items)-1: d.text(s,"→",Inches(0.6+gap*i+w.inches),y,Inches(0.2),h,size=18,color=b.TEAL,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
def card(s,x,y,w,h,title,lines,*,fill=None,tc=None,bc=None,tsize=13):
    fill=fill or b.SOFT;tc=tc or b.NAVY;bc=bc or b.INK
    d.rect(s,x,y,w,h,fill,radius=0.05,shadow=True); d.rect(s,x,y,Inches(0.1),h,b.TEAL)
    d.text(s,title,x+Inches(0.26),y+Inches(0.14),w-Inches(0.45),Inches(0.45),size=tsize,color=tc,bold=True,shrink=True)
    d.text(s,[{"text":t,"bullet":True,"space_before":5,"size":10.5,"color":bc} for t in lines],
           x+Inches(0.26),y+Inches(0.66),w-Inches(0.5),h-Inches(0.8),shrink=True,ls=1.05)

# 39 acquisition
s=d.slide(fill=b.WHITE)
d.header(s,"Acquisition is trigger-led outbound + proof-led referral — few logos needed because each compounds",
         "Hunt the signal, land a small pilot, turn it into a case study and a referral  (illustrative)")
chips(s,["Trigger signal","Targeted outbound","Pilot ($2–3k/mo)","Case study","Referral / expand"],Inches(1.9))
card(s,Inches(0.6),Inches(3.15),Inches(2.85),Inches(2.6),"CHANNELS",["Trigger monitoring (job posts, EOS, re-pricing)","Vertical referrals & communities","Partner / agent-vendor ecosystem","Founder-led + targeted content"])
card(s,Inches(3.63),Inches(3.15),Inches(2.85),Inches(2.6),"WHY IT'S EFFICIENT",["Triggered buyers are in-market (forced)","Small pilot = low approval friction","Proof, not promises, sells the next deal","Each win seeds referrals in the vertical"])
card(s,Inches(6.66),Inches(3.15),Inches(2.85),Inches(2.6),"CAC (illustrative)",["Founder-led: low cash CAC, high time","Target CAC payback < 6–9 months","Pilot converts to managed within 1–2 quarters","Referral CAC ≈ near-zero"],fill=b.NAVY,tc=b.TEAL,bc=b.LIGHT_TEAL)
card(s,Inches(9.69),Inches(3.15),Inches(3.0),Inches(2.6),"LOGOS NEEDED",["~40–50 accounts at ~$120k/yr → ~$5–7M","Expansion (NRR) cuts the new-logo count","High-trust BUILD wins punch above ACV"],fill=b.SOFT,tc=b.NAVY)
band(s,Inches(6.0),"The hunt from Chapter 4's signals is the acquisition engine: in-market buyers, low-friction pilots, proof-led "
     "referrals — a motion a small team can run.",h=Inches(0.95))
d.footer(s,39,46)
notes(s,("Open the path-to-scale chapter with acquisition, because the credibility of every later number depends on a "
 "believable way to win customers. The motion across the top is the funnel: a trigger signal, targeted outbound against "
 "it, a small pilot at $2–3k a month, a case study, and then referral and expansion. The key idea is that this reuses "
 "the hunt established in Chapter 4 — DataStaqAI does not need to generate demand from scratch; it monitors for "
 "in-market, forced buyers (a Salesforce CPQ End-of-Sale, a SOC-analyst job posting, a low-code re-pricing, a failed "
 "OCR rollout) and reaches them at the moment of pain. The four channels — trigger monitoring, vertical referrals and "
 "communities, the partner and agent-vendor ecosystem, and founder-led targeted content — are all low-cash, "
 "high-leverage for a small team. Why it is efficient: triggered buyers are already shopping, a small pilot clears "
 "approval without a committee, proof rather than promises sells the next deal, and each win seeds referrals within the "
 "same vertical, which compounds. On economics, be explicit that these are illustrative: founder-led selling means low "
 "cash CAC but real time cost; the target is CAC payback inside six to nine months, with pilots converting to managed "
 "retainers within a quarter or two and referral CAC approaching zero. The logos-needed callout is the slide's "
 "strategic punchline and the bridge to the rest of the chapter: roughly 40–50 accounts at about $120k a year gets you "
 "to $5–7M, and expansion (net revenue retention) reduces how many new logos you actually need, while high-trust BUILD "
 "wins punch above their headline ACV. The takeaway to land is that this is an acquisition motion a small, disciplined "
 "team can actually execute — not a venture-scale demand-gen machine — which is exactly right for a delivery business "
 "compounding toward $5–10M. Expansion, the real growth engine, is next."))

# 40 expansion
s=d.slide(fill=b.WHITE)
d.header(s,"Expansion is the growth engine: land one function, expand to 3–5, NRR > 130%",
         "A single account compounds from a $2–3k pilot to a $10–15k/mo multi-function program  (illustrative)")
steps=["Pilot: 1 function $2–3k/mo","+2nd function","+3rd function","Multi-function $10–15k/mo","+ BUILD project"]
chips(s,steps,Inches(2.0))
card(s,Inches(0.6),Inches(3.3),Inches(5.95),Inches(2.4),"WHY ACCOUNTS EXPAND",
     ["Trust from the first win + system access already in place","Same buyer owns adjacent broken workflows","Reusable library makes the 2nd–5th use case cheap to add","Switching cost rises as the agent embeds in the SoR"])
card(s,Inches(6.73),Inches(3.3),Inches(6.0),Inches(2.4),"THE MATH OF NRR (illustrative)",
     ["NRR > 130% means the base grows before new logos","A cohort can ~double in value over 24 months","Expansion revenue carries near-zero incremental CAC","Few logos + strong NRR = capital-efficient path to $5–10M"],fill=b.NAVY,tc=b.TEAL,bc=b.LIGHT_TEAL)
band(s,Inches(6.0),"Land-and-expand is why the logo count stays small: each account compounds 3–5x, so growth comes mostly from "
     "within the installed base.",h=Inches(0.95))
d.footer(s,40,46)
notes(s,("Expansion is the single most important mechanic in the path to $5–10M, so give it its own slide and make the "
 "compounding vivid. The step diagram shows one account's journey: a pilot on a single function at $2–3k a month, then "
 "a second function, a third, a multi-function program at $10–15k a month, and ultimately a BUILD project layered on "
 "top. Why accounts expand is structural, not hopeful: the first win creates trust and, just as importantly, the agent "
 "is already wired into the customer's systems, so the integration cost of the next use case is largely paid; the same "
 "buyer typically owns several adjacent broken workflows; the reusable library makes the second-through-fifth use case "
 "cheap to deliver; and switching cost rises as the agent embeds in the system of record, protecting the base. The math "
 "of net revenue retention is the strategic payoff: at NRR above 130%, the installed base grows in value before a single "
 "new logo is added, a cohort can roughly double over 24 months, and that expansion revenue carries near-zero "
 "incremental customer-acquisition cost because you are selling to an existing, happy buyer. Put the two together — few "
 "logos plus strong NRR — and you have a capital-efficient path to $5–10M that does not require a large sales "
 "organization. This is the answer to the skeptic who assumes a delivery business must grind out hundreds of logos: it "
 "does not, if each account compounds three-to-five-fold. Be explicit that the NRR figure and cohort doubling are "
 "illustrative targets, not promises, and that achieving them depends on delivery quality and the reusable library "
 "maturing as planned — which is exactly why the hiring and delivery model must be right, the subject of the next "
 "slide. The headline to leave in the room: growth comes mostly from within the installed base, which is the most "
 "capital-efficient growth there is."))

# 41 hiring
s=d.slide(fill=b.WHITE)
d.header(s,"Hire delivery pods, not an army — a senior core plus agent leverage covers many accounts",
         "Revenue per head rises as the reusable library matures  (illustrative)")
chips(s,["Founder / Principal","Delivery Pod","Delivery Pod","+ Pods as ARR grows"],Inches(1.95),w=Inches(2.6),gap=2.8)
card(s,Inches(0.6),Inches(3.2),Inches(5.95),Inches(2.5),"THE POD MODEL",
     ["Pod = 1–2 senior engineers + the agent/MCP library","Each pod runs several accounts (leverage, not 1:1)","Productized scope lets mid-level staff execute","Add a pod only when recurring ARR justifies it"])
card(s,Inches(6.73),Inches(3.2),Inches(6.0),Inches(2.5),"HEADCOUNT RAMP (illustrative)",
     ["Y1: founder + 2–3 (prove + first library)","Y2: ~6–10 (2–3 pods + GTM/ops)","Y3: ~15–25 to support $5–10M","Revenue/head trends up as reuse compounds"],fill=b.NAVY,tc=b.TEAL,bc=b.LIGHT_TEAL)
band(s,Inches(6.0),"Lean by design: the agent library is the force multiplier, so headcount grows slower than revenue — the "
     "opposite of a billable-hours SI.",h=Inches(0.95))
d.footer(s,41,46)
notes(s,("Hiring is where a delivery business either earns software-like economics or collapses into a body-shop, so the "
 "model must be explicit. The unit of scaling is the pod, not the individual: a pod is one or two senior engineers plus "
 "the shared agent and MCP library, and — this is the leverage point — each pod runs several accounts rather than one "
 "engineer per client. Productized scope (the three service lines from Chapter 5) lets mid-level staff execute against a "
 "known playbook instead of every senior reinventing each engagement, and a new pod is added only when recurring ARR "
 "justifies it, keeping hiring disciplined and demand-led. The illustrative headcount ramp shows the shape: Year 1 is "
 "the founder plus two or three people, focused as much on building the first reusable library as on delivery; Year 2 "
 "is roughly six to ten — two or three pods plus go-to-market and operations; Year 3 is roughly fifteen to twenty-five "
 "to support $5–10M in revenue. The critical metric is revenue per head trending upward over time, because the library "
 "compounds and each engagement gets cheaper to deliver — the exact opposite of a systems integrator whose revenue and "
 "headcount rise together. Make the contrast explicit in the band: lean by design, headcount grows slower than revenue, "
 "and the agent library is the force multiplier. Be honest, echoing the SWOT, that in the early years before the library "
 "is deep, the model is more labor-intensive and the revenue-per-head advantage is a trajectory being built, not an "
 "instant property — which is why disciplined productization and pod leverage are non-negotiable rather than nice to "
 "have. The numbers are illustrative and will flex with delivery efficiency and deal mix; the durable claim is the "
 "structure — pods over armies, reuse over rework, hire behind ARR. The economics slide quantifies what this leverage "
 "produces."))

# 42 economics (chart + unit econ)
s=d.slide(fill=b.WHITE)
d.header(s,"Unit economics: software-trending gross margin, fast payback, LTV/CAC that funds its own growth",
         "An illustrative model — the shape (recurring base + rising margin) is the point")
s.shapes.add_picture(str(H/"chart_arr_ramp.png"),d.M,Inches(1.8),width=Inches(6.3))
ue=[("GROSS MARGIN","~50–55% early → 65–70%+ as the reusable library matures"),
    ("CAC PAYBACK","< 6–9 months (trigger-led + founder/referral motion)"),
    ("LTV / CAC","> 4–5x, driven by NRR>130% and low churn (embedded in SoR)"),
    ("MIX","~70% recurring + ~30% build → durable, growing ARR")]
yy=1.85
for t,x in ue:
    d.rect(s,Inches(7.2),Inches(yy),Inches(5.5),Inches(1.05),b.SOFT,radius=0.05,shadow=True)
    d.rect(s,Inches(7.2),Inches(yy),Inches(0.1),Inches(1.05),b.TEAL)
    d.text(s,t,Inches(7.45),Inches(yy+0.12),Inches(5.1),Inches(0.35),size=12,color=b.ACCENT,bold=True)
    d.text(s,x,Inches(7.45),Inches(yy+0.5),Inches(5.1),Inches(0.5),size=11,color=b.INK,shrink=True,ls=1.05)
    yy+=1.16
band(s,Inches(6.55),"Assumptions (illustrative): ~$120k avg account/yr · NRR>130% · ~40–50 accounts · margin rising with library reuse.",h=Inches(0.5),size=12)
d.footer(s,42,46)
notes(s,("This slide quantifies what the model produces, and the framing must be disciplined: these are illustrative unit "
 "economics whose value is the shape, not the decimal places. The chart shows the ARR ramp — recurring managed revenue "
 "in teal stacking with build-project revenue in gold — climbing from under a million in Year 1 to roughly $2.5M in "
 "Year 2 and into the $5–10M target band by Year 3, with recurring becoming the dominant and compounding component. The "
 "unit economics on the right define the engine. Gross margin starts at a services-like 50–55% but trends toward "
 "software-like 65–70%-plus as the reusable library matures and each engagement requires less bespoke work — that "
 "upward margin trajectory is the whole bet. CAC payback under six-to-nine months reflects the trigger-led, "
 "founder-and-referral acquisition motion with low cash cost. LTV-to-CAC above four-to-five-times is driven by net "
 "revenue retention over 130% and low churn, because the agent is embedded in the system of record and expensive to "
 "rip out. And the roughly 70% recurring, 30% build mix gives durable, growing ARR rather than lumpy project revenue. "
 "State the assumptions plainly so the model is auditable: roughly $120k average account per year, NRR above 130%, "
 "around 40–50 accounts to reach the target, and margin rising with library reuse — and label every one of them "
 "illustrative, to be replaced with real cohort data. The strategic message is the investor one: this is a services "
 "business on a software trajectory — capital-efficient, recurring, margin-expanding — which is precisely the profile "
 "that can reach $5–10M without massive funding. The honest caveat to voice is that the margin expansion and NRR are "
 "earned through delivery discipline, not guaranteed by the model; the next slide lays out the execution roadmap that "
 "earns them phase by phase."))

# 43 roadmap
s=d.slide(fill=b.WHITE)
d.header(s,"Execution roadmap: prove → productize → expand → scale, in four phases to $5–10M",
         "Each phase has a single objective and a clear exit milestone  (illustrative)")
ph=[("PHASE 1 · 0–6 mo  PROVE",["Land first BUILD win + 2–3 pilots","Build the first reusable library","Exit: 3–5 reference logos"]),
    ("PHASE 2 · 6–12 mo  PRODUCTIZE",["Harden the 3 service lines + governance","Templatize top use cases","Exit: repeatable margins, ~$1M ARR"]),
    ("PHASE 3 · 12–24 mo  EXPAND",["Land-and-expand accounts (NRR>130%)","Add 2–3 delivery pods + GTM","Exit: ~$2.5–4M ARR"]),
    ("PHASE 4 · 24–36 mo  SCALE",["Vertical playbooks + partner channel","Scale pods behind ARR","Exit: $5–10M ARR"])]
xs=[Inches(0.6),Inches(3.63),Inches(6.66),Inches(9.69)]
for i,(x,(t,ls)) in enumerate(zip(xs,ph)):
    fill=b.NAVY if i==3 else b.SOFT
    d.rect(s,x,Inches(1.95),Inches(2.85),Inches(3.5),fill,radius=0.05,shadow=True)
    d.rect(s,x,Inches(1.95),Inches(2.85),Inches(0.5),b.TEAL if i<3 else b.GOLD,radius=0.05)
    d.text(s,t,x+Inches(0.15),Inches(1.95),Inches(2.55),Inches(0.5),size=10.5,color=b.NAVY,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    d.text(s,[{"text":q,"bullet":True,"space_before":7,"size":10.5,"color":b.LIGHT_TEAL if fill==b.NAVY else b.INK} for q in ls],
           x+Inches(0.2),Inches(2.6),Inches(2.5),Inches(2.7),shrink=True,ls=1.06)
    if i<3: d.text(s,"→",x+Inches(2.85),Inches(3.4),Inches(0.2),Inches(0.6),size=18,color=b.TEAL,bold=True,align=PP_ALIGN.CENTER)
band(s,Inches(5.7),"Prove delivery → productize for margin → expand the base → scale behind ARR. Disciplined, demand-led, and "
     "capital-efficient at every phase.",h=Inches(0.9))
d.footer(s,43,46)
notes(s,("Close the path-to-scale chapter with an execution roadmap that turns the model into a sequence anyone can hold "
 "accountable, each phase with one objective and a clear exit milestone. Phase 1, the first six months, is Prove: land "
 "the first BUILD win and two or three pilots, and — just as important — build the first reusable library; the exit "
 "milestone is three to five reference logos that make the next deals easier. Phase 2, months six to twelve, is "
 "Productize: harden the three service lines and the governance layer, templatize the top use cases, and reach "
 "repeatable margins at roughly $1M ARR; this is the phase that converts a consultancy into a scalable delivery firm. "
 "Phase 3, the second year, is Expand: drive land-and-expand across the installed base toward net revenue retention "
 "above 130%, add two or three delivery pods and a go-to-market function, and exit around $2.5–4M ARR. Phase 4, the "
 "third year, is Scale: codify vertical playbooks, open a partner channel, scale pods behind ARR, and reach the $5–10M "
 "target. The discipline to emphasize is that each phase is demand-led — you productize before you scale, you expand "
 "the base before you chase logos, and you add headcount behind recurring revenue, never ahead of it — which keeps the "
 "whole path capital-efficient. Note that the phases are illustrative and the timeline will flex with traction, but the "
 "ordering is deliberate and load-bearing: proving delivery must come before productizing, productizing before "
 "expanding, expanding before scaling. The sequence also de-risks the threats from the SWOT — by building the reusable "
 "library and embedding in systems of record early, the business raises switching costs and margin before larger "
 "competitors might push down-market. With acquisition, expansion, hiring, economics and roadmap established, the book "
 "has shown not just that the opportunity exists but that there is a credible, capital-efficient path to capture it. "
 "Chapter 7 closes with the investment thesis: why now, why DataStaqAI, and why this becomes a $5–10M company."))

out=H/"DataStaqAI-Book-Ch6-Path-to-5-10M.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)
defs=[("39","Acquisition — trigger-led outbound + proof-led referral","Funnel + channel/CAC/logos cards"),
      ("40","Expansion is the growth engine — NRR>130%","Land-and-expand step ramp"),
      ("41","Hire delivery pods, not an army","Pod model + headcount ramp"),
      ("42","Unit economics — software-trending margin, fast payback","ARR ramp chart + unit-econ cards"),
      ("43","Execution roadmap — prove → productize → expand → scale","4-phase timeline")]
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 6 — Path to $5–10M (Slides 39–43)\n","Illustrative financial model, labeled. Headline · viz · 300w notes.\n"]
for (n,hl,vz),t in zip(defs,nt):
    spec+=[f"\n## Slide {n} — {hl}\n",f"**Recommended visualization.** {vz}\n",f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter6-Path-to-5-10M.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter6-Path-to-5-10M.md")
