#!/usr/bin/env python3
"""PART V — Business Model (slides 34–38). Constructed/illustrative model, labeled.
Renders branded .pptx with notes + spec. Validated on save."""
import sys
sys.path.insert(0,"/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path
H=Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
d=Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 5: Business Model"); b=d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def band(s,y,txt,h=Inches(0.7),fill=None,col=None,size=13.5):
    d.rect(s,d.M,y,d.CW,h,fill or b.NAVY,radius=0.03)
    d.text(s,txt,d.M+Inches(0.25),y,d.CW-Inches(0.5),h,size=size,color=col or b.WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
def card(s,x,y,w,h,title,lines,*,fill=None,tc=None,bc=None,spine=True,tsize=14):
    fill=fill or b.SOFT; tc=tc or b.NAVY; bc=bc or b.INK
    d.rect(s,x,y,w,h,fill,radius=0.05,shadow=True)
    if spine: d.rect(s,x,y,Inches(0.12),h,b.TEAL)
    d.text(s,title,x+Inches(0.3),y+Inches(0.16),w-Inches(0.5),Inches(0.5),size=tsize,color=tc,bold=True,shrink=True)
    d.text(s,[{"text":t,"bullet":True,"space_before":6,"size":11,"color":bc} for t in lines],
           x+Inches(0.3),y+Inches(0.74),w-Inches(0.55),h-Inches(0.9),shrink=True,ls=1.06)

# 34 ICP
s=d.slide(fill=b.WHITE)
d.header(s,"The ICP is the mid-market company too big for SMB tools, too small for AI-natives — with a forced trigger",
         "Tight firmographics + a named champion + an observable trigger = a qualified deal  (illustrative profile)")
card(s,Inches(0.6),Inches(1.95),Inches(5.95),Inches(2.0),"FIRMOGRAPHICS",
     ["200–2,000 employees; ~$50M–$1B revenue","Verticals w/ acute pain: mfg & distribution, financial services, legal, healthcare-adjacent, B2B SaaS","Has real systems of record (ERP/CRM/HRIS/SIEM) but no internal agent team"])
card(s,Inches(6.73),Inches(1.95),Inches(6.0),Inches(2.0),"BUYER & CHAMPIONS",
     ["Econ buyer: CFO / COO / CIO","Champions: VP Eng/CTO, RevOps, Controller, Head of CX, CISO, Legal Ops","Pain owner who is measured on the broken workflow"])
card(s,Inches(0.6),Inches(4.1),Inches(5.95),Inches(2.0),"TRIGGER SIGNALS (the hunt)",
     ["Salesforce CPQ End-of-Sale; low-code license re-pricing","SOC-analyst job posts; failed OCR rollout; legal 'which-tools' review","Onboarding pain; month-end close slipping; dashboard sprawl"])
card(s,Inches(6.73),Inches(4.1),Inches(6.0),Inches(2.0),"DISQUALIFIERS",
     ["Pure SMB (<50 staff) → a self-serve SMB tool fits better","Global 2000 → a Global SI / direct AI-native deal","No system of record / no owned data to wire into"],spine=True,tc=b.CORAL)
band(s,Inches(6.25),"ICP in one line: a 200–2,000-person company with a real system of record, a measured pain owner, and a forced "
     "trigger — that can't afford the enterprise tool and can't staff the integration.",h=Inches(0.85),size=13)
d.footer(s,34,46)
notes(s,("Open the business-model chapter by making the customer concrete, because a fuzzy ICP is the most common reason a "
 "delivery business fails to scale. The ideal customer is defined on three dimensions that must all be true. "
 "Firmographically, it is a mid-market company — roughly 200 to 2,000 employees and $50M to $1B in revenue — in a "
 "vertical where the agentic pain is acute: manufacturing and distribution, financial services, legal, "
 "healthcare-adjacent, and B2B SaaS. Critically, it already runs real systems of record — an ERP, CRM, HRIS or SIEM — "
 "but has no internal team to build and operate agents on top of them. The buyer side has an economic buyer (CFO, COO "
 "or CIO) and a functional champion who is measured on the broken workflow — a VP of Engineering, a RevOps lead, a "
 "controller, a head of CX, a CISO, or a legal-ops manager. The third dimension, and the one that makes outbound "
 "efficient, is an observable trigger: a Salesforce CPQ End-of-Sale forcing a migration, a low-code license re-pricing, "
 "a SOC-analyst job posting signaling alert overload, a failed OCR rollout in AP, a legal 'which-tools' evaluation, or "
 "onboarding and month-end pain. The disqualifiers matter as much as the qualifiers: a sub-50-person SMB is better "
 "served by a self-serve tool; a Global-2000 enterprise belongs to a Global SI or a direct AI-native deal; and a "
 "company with no real system of record has nothing to wire into. State the ICP in one sentence the team can repeat: a "
 "200–2,000-person company with a real system of record, a measured pain owner, and a forced trigger, that can neither "
 "afford the enterprise tool nor staff the integration. Note clearly that the bands are illustrative starting "
 "parameters to be tightened with real win/loss data — but the shape is what makes the hunt (Chapter 6) efficient."))

# 35 service portfolio
s=d.slide(fill=b.WHITE)
d.header(s,"Three productized service lines map to the three delivery postures",
         "BUILD, INTEGRATE & operate, DEPLOY & tune — each a repeatable offer, not a bespoke project")
card(s,Inches(0.6),Inches(1.95),Inches(3.9),Inches(4.0),"BUILD STUDIO",
     ["Owned-code outcomes: legacy modernization, low-code escape, custom agents","Behavior-grounded; client keeps the code","Shape: fixed-scope project + maintenance retainer","Timeline: weeks–months"],fill=b.NAVY,tc=b.GOLD,bc=b.LIGHT_TEAL)
card(s,Inches(4.66),Inches(1.95),Inches(3.9),Inches(4.0),"INTEGRATE & OPERATE",
     ["Wire a best-of-breed agent into the SoR + own the workflow + governance","CPQ, AP, support, legal, search, fraud, GRC","Shape: monthly managed (recurring)","Timeline: 2–6 week standup"],fill=b.SOFT,tc=b.NAVY,bc=b.INK)
card(s,Inches(8.72),Inches(1.95),Inches(4.0),Inches(4.0),"DEPLOY & TUNE",
     ["Stand up + tune a mature tool the client can't run alone","SIEM investigation, predictive ops, code review, agent-assist","Shape: onboarding fee + retainer","Timeline: days–weeks"],fill=b.SOFT,tc=b.NAVY,bc=b.INK)
band(s,Inches(6.15),"One sales motion, three fulfilment shapes: BUILD earns trust (owned code), INTEGRATE drives recurring volume, "
     "DEPLOY lands fast wins — and all three expand into each other.",h=Inches(0.9),size=13)
d.footer(s,35,46)
notes(s,("The service portfolio operationalizes the three postures introduced earlier into three productized lines, which is "
 "the difference between a consultancy that reinvents every engagement and a scalable delivery firm with repeatable "
 "offers. The BUILD Studio delivers owned-code outcomes — legacy modernization, low-code escape, and bespoke agents "
 "where no off-the-shelf product exists — using the behavior-grounded method the leaders validated, with the client "
 "keeping the code; commercially it is a fixed-scope project plus a maintenance retainer, delivered in weeks to months, "
 "and it is the sharpest, highest-trust line. INTEGRATE & Operate is the volume engine: wire a best-of-breed agent into "
 "the customer's system of record, own the client-specific workflow and governance, and run it — across CPQ, AP, "
 "support, legal, search, fraud and GRC — sold as a monthly managed service that is recurring by construction, with a "
 "two-to-six-week standup. DEPLOY & Tune lands fast wins: stand up and tune a mature tool the client can't operate "
 "alone — SIEM investigation, predictive ops, code review, agent-assist — as an onboarding fee plus retainer, live in "
 "days to weeks. The strategic elegance, and the line to land, is that this is one sales motion with three fulfilment "
 "shapes, and the three feed each other: a BUILD engagement earns the trust and system access that make INTEGRATE "
 "deals easy; a DEPLOY win proves value fast and opens the door to INTEGRATE; and every INTEGRATE account is a "
 "land-and-expand base for more functions. Productizing matters because it lets junior delivery staff and reusable "
 "agent templates execute against a known scope, which is what converts a services business into one with software-like "
 "leverage — the subject of the delivery-model slide. Keep the framing that these are offers, not projects: named, "
 "scoped, repeatable, and priced — the next slide makes the pricing explicit."))

# 36 pricing
s=d.slide(fill=b.WHITE)
d.header(s,"Pricing blends a fixed build fee with a managed monthly — predictable for the buyer, recurring for us",
         "Positioned below every enterprise floor; designed for land-and-expand  (illustrative tiers)")
tiers=[("PILOT / LAND","1 use case, INTEGRATE or DEPLOY","~$2–3k / mo","2–4 wk standup"),
       ("GROWTH","2–3 use cases + governance","~$5–8k / mo","land-and-expand"),
       ("MULTI-FUNCTION","Cross-function managed program","~$10–15k / mo","quarterly expansion"),
       ("BUILD PROJECT","Owned-code modernization / escape","~$40–150k fixed + retainer","milestone-based")]
xs=[Inches(0.6),Inches(3.63),Inches(6.66),Inches(9.69)]
for x,(t,what,price,extra) in zip(xs,tiers):
    fill=b.NAVY if t=="BUILD PROJECT" else b.SOFT
    d.rect(s,x,Inches(1.95),Inches(2.85),Inches(3.2),fill,radius=0.05,shadow=True)
    d.text(s,t,x+Inches(0.2),Inches(2.1),Inches(2.5),Inches(0.4),size=12.5,color=(b.GOLD if fill==b.NAVY else b.NAVY),bold=True,shrink=True)
    d.text(s,price,x+Inches(0.2),Inches(2.55),Inches(2.5),Inches(0.6),size=17,color=(b.TEAL if fill==b.NAVY else b.ACCENT),bold=True,shrink=True)
    d.text(s,[{"text":what,"size":11,"color":b.LIGHT_TEAL if fill==b.NAVY else b.INK,"space_before":2},
              {"text":extra,"size":10.5,"color":b.MUTED,"space_before":8,"italic":True}],
           x+Inches(0.2),Inches(3.3),Inches(2.5),Inches(1.7),shrink=True,ls=1.06)
band(s,Inches(5.4),"Anchor vs the floor: incumbents start at $40K (search) → $360K/yr (legal). DataStaqAI's $24–60K/yr band "
     "undercuts them while delivering the outcome the cheaper SMB tools don't. (Illustrative — refine with win/loss.)",
     h=Inches(1.0),size=13)
d.footer(s,36,46)
notes(s,("Pricing is where the mid-market position becomes a number, so present it as a deliberate structure rather than a "
 "rate card. The model blends two components: a recurring managed monthly that makes revenue predictable for "
 "DataStaqAI, and, for the BUILD line, a fixed project fee that funds delivery up front and de-risks cash flow. Four "
 "illustrative tiers express the land-and-expand motion. The Pilot/Land tier — a single INTEGRATE or DEPLOY use case at "
 "roughly $2–3k a month with a two-to-four-week standup — is the wedge: small enough to approve without a committee, "
 "fast enough to prove value. Growth — two to three use cases plus governance at roughly $5–8k a month — is the "
 "expansion most accounts settle into. Multi-Function — a cross-function managed program at roughly $10–15k a month — "
 "is the mature account. And the BUILD Project — owned-code modernization or low-code escape at roughly $40–150k fixed "
 "plus a retainer — is the high-trust, high-value engagement that often opens the relationship. The single most "
 "important framing, in the band, is the anchor against the competitive floor established in Chapter 4: incumbents start "
 "at $40k a year for search and run to $360k for legal, before the agent engineers the buyer must also supply. "
 "DataStaqAI's $24–60k/year band undercuts every one of those floors while delivering the outcome that the cheap "
 "self-serve SMB tools do not. That is the pricing thesis in one sentence: priced below the enterprise floor, scoped "
 "above the SMB tool. Be explicit that these tiers are illustrative and must be refined with real win/loss and "
 "cost-to-serve data; the point of the slide is the structure — recurring monthly plus fixed build, anchored below the "
 "floor, built for expansion — not the precise dollar figures. The delivery model next shows why these prices can be "
 "profitable."))

# 37 delivery model
s=d.slide(fill=b.WHITE)
d.header(s,"Delivery runs on engineering leverage — agents build for us, so margin scales with reuse, not headcount",
         "A reusable agent + connector library makes each new engagement cheaper than the last")
steps=["Discover + qualify","Wire / BUILD (OpenHands + subagents + MCPs)","Govern (policy + provenance)","Operate + monitor","Expand"]
xs=[Inches(0.6+ (2.45)*i) for i in range(5)]
for i,(x,st) in enumerate(zip(xs,steps)):
    d.rect(s,x,Inches(1.95),Inches(2.25),Inches(0.95),b.NAVY,radius=0.06)
    d.text(s,st,x+Inches(0.1),Inches(1.95),Inches(2.05),Inches(0.95),size=10.5,color=b.WHITE,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    if i<4: d.text(s,"→",x+Inches(2.25),Inches(1.95),Inches(0.2),Inches(0.95),size=18,color=b.TEAL,bold=True,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
card(s,Inches(0.6),Inches(3.2),Inches(5.95),Inches(2.6),"THE LEVERAGE",
     ["Reusable agents, connectors (MCPs) & workflow templates compound across clients","Each engagement adds to the library → next one is faster & cheaper","Junior delivery staff execute against productized scope","Gross margin rises with reuse, not with headcount"],fill=b.SOFT,tc=b.NAVY)
card(s,Inches(6.73),Inches(3.2),Inches(6.0),Inches(2.6),"WHY IT'S NOT A BODY-SHOP",
     ["SIs scale with billable hours; we scale with reusable software assets","Target gross margin trends toward software as the library matures","Outcome-priced, not time-and-materials","The library is a compounding moat competitors must rebuild"],fill=b.NAVY,tc=b.TEAL,bc=b.LIGHT_TEAL)
d.footer(s,37,46)
notes(s,("This slide answers the toughest question about any delivery business: 'isn't this just a consultancy that scales "
 "with headcount?' The pipeline across the top — discover and qualify, wire or build using OpenHands with subagents and "
 "MCP integrations, govern with policy and provenance, operate and monitor, then expand — is the repeatable delivery "
 "motion. But the strategic content is below it: the leverage. Every engagement contributes reusable agents, connectors "
 "and workflow templates to a shared library, so each new client engagement starts further along and costs less to "
 "deliver than the last. That is the mechanism that separates DataStaqAI from a body-shop: a systems integrator scales "
 "revenue by adding billable hours, and its margin is capped by labor; DataStaqAI scales by adding reusable software "
 "assets, so gross margin trends upward toward software-like levels as the library matures, and junior delivery staff "
 "can execute against productized scope rather than every senior engineer reinventing each project. Reinforce that the "
 "pricing is outcome-based, not time-and-materials, which aligns incentives and protects margin as delivery gets more "
 "efficient. And make the defensibility point: the accumulated library — the wired integrations, the governance "
 "patterns, the function-specific agent templates — is a compounding moat that a competitor would have to rebuild "
 "client by client. Be candid about the honest tension surfaced in the SWOT: in the early stage, before the library is "
 "deep, delivery does carry a services flavor and capacity is real; the model bets that disciplined productization and "
 "reuse convert that into software economics over time. The investor translation, which Chapter 7 will make explicit, "
 "is that this is a services business with a software trajectory — which is exactly the profile that can reach the "
 "$5–10M target with healthy margins. The revenue model next shows how those engagements stack into recurring "
 "revenue."))

# 38 revenue model
s=d.slide(fill=b.WHITE)
d.header(s,"Revenue compounds: land a use case, expand across functions, on a recurring managed base",
         "Recurring managed retainers + build projects + expansion = durable, growing ARR  (illustrative mix)")
card(s,Inches(0.6),Inches(1.95),Inches(3.9),Inches(2.5),"RECURRING MANAGED  (~70%)",
     ["Monthly INTEGRATE/DEPLOY retainers","Predictable, compounding ARR base","Sticky: wired into the SoR + governance"],fill=b.NAVY,tc=b.TEAL,bc=b.LIGHT_TEAL)
card(s,Inches(4.66),Inches(1.95),Inches(3.9),Inches(2.5),"BUILD PROJECTS  (~30%)",
     ["Fixed-fee owned-code engagements","Funds delivery up front; high-trust entry","Converts into managed retainers"],fill=b.SOFT,tc=b.NAVY)
card(s,Inches(8.72),Inches(1.95),Inches(4.0),Inches(2.5),"EXPANSION  (NRR > 100%)",
     ["Land 1 function → expand to 3–5","Cross-sell BUILD ↔ INTEGRATE ↔ DEPLOY","Net revenue retention is the growth engine"],fill=b.SOFT,tc=b.NAVY)
d.rect(s,d.M,Inches(4.75),d.CW,Inches(1.0),b.SOFT,radius=0.03)
d.text(s,"LAND  →  EXPAND  →  COMPOUND", d.M+Inches(0.25),Inches(4.85),Inches(5),Inches(0.35),size=12,color=b.ACCENT,bold=True)
d.text(s,"Pilot one use case at $2–3k/mo  →  add functions to $10–15k/mo  →  layer BUILD projects  →  a growing recurring "
         "base with NRR-driven expansion. Few logos needed to reach $5–10M (Chapter 6 does the math).",
       d.M+Inches(0.25),Inches(5.2),d.CW-Inches(0.5),Inches(0.5),size=12,color=b.INK,shrink=True)
band(s,Inches(6.0),"~70% recurring + ~30% build, with NRR>100% — a services entry that compounds into software-like recurring "
     "revenue. (Illustrative mix; validated in Chapter 6.)",h=Inches(1.0),size=13)
d.footer(s,38,46)
notes(s,("Close the business-model chapter by showing how individual engagements stack into durable, compounding revenue — "
 "the structure, with the actual three-year math reserved for Chapter 6. Revenue has three streams. Recurring managed, "
 "the largest at an illustrative ~70%, is the monthly INTEGRATE and DEPLOY retainers — predictable, compounding, and "
 "sticky because the agent is wired into the customer's system of record and governance, which raises switching costs. "
 "Build projects, ~30%, are the fixed-fee owned-code engagements that fund delivery up front, provide a high-trust entry "
 "point, and convert into managed retainers once the built system needs operating. Expansion is the growth engine and "
 "the reason net revenue retention can exceed 100%: land a single function, then expand the same account to three to "
 "five functions, cross-selling across BUILD, INTEGRATE and DEPLOY. The motion to emphasize is land, expand, compound: "
 "a pilot at $2–3k a month grows to a multi-function program at $10–15k a month, layered with build projects, producing "
 "a recurring base that grows from within even before new logos are added. The strategic payoff, and the bridge to "
 "Chapter 6, is that an expansion-led model needs surprisingly few logos to reach $5–10M, because each account "
 "compounds — which is why net revenue retention, not just new-logo acquisition, is the metric that matters. Frame the "
 "blended picture honestly: roughly 70% recurring plus 30% build, with NRR above 100%, is a services entry that "
 "compounds into software-like recurring revenue over time. Stress once more that the mix and percentages are "
 "illustrative and will be calibrated with real cohort data; the durable claim is the shape — a sticky recurring base, "
 "a high-trust build wedge, and expansion as the engine. Chapter 6 now turns this structure into a concrete path to "
 "$5–10M: acquisition, expansion, hiring, unit economics, and the execution roadmap."))

out=H/"DataStaqAI-Book-Ch5-Business-Model.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)
defs=[("34","ICP — mid-market, real SoR, measured pain owner, forced trigger","ICP profile (4 panels)"),
      ("35","Three productized service lines map to the three postures","3 service-line cards"),
      ("36","Pricing blends fixed build + managed monthly, below every floor","4 pricing-tier cards"),
      ("37","Delivery runs on engineering leverage — margin scales with reuse","5-step pipeline + leverage panels"),
      ("38","Revenue compounds: land → expand → recurring base (NRR>100%)","3 revenue-stream cards + motion strip")]
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 5 — Business Model (Slides 34–38)\n","Constructed/illustrative model, labeled. Headline · viz · 300w notes.\n"]
for (n,hl,vz),t in zip(defs,nt):
    spec+=[f"\n## Slide {n} — {hl}\n",f"**Recommended visualization.** {vz}\n",f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter5-Business-Model.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter5-Business-Model.md")
