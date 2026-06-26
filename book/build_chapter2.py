#!/usr/bin/env python3
"""PART II — The AI Transformation (slides 4–8). Diagram-forward, minimal text.
Renders branded .pptx with speaker notes + companion markdown spec. Validated on save."""
import sys, os
sys.path.insert(0, "/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

H = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
NAVY="#0A1628";TEAL="#00C9A7";GOLD="#FFB800";MUTED="#5B6B7C";INK="#1B2B3C"

# ── CAGR chart for slide 8 (sourced) ──────────────────────────────────────────
data=[("Autonomous SOC",24.77),("AI Customer Support",23.14),("AI Code Review",20.2),
      ("Digital Asset Mgmt",16.2),("Fraud Detection",15.5),("Low-code",14.0),
      ("Creative DCO",11.5),("Mainframe Modernization",9.8)]
data.sort(key=lambda x:x[1])
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"figure.dpi":150})
fig,ax=plt.subplots(figsize=(6.4,4.8))
cols=[TEAL if v>=15 else MUTED for _,v in data]
ax.barh([k for k,_ in data],[v for _,v in data],color=cols,height=0.66)
for i,(k,v) in enumerate(data): ax.text(v+0.3,i,f"{v:.1f}%",va="center",fontsize=9,color=INK,fontweight="bold")
ax.set_xlabel("Market CAGR (%, sourced analyst sizings)")
ax.set_title("Agentic sub-markets are compounding 10–25%/yr",fontweight="bold",color=NAVY,loc="left")
ax.spines[["top","right"]].set_visible(False); ax.set_xlim(0,28)
fig.tight_layout(); fig.savefig(H/"chart_cagr.png"); plt.close(fig)

# ── deck ──────────────────────────────────────────────────────────────────────
d = Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 2: The AI Transformation")
b = d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def cell(s,x,y,w,h,txt,*,fill,col,bold=False,size=12,align=PP_ALIGN.CENTER):
    d.rect(s,x,y,w,h,fill)
    d.text(s,txt,x+Inches(0.1),y,w-Inches(0.2),h,size=size,color=col,bold=bold,align=align,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
def panel(s,x,y,w,h,title,lines,*,fill,tcol,bcol,tsize=14):
    d.rect(s,x,y,w,h,fill,radius=0.05,shadow=True)
    d.text(s,title,x+Inches(0.18),y+Inches(0.16),w-Inches(0.36),Inches(0.7),size=tsize,color=tcol,bold=True,shrink=True)
    d.text(s,[{"text":t,"bullet":True,"space_before":5,"size":11,"color":bcol} for t in lines],
           x+Inches(0.18),y+Inches(0.92),w-Inches(0.36),h-Inches(1.05),shrink=True,ls=1.05)
XS=[Inches(0.6),Inches(3.63),Inches(6.66),Inches(9.69)]; PW=Inches(2.85)
def arrows(s,y):
    for cx in (Inches(3.48),Inches(6.51),Inches(9.54)):
        d.text(s,"→",cx,y,Inches(0.3),Inches(0.5),size=26,color=b.TEAL,bold=True,align=PP_ALIGN.CENTER)

# SLIDE 4 — Evolution of Enterprise Software
s=d.slide(fill=b.WHITE)
d.header(s,"Enterprise software re-platforms every ~15 years — each wave moved intelligence closer to the work",
         "Agents are the fourth wave: the first to move intelligence past the human at the seat")
eras=[("1970s–90s · Mainframe / ERP",["Centralized records, IT-operated","Unit of value: the batch job"],b.SOFT,b.INK),
      ("1990s–2010s · Client-server → SaaS",["Per-seat apps; humans operate tools","Unit of value: the seat"],b.SOFT,b.INK),
      ("2010s–20s · Cloud / Mobile / API",["Access everywhere; integration sprawl","Unit of value: the API call"],b.SOFT,b.INK),
      ("2024+ · Agentic",["Agents operate the tools; outcome-billed","Unit of value: the agent run"],b.NAVY,b.WHITE)]
for x,(t,ls,fl,tc) in zip(XS,eras):
    panel(s,x,Inches(2.05),PW,Inches(3.0),t,ls,fill=fl,tcol=(b.TEAL if fl==b.NAVY else b.NAVY),bcol=tc,tsize=12.5)
arrows(s,Inches(3.4))
d.rect(s,d.M,Inches(5.45),d.CW,Inches(1.1),b.GOLD,radius=0.03)
d.text(s,"Each wave moved intelligence closer to the work. The agentic wave moves it PAST the human entirely — "
         "and resets who captures the budget the seat used to hold.",d.M+Inches(0.25),Inches(5.6),d.CW-Inches(0.5),Inches(0.85),
       size=14.5,color=b.NAVY,bold=True,shrink=True)
d.footer(s,4,8)
notes(s,("Open Chapter 2 by giving the audience a frame for change they already intuit: enterprise software re-platforms "
 "roughly every fifteen years, and each wave has moved intelligence one step closer to the actual work. The mainframe/ERP "
 "era centralized the record but kept intelligence in the IT department running batch jobs. The client-server and SaaS era "
 "put applications on every desk and made the seat the unit of value — but the intelligence still lived in the human "
 "operating the tool. The cloud/mobile/API era made everything accessible everywhere and turned integration into the "
 "dominant cost, but it did not change who did the thinking. The point of walking these three is to make the fourth feel "
 "inevitable rather than hyped. The agentic wave is categorically different from the first three because, for the first "
 "time, the intelligence moves past the human at the seat: the agent operates the tools itself, and value is billed per "
 "outcome rather than per seat. Stress the throughline — each wave moved intelligence closer to the work, and this one "
 "moves it through the human entirely. That is why it resets the budget: when the seat is no longer where the work happens, "
 "the spend that funded seats is in play. Close by setting up the rest of the chapter: if this is a genuine platform wave, "
 "we should expect to see it in the capability curve of AI itself (slide 5), in the limits of half-measures like copilots "
 "(slide 6), in a specific unsolved layer (slide 7), and in market data showing the inflection is now (slide 8). Keep the "
 "delivery deliberately calm and historical — you are earning the right to the sharper claims that follow by grounding them "
 "in a pattern the audience has lived through twice already."))

# SLIDE 5 — Evolution of AI (capability staircase)
s=d.slide(fill=b.WHITE)
d.header(s,"AI crossed from 'predict' to 'do' — and that jump makes orchestration, not the model, the scarce layer",
         "Each step added capability; the last step changes who performs the work")
steps=[("Rules / RPA",["If-this-then-that","Brittle; breaks on change"],4.5,b.SOFT,b.INK),
       ("ML / Predictive",["Forecasts & scores","Needs clean labeled data"],3.8,b.SOFT,b.INK),
       ("Generative / Copilot",["Drafts & suggests","Human stays in the loop"],3.1,b.SOFT,b.INK),
       ("Agentic / Autonomous",["Reasons, decides, ACTS","Owns the outcome"],2.4,b.NAVY,b.WHITE)]
for x,(t,ls,top,fl,tc) in zip(XS,steps):
    h=6.3-top
    d.rect(s,x,Inches(top),PW,Inches(h),fl,radius=0.05,shadow=True)
    d.text(s,t,x+Inches(0.18),Inches(top)+Inches(0.16),PW-Inches(0.36),Inches(0.7),size=13,
           color=(b.TEAL if fl==b.NAVY else b.NAVY),bold=True,shrink=True)
    d.text(s,[{"text":q,"bullet":True,"space_before":5,"size":11,"color":tc} for q in ls],
           x+Inches(0.18),Inches(top)+Inches(0.86),PW-Inches(0.36),Inches(h-1.0),shrink=True,ls=1.05)
d.text(s,"The jump from PREDICT to DO is the value inflection: once the agent acts across systems, the model becomes a "
         "commodity input and orchestration becomes the scarce, defensible layer.",d.M,Inches(6.45),d.CW,Inches(0.7),
       size=13.5,color=b.NAVY,bold=True,shrink=True)
d.footer(s,5,8)
notes(s,("This slide reframes 'AI progress' as a capability staircase so the audience sees that the recent jump is "
 "qualitatively different, not just bigger. Step one, rules and RPA: deterministic if-this-then-that automation that is "
 "powerful but brittle and breaks the moment the environment changes. Step two, machine learning: forecasts and scores, a "
 "real leap, but dependent on clean labeled data and still only predicting, not acting. Step three, generative AI and "
 "copilots: the system can now draft and suggest in natural language, which felt revolutionary, but the human stays firmly "
 "in the loop and must accept, edit, and execute. Step four, agentic: the system reasons over context, decides the next "
 "step, acts across systems, and owns the outcome. The crucial teaching point is that the first three steps all kept the "
 "human as the actor; only the fourth makes the software the actor. That is why the jump from 'predict' to 'do' is the "
 "value inflection of the entire field. Now connect it to strategy, because this is where Chapter 2 starts doing real work "
 "for DataStaqAI: once agents can act, the foundation model becomes a commodity input — interchangeable, rapidly cheapening, "
 "and as we will show, unable to function reliably without governed context. What becomes scarce and defensible is the "
 "orchestration: wiring the agent into the real systems, giving it the governed context it needs, constraining it with "
 "policy, and operating it. Preview the proof that the model is not the moat, which lands harder in slide 7: on realistic "
 "enterprise data, frontier text-to-SQL accuracy collapses from ~87% on toy schemas to ~10%, and the accuracy that "
 "production systems do achieve comes from the semantic layer, not the raw model. End on the strategic inversion: the part "
 "everyone is racing to build — the model — is the part that commoditizes; the part almost no one is building — delivery — "
 "is the part that compounds."))

# SLIDE 6 — Why Copilots Aren't Enough (matrix)
s=d.slide(fill=b.WHITE)
d.header(s,"Copilots assist the human at the seat — they don't remove it, so they cap out at suggestion not resolution",
         "The capability gap between a copilot and an agent is the gap between faster work and no work")
lx,cx,ax_=d.M,Inches(5.7),Inches(9.18); lw,cw,aw=Inches(5.0),Inches(3.4),Inches(3.55)
y0=Inches(1.8); rh=Inches(0.6)
cell(s,lx,y0,lw,rh,"Capability",fill=b.NAVY,col=b.WHITE,bold=True,align=PP_ALIGN.LEFT,size=12)
cell(s,cx,y0,cw,rh,"Copilot (assists the seat)",fill=b.NAVY,col=b.WHITE,bold=True,size=12)
cell(s,ax_,y0,aw,rh,"Agent (replaces the seat)",fill=b.NAVY,col=b.TEAL,bold=True,size=12)
rows=[("Triggers itself on an event","No — human invokes","Yes"),
      ("Decides the next step","Suggests","Decides & executes"),
      ("Acts across systems of record","No","Yes"),
      ("Owns the outcome end-to-end","No","Yes"),
      ("Billing unit","Per seat","Per outcome")]
for i,(lab,cp,ag) in enumerate(rows):
    yy=Inches(2.42+0.6*i); alt=b.SOFT if i%2==0 else b.WHITE
    cell(s,lx,yy,lw,rh,lab,fill=alt,col=b.INK,align=PP_ALIGN.LEFT,size=11.5)
    cell(s,cx,yy,cw,rh,cp,fill=b.SOFT,col=b.CORAL,bold=True,size=11.5)
    cell(s,ax_,yy,aw,rh,ag,fill=b.LIGHT_TEAL,col=b.ACCENT,bold=True,size=11.5)
d.rect(s,d.M,Inches(5.55),d.CW,Inches(0.85),b.NAVY,radius=0.03)
d.text(s,"In the field: agent-assist tools are used ~1% of the time · AI code review reads as 'mostly noise' · the copilot "
         "adds a tab, it doesn't remove the work.",d.M+Inches(0.25),Inches(5.68),d.CW-Inches(0.5),Inches(0.6),
       size=12.5,color=b.LIGHT_TEAL,shrink=True)
d.text(s,"A copilot makes the seat faster. An agent makes the seat unnecessary — and only delivery makes the agent real.",
       d.M,Inches(6.55),d.CW,Inches(0.5),size=14,color=b.NAVY,bold=True,shrink=True)
d.footer(s,6,8)
notes(s,("This slide pre-empts the most common pushback an enterprise audience has: 'we already have copilots, isn't that "
 "the same thing?' The matrix answers it crisply by separating assistance from autonomy across five dimensions. A copilot "
 "does not trigger itself — a human must invoke it; an agent fires on an event. A copilot suggests the next step; an agent "
 "decides and executes it. A copilot cannot act across the systems of record; an agent does. A copilot does not own the "
 "outcome; an agent does, end to end. And the billing unit gives the game away: copilots are sold per seat, because they "
 "presuppose the seat, while agents are increasingly sold per outcome, because they replace it. The strategic significance "
 "is that copilots, by construction, cannot reset the budget — they make the existing seat faster, which is why they are an "
 "add-on line item rather than a re-architecture. Bring the field evidence to make this concrete and a little provocative: "
 "real contact-center audits show push-style agent-assist tools are used about one percent of the time; engineering teams "
 "describe AI code review as 'mostly noise' that trains reviewers to rubber-stamp; across the board the copilot adds a tab "
 "to an already-cluttered screen rather than removing the work. None of this is a knock on the technology — it is a "
 "statement about the ceiling of the form factor. Land the takeaway as the chapter's sharpest line so far: a copilot makes "
 "the seat faster, an agent makes the seat unnecessary, and only the second resets the budget. Then immediately set up "
 "slide 7's twist — making the second real (an agent that actually acts across a specific company's messy systems, safely) "
 "is not a model problem and not even an agent-platform problem; it is a delivery problem, and that is the layer nobody is "
 "serving for the mid-market."))

# SLIDE 7 — The AI Delivery Gap (value chain)
s=d.slide(fill=b.WHITE)
d.header(s,"The model is solved and the agent exists — the unsolved layer is delivery",
         "Integration, workflow, governance, operation: the value-chain stage everyone skips")
chain=[("Foundation model",["Commoditized","Frontier models converge; not the moat"],b.SOFT,b.NAVY,b.INK),
       ("Agent platform",["Funded","Sierra/Harvey/Glean/Vanta built the agents"],b.SOFT,b.NAVY,b.INK),
       ("Delivery layer",["UNOWNED","Integration · workflow · governance · run"],b.GOLD,b.NAVY,b.NAVY),
       ("Business outcome",["The prize","Resolved tickets · owned code · audit-ready"],b.NAVY,b.TEAL,b.WHITE)]
for x,(t,ls,fl,tc,bc) in zip(XS,chain):
    panel(s,x,Inches(2.05),PW,Inches(2.7),t,ls,fill=fl,tcol=tc,bcol=bc,tsize=14)
arrows(s,Inches(3.25))
d.rect(s,d.M,Inches(5.0),d.CW,Inches(1.0),b.NAVY_2,radius=0.03)
d.text(s,"Evidence: 20 of 25 use cases are INTEGRATE work · the semantic layer (not the model) drives accuracy · "
         "'automated' GRC evidence is often organized manual work · the leading modernizer needs system integrators · "
         "80% of orgs still can't fully automate — integration + skills are the blockers.",
       d.M+Inches(0.25),Inches(5.12),d.CW-Inches(0.5),Inches(0.8),size=12,color=b.LIGHT_TEAL,shrink=True)
d.text(s,"Everyone optimized the model and the agent. Almost no one delivers them into the mid-market. That gap is the company.",
       d.M,Inches(6.15),d.CW,Inches(0.6),size=14.5,color=b.NAVY,bold=True,shrink=True)
d.footer(s,7,8)
notes(s,("This is the pivotal slide of Chapter 2 — the one that names the company's reason to exist. Present the agentic "
 "value chain as four stages and force the audience to locate where the unsolved problem actually is. Stage one, the "
 "foundation model: solved and commoditizing, with frontier models converging in capability and falling in price; it is "
 "explicitly not the moat. Stage two, the agent platform: built and richly funded — Sierra, Harvey, Glean, Vanta and their "
 "peers have already produced excellent agents. Stage three, the delivery layer: integrating the agent into a specific "
 "company's systems of record, designing the workflow around it, governing it for safety and audit, and operating it in "
 "production — and this stage is essentially unowned for the mid-market. Stage four, the business outcome: the prize the "
 "buyer actually wants — resolved tickets, owned code, audit-ready evidence. The whole argument is that the industry has "
 "poured capital into stages one and two and almost none into stage three, even though stage three is what converts a "
 "demo into a deployed outcome. Marshal the evidence deliberately: twenty of our twenty-five use cases resolve to "
 "integration-and-workflow work rather than model or agent invention; production text-to-SQL accuracy comes from the "
 "semantic layer, not the model; 'automated' GRC evidence is frequently organized manual work that breaks silently; the "
 "best-funded legacy modernizer states its platform must be operated and delivered by system integrators; and surveys show "
 "roughly eighty percent of organizations still cannot fully automate, with integration complexity and skills — not "
 "appetite — as the blockers. Deliver the takeaway as the thesis of the entire book: everyone optimized the model and the "
 "agent; almost no one delivers them into the mid-market; that gap is the company. Then hand to slide 8: the gap is real, "
 "but is the timing right? The market data says the window is open now."))

# SLIDE 8 — Market Inflection Point (chart + signals)
s=d.slide(fill=b.WHITE)
d.header(s,"The inflection is now — demand compounding, incumbents forced to migrate, prices resetting",
         "Three signals say the window to land the mid-market is open today, not in two years")
s.shapes.add_picture(str(H/"chart_cagr.png"),d.M,Inches(1.75),width=Inches(6.5))
sig=[("DEMAND","Agentic sub-markets compounding 10–25%/yr — autonomous SOC 24.8%, AI support 23.1%, code review 20.2%"),
     ("SUPPLY SHOCK","Incumbents forcing migrations: Salesforce CPQ End-of-Sale strands 6,000+ orgs; Claude legal plug-ins triggered a ~$285B selloff"),
     ("PRICE RESET","Outcome pricing collapsing to $0.40–1.50 / resolution; $10/mo agents — 'cheap' is now table stakes")]
yy=Inches(1.85)
for t,txt in sig:
    d.rect(s,Inches(7.4),yy,Inches(5.33),Inches(1.45),b.SOFT,radius=0.05,shadow=True)
    d.text(s,t,Inches(7.6),yy+Inches(0.14),Inches(5),Inches(0.35),size=12.5,color=b.ACCENT,bold=True)
    d.text(s,txt,Inches(7.6),yy+Inches(0.52),Inches(4.95),Inches(0.85),size=11.5,color=b.INK,shrink=True,ls=1.05)
    yy=Inches(yy.inches+1.6)
d.rect(s,d.M,Inches(6.55),d.CW,Inches(0.6),b.NAVY,radius=0.03)
d.text(s,"Demand up, incumbents migrating, prices resetting — the mid-market window is open NOW. Chapter 3 maps it function by function.",
       d.M+Inches(0.25),Inches(6.62),d.CW-Inches(0.5),Inches(0.45),size=13,color=b.LIGHT_TEAL,bold=True,shrink=True)
d.footer(s,8,8)
notes(s,("Close Chapter 2 by answering the timing question directly, because a real gap with the wrong timing is not an "
 "opportunity. The argument is that three independent forces have converged right now. First, demand: the chart shows the "
 "agentic sub-markets compounding at rates between roughly ten and twenty-five percent a year — autonomous SOC near 24.8%, "
 "AI customer support 23.1%, AI code review 20.2%, fraud and DAM in the mid-teens, even the slower modernization and "
 "low-code markets in double digits. Markets grow at these rates during platform transitions, not incremental upgrades. "
 "Second, a supply shock on the incumbent side: vendors are themselves forcing the disruption. Salesforce putting CPQ into "
 "End-of-Sale strands more than six thousand organizations into a $250–750K reimplementation decision; Anthropic shipping "
 "Claude legal plug-ins erased roughly $285B of incumbent market value in a single session. When incumbents destabilize "
 "their own installed base, buyers are forced into the market — and a forced buyer is the best buyer an integrator can "
 "have. Third, a price reset: outcome pricing is collapsing toward $0.40–1.50 per resolution and ten-dollar-a-month "
 "agents, which means the conversation is no longer 'can we afford AI' but 'who will make it work in our environment' — "
 "exactly the question delivery answers. Put the three together and the message is that the window to land the mid-market "
 "is open today, and it will not stay uncontested: as price ceilings fall and forced migrations peak, the buyers are in "
 "motion now. End by handing to Chapter 3: with the thesis set and the timing established, the next chapter goes function "
 "by function — Customer Operations, Sales, HR, Finance, Procurement, Security, Legal, Analytics, Engineering, Operations "
 "— showing the workflow today, the incumbent vendors, the AI disruption, the opportunity, and DataStaqAI's positioning "
 "for each. That is where the abstract thesis becomes a concrete, addressable map."))

out=H/"DataStaqAI-Book-Ch2-AI-Transformation.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)

# companion spec
defs=[("4","Enterprise software re-platforms every ~15 years — each wave moved intelligence closer to the work",
       "Four-era pattern makes the agentic wave feel inevitable.","Per-seat SaaS model; agentic = outcome-billed.","4-era value-chain timeline + gold takeaway band"),
      ("5","AI crossed from 'predict' to 'do' — orchestration, not the model, is the scarce layer",
       "Capability staircase; the last step changes who acts.","Spider 2.0 (~87%→~10%); semantic layer drives accuracy.","Ascending 4-step staircase"),
      ("6","Copilots assist the seat — they don't remove it",
       "5-dimension copilot-vs-agent split.","Agent-assist used ~1% of time; code review 'mostly noise'.","Copilot-vs-agent capability matrix"),
      ("7","The model is solved and the agent exists — the unsolved layer is delivery",
       "4-stage value chain; delivery is unowned.","20/25 INTEGRATE; semantic layer; 80% can't fully automate.","Value chain with delivery stage highlighted gold"),
      ("8","The inflection is now — demand up, incumbents migrating, prices resetting",
       "Three converging signals; timing is now.","CAGR 10–25%; CPQ EOS 6,000 orgs; ~$285B selloff; $0.40–1.50/resolution.","CAGR bar chart + 3 signal cards")]
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 2 — The AI Transformation (Slides 4–8)\n",
      "Production standard: headline · analysis · evidence · visualization · speaker notes (300–500w). Figures source-traceable.\n"]
for (n,hl,an,ev,vz),t in zip(defs,nt):
    spec+= [f"\n## Slide {n} — {hl}\n",f"**Supporting analysis.** {an}\n",f"**Evidence.** {ev}\n",
            f"**Recommended visualization.** {vz}\n",f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter2-AI-Transformation.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter2-AI-Transformation.md")
