#!/usr/bin/env python3
"""PART IV-a — Competitive Analysis, slides 19–26. Diagram-forward.
Renders branded .pptx with speaker notes + companion spec. Validated on save."""
import sys
sys.path.insert(0, "/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path

H = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
A = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/analysis")
d = Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 4: Competitive Analysis")
b = d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def band(s,y,txt,h=Inches(0.7),fill=None,col=None,size=14):
    d.rect(s,d.M,y,d.CW,h,fill or b.NAVY,radius=0.03)
    d.text(s,txt,d.M+Inches(0.25),y,d.CW-Inches(0.5),h,size=size,color=col or b.WHITE,bold=True,
           anchor=MSO_ANCHOR.MIDDLE,shrink=True)
def twocol(s,lt,ll,rt,rl,*,lfill,lt_c,rfill,rt_c,top=Inches(1.95),h=Inches(3.0)):
    d.rect(s,d.M,top,Inches(5.9),h,lfill,radius=0.05,shadow=True)
    d.text(s,lt,d.M+Inches(0.2),top+Inches(0.16),Inches(5.5),Inches(0.4),size=14,color=lt_c,bold=True)
    d.text(s,[{"text":t,"bullet":True,"space_before":6,"size":12,"color":b.INK if lfill!=b.NAVY else b.LIGHT_TEAL} for t in ll],
           d.M+Inches(0.2),top+Inches(0.66),Inches(5.5),h-Inches(0.8),shrink=True,ls=1.06)
    x2=Inches(6.73)
    d.rect(s,x2,top,Inches(6.0),h,rfill,radius=0.05,shadow=True)
    d.text(s,rt,x2+Inches(0.2),top+Inches(0.16),Inches(5.6),Inches(0.4),size=14,color=rt_c,bold=True)
    d.text(s,[{"text":t,"bullet":True,"space_before":6,"size":12,"color":b.INK if rfill!=b.NAVY else b.LIGHT_TEAL} for t in rl],
           x2+Inches(0.2),top+Inches(0.66),Inches(5.6),h-Inches(0.8),shrink=True,ls=1.06)

# 19 — ecosystem stack
s=d.slide(fill=b.WHITE)
d.header(s,"The enterprise AI stack has four layers — value is migrating to the one nobody serves",
         "Foundation model · agent platform · delivery · system of record — the delivery layer is the gap")
layers=[("FOUNDATION MODELS — commoditizing","OpenAI · Anthropic · Google · Meta · open models",b.SOFT,b.INK,b.NAVY),
        ("AGENT PLATFORMS — funded","Sierra · Harvey · Glean · Decagon · Vanta · Torq · Rossum",b.SOFT,b.INK,b.NAVY),
        ("DELIVERY LAYER — unowned for the mid-market","Global SIs (enterprise-only)   →   DataStaqAI (mid-market, done-for-you)",b.GOLD,b.NAVY,b.NAVY),
        ("SYSTEMS OF RECORD — the moat stays","Salesforce · Workday · SAP · Splunk · OutSystems · ERPs",b.NAVY,b.WHITE,b.TEAL)]
y=1.95
for lab,ex,fl,exc,labc in layers:
    d.rect(s,d.M,Inches(y),d.CW,Inches(0.95),fl,radius=0.04,shadow=True)
    d.text(s,lab,d.M+Inches(0.25),Inches(y+0.12),Inches(5.6),Inches(0.7),size=13.5,color=labc,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    d.text(s,ex,d.M+Inches(6.0),Inches(y+0.12),Inches(6.0),Inches(0.7),size=11.5,color=exc,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    y+=1.06
band(s,Inches(6.35),"The model commoditizes and the system of record persists. The agent platform is funded. The "
     "delivery layer — wiring it all together for the mid-market — is the unowned value layer.",h=Inches(0.7),size=13)
d.footer(s,19,46)
notes(s,("Open Chapter 4 with the map the rest of the chapter navigates: the enterprise AI stack has four layers, and the "
 "purpose of this slide is to show value migrating to the layer nobody serves for the mid-market. The top layer, "
 "foundation models, is commoditizing — OpenAI, Anthropic, Google, Meta and open models converge in capability and fall "
 "in price, so the model is an input, not a moat. The second layer, agent platforms, is richly funded — Sierra, Harvey, "
 "Glean, Decagon, Vanta, Torq, Rossum — and these are genuinely good products. The bottom layer, systems of record — "
 "Salesforce, Workday, SAP, Splunk, OutSystems, the ERPs — persists, because the proprietary data and workflow are the "
 "durable moat; agents ride on top of it rather than replacing it. The third layer, delivery, is the one this whole "
 "document is about: wiring the agent into the systems of record, designing the workflow, governing it, operating it. "
 "Today that layer is owned only by global systems integrators, and they serve only the Global 2000. For the mid-market "
 "it is unowned. Use the gold band to make the strategic claim unmissable: the model commoditizes, the system of record "
 "persists, the agent platform is funded — and the delivery layer is where the value accrues and where the competition is "
 "thinnest. Every subsequent slide in the chapter zooms into one part of this map: who the archetypes are, how the "
 "incumbents and AI-natives and SIs each compete, how pricing and funding have concentrated, and where the white space "
 "sits. Tell the audience to keep this four-layer picture in mind, because DataStaqAI's entire position is 'we own the "
 "delivery layer for the mid-market,' and this slide is the proof that such a layer exists and is empty."))

# 20 — segmentation 2x2
s=d.slide(fill=b.WHITE)
d.header(s,"Segment two ways — by buyer size and by who delivers — and the mid-market done-for-you cell is empty",
         "The competitive map has a structural hole exactly where DataStaqAI sits")
X0,Y0,CWf,HT=0.6,2.0,12.133,4.0; XM=X0+CWf/2; YM=Y0+HT/2; cwf=CWf/2-0.1; chf=HT/2-0.1
def quad(cx,cy,w,h,title,lines,fill,tc):
    d.rect(s,cx,cy,w,h,fill,radius=0.04,shadow=True)
    d.text(s,title,cx+Inches(0.18),cy+Inches(0.14),w-Inches(0.36),Inches(0.4),size=12.5,color=tc,bold=True)
    d.text(s,[{"text":t,"bullet":True,"space_before":5,"size":11,"color":b.INK if fill!=b.NAVY else b.LIGHT_TEAL} for t in lines],
           cx+Inches(0.18),cy+Inches(0.6),w-Inches(0.36),h-Inches(0.74),shrink=True,ls=1.05)
cw=Inches(cwf); ch=Inches(chf)
quad(Inches(X0),Inches(Y0),cw,ch,"Enterprise · Self-serve product",["AI-native platforms","Sierra, Glean, Harvey, Decagon, Vanta"],b.SOFT,b.NAVY)
quad(Inches(XM+0.1),Inches(Y0),cw,ch,"Mid-market · Self-serve product",["SMB point tools","Freshdesk Freddy, Botpress, eesel, Sprinto"],b.SOFT,b.NAVY)
quad(Inches(X0),Inches(YM+0.1),cw,ch,"Enterprise · Done-for-you",["Global SIs + managed tiers","Accenture, Deloitte, Crescendo (BPO)"],b.SOFT,b.NAVY)
quad(Inches(XM+0.1),Inches(YM+0.1),cw,ch,"Mid-market · Done-for-you  ← EMPTY",["The structural hole","DataStaqAI: wire + own + run, at $2–5k/mo"],b.NAVY,b.TEAL)
d.text(s,"BUYER →  Enterprise … Mid-market      |      DELIVERY ↓  Self-serve … Done-for-you",d.M,Inches(6.15),d.CW,Inches(0.3),size=10.5,color=b.MUTED)
band(s,Inches(6.5),"Three cells are crowded. The fourth — mid-market companies that need it done for them — is the opening.",h=Inches(0.55),size=13)
d.footer(s,20,46)
notes(s,("This slide reduces a noisy market to a single 2x2 so the audience can see the hole rather than be told about it. "
 "Segment the market on two axes. The horizontal axis is buyer size: enterprise on the left, mid-market on the right. "
 "The vertical axis is who does the delivery: self-serve product at the top, done-for-you at the bottom. Now place the "
 "players. Top-left, enterprise buyers served by self-serve products: the funded AI-natives — Sierra, Glean, Harvey, "
 "Decagon, Vanta — who sell a powerful platform the enterprise's own engineers operate. Top-right, mid-market buyers "
 "served by self-serve products: the SMB point tools — Freshdesk Freddy, Botpress, eesel, Sprinto — cheap but "
 "self-operated and shallow. Bottom-left, enterprise buyers served done-for-you: the global systems integrators "
 "(Accenture, Deloitte) plus the AI-natives' own managed and BPO tiers (Crescendo). And bottom-right, mid-market buyers "
 "who need it done for them: empty. That empty cell is the entire thesis rendered as geography. The mid-market company is "
 "too small for the enterprise AI-native and its agent engineers, too complex for a self-serve SMB tool, and not worth a "
 "Global SI's time — so no one delivers the agent into their systems for them. DataStaqAI occupies that cell: wire it, "
 "own the workflow and governance, run it, at $2–5k/month. Make the closing point explicit — three of the four cells are "
 "crowded with well-funded competitors, and the fourth is structurally open, not because it lacks demand (Chapters 1–3 "
 "proved the demand) but because every existing archetype is optimized away from it. The next slide names those "
 "archetypes and shows precisely how each one is optimized away from this cell."))

# 21 — archetypes
s=d.slide(fill=b.WHITE)
d.header(s,"Five archetypes compete for the agent budget — each optimized away from the mid-market outcome",
         "Knowing the archetype tells you exactly where each competitor stops short")
arch=[("Incumbent Defender","Bolts AI on the seat it sells","Won't cannibalise seat revenue",b.SOFT),
      ("AI-Native Point Solution","Best agent, enterprise-first","6-figure floor + agent engineers",b.SOFT),
      ("Managed / BPO Hybrid","Runs it for you, with people","Labor-cost scaling, not engineering",b.SOFT),
      ("Global Systems Integrator","Delivers — for the Global 2000","Too slow & costly for mid-market",b.SOFT),
      ("Horizontal Agent Platform","Build-your-own-agent toolkit","You still supply the delivery",b.SOFT)]
cw=Inches(2.3)
xs=[Inches(0.6+ (2.3+0.12)*i) for i in range(5)]
for x,(t,what,stop,fl) in zip(xs,arch):
    d.rect(s,x,Inches(2.0),cw,Inches(3.3),fl,radius=0.05,shadow=True)
    d.rect(s,x,Inches(2.0),cw,Inches(0.55),b.NAVY,radius=0.05)
    d.text(s,t,x+Inches(0.12),Inches(2.0),cw-Inches(0.24),Inches(0.55),size=11.5,color=b.TEAL,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    d.text(s,[{"text":"Play: "+what,"size":10.5,"color":b.INK,"space_before":2},
              {"text":"Stops short: "+stop,"size":10.5,"color":b.CORAL,"bold":True,"space_before":10}],
           x+Inches(0.14),Inches(2.7),cw-Inches(0.28),Inches(2.4),shrink=True,ls=1.08)
band(s,Inches(5.6),"DataStaqAI is the sixth archetype: the mid-market delivery specialist — engineering economics (not labor), "
     "outcome-owned, priced for the middle. It is defined by the gap the other five leave.",h=Inches(0.95),fill=b.NAVY,size=13.5)
d.footer(s,21,46)
notes(s,("This slide gives the audience a vocabulary that makes the rest of the chapter legible: five competitor archetypes, "
 "each with a play and, crucially, a structural reason it stops short of the mid-market outcome. The Incumbent Defender "
 "(Zendesk, Salesforce, Workday) bolts AI onto the seat it already sells and cannot cannibalise its own seat revenue, so "
 "its AI is an add-on, never a re-architecture. The AI-Native Point Solution (Sierra, Harvey, Glean) builds the best "
 "agent but goes enterprise-first, with six-figure floors and a requirement that the buyer supply agent engineers. The "
 "Managed/BPO Hybrid (Crescendo) will run it for you, but with people, so its economics scale with labor cost rather "
 "than engineering leverage. The Global Systems Integrator (Accenture, Deloitte, IBM) genuinely delivers, but only for "
 "the Global 2000, because their cost structure and sales motion are too slow and expensive for a mid-market shop. And "
 "the Horizontal Agent Platform (the build-your-own-agent toolkits) hands you primitives but leaves you to supply the "
 "delivery yourself. The pattern is the punchline: every archetype is optimized away from the same place — a mid-market "
 "company that wants the agent delivered into its systems with engineering economics and an owned outcome. DataStaqAI is "
 "best understood as a sixth archetype defined precisely by that gap: the mid-market delivery specialist, with "
 "engineering economics rather than labor, the outcome owned rather than a tool handed over, and pricing built for the "
 "middle. Stress that this is not a claim of being 'better' than the other five at their own game — it is a claim of "
 "occupying a different, empty position. The next three slides examine the three most important archetypes — incumbents, "
 "AI-natives, and systems integrators — in detail, because those are the ones a buyer will compare us against."))

# 22 — incumbents
s=d.slide(fill=b.WHITE)
d.header(s,"Incumbents own distribution and the system of record — but can't disrupt the seat they sell",
         "Their strength is also their cage")
twocol(s,"STRENGTHS",["Distribution + installed base + procurement trust","Compliance, security, and the system-of-record data moat","AI shipped as a safe add-on to an existing contract"],
       "STRUCTURAL LIMITS",["Won't cannibalise seat revenue → AI as a line item, not a re-architecture","Slow, committee-bound roadmaps; per-seat pricing preserved","Agentforce $200/seat, Zendesk add-ons, Looker dev-heavy"],
       lfill=b.SOFT,lt_c=b.ACCENT,rfill=b.SOFT,rt_c=b.CORAL)
band(s,Inches(5.2),"Examples: Zendesk · Salesforce · Workday · Splunk · OutSystems · Looker. Implication: incumbents are the "
     "system of record we wire INTO — partners, not the battleground.",h=Inches(1.1),size=13.5)
d.footer(s,22,46)
notes(s,("Examine the incumbent camp honestly, because a buyer's default is to ask 'why not just wait for Salesforce or "
 "Zendesk to ship this?' The strengths are real and should be stated plainly: incumbents own distribution, the installed "
 "base, and procurement trust; they hold compliance, security, and the system-of-record data that is the durable moat; "
 "and they can ship AI as a low-friction add-on to a contract the customer already has. That is a strong hand. But the "
 "limits are structural, not temporary. An incumbent cannot lead the disruption because its revenue is the seat, and "
 "cannibalising the seat is irrational — so its AI arrives as a line item bolted onto the existing model rather than a "
 "re-architecture of the work, and its pricing stays per-seat (Agentforce at $200/seat, Zendesk's stack of add-ons, "
 "Looker's developer-heavy LookML). Roadmaps are committee-bound and slow. The strategic conclusion is the most "
 "important takeaway of the slide and a reframe of the whole competitive question: incumbents are not the battleground — "
 "they are the system of record DataStaqAI wires INTO. We do not displace Workday or Splunk; we make the agent layer on "
 "top of them work for the mid-market. That turns the most fearsome-looking competitor into a partner and an asset: their "
 "persistence is what makes the delivery layer necessary and durable. Tell the audience to hold this distinction, "
 "because it recurs in the business model — DataStaqAI's defensibility comes partly from being aligned with, not opposed "
 "to, the systems the customer will never rip out. The next slide turns to the AI-natives, who are the opposite case: "
 "genuinely disruptive, genuinely excellent, and genuinely unable to serve the middle."))

# 23 — AI-natives
s=d.slide(fill=b.WHITE)
d.header(s,"AI-natives build the best agents — and price them for the Fortune 500",
         "Excellent products, structurally enterprise-first — they concede the mid-market")
twocol(s,"STRENGTHS",["Best-in-class agent quality and shipping velocity","Category-defining valuations & capital (winner-take-most bet)","Sierra $15.8B · Harvey $11B · Glean $7.2B · Decagon $4.5B · Vanta $4.15B"],
       "STRUCTURAL LIMITS",["Six-figure floors + dedicated agent engineers required","Sit on top of a separate SoR → integration TCO on the buyer","Wrapper-risk where there's no proprietary data moat"],
       lfill=b.SOFT,lt_c=b.ACCENT,rfill=b.SOFT,rt_c=b.CORAL)
band(s,Inches(5.2),"They've already conceded the gap — shipping managed/forward-deployed tiers because mid-market buyers can't run "
     "the agents alone. We are the delivery layer they implicitly require.",h=Inches(1.1),fill=b.NAVY,size=13.5)
d.footer(s,23,46)
notes(s,("Give the AI-natives full credit, because over-claiming against them destroys credibility. Their strengths are "
 "genuine and formidable: best-in-class agent quality, extraordinary shipping velocity, and category-defining "
 "valuations and capital — Sierra at $15.8B, Harvey at $11B, Glean at $7.2B, Decagon at $4.5B, Vanta at $4.15B — which "
 "reflect a deliberate winner-take-most enterprise bet. DataStaqAI does not try to out-build these agents; it rides on "
 "them. The limits, again, are structural rather than fixable with a price cut. Their floors are six figures and they "
 "require the buyer to supply dedicated agent engineers or accept forward-deployed teams; their products sit on top of a "
 "separate system of record, so the integration total-cost-of-ownership lands on the buyer; and where a vendor lacks a "
 "proprietary data moat, it carries wrapper-risk as frontier models advance. The decisive evidence — and the reason this "
 "slide ends on a navy emphasis band — is that the AI-natives have already conceded the mid-market gap by shipping "
 "managed and forward-deployed services, because their own customers cannot operate the agents alone. That concession is "
 "DataStaqAI's validation: the delivery layer is not a 'nice to have' the natives could bolt on; it is a function they "
 "implicitly require and are bad at, because doing it at mid-market scale needs engineering economics and a "
 "services-light delivery model, not six-figure white-glove teams. Frame the relationship precisely: the AI-natives are "
 "suppliers and, occasionally, the agent we deploy — not the competitor we beat on agent quality. We beat them only on "
 "the question they don't want to answer: who makes this work, affordably, in a mid-market company's messy systems? The "
 "next slide addresses the one archetype that does answer that question — the systems integrators — and why they still "
 "miss the middle."))

# 24 — systems integrators
s=d.slide(fill=b.WHITE)
d.header(s,"The integrators that actually deliver serve only the Global 2000 — leaving the mid-market unintegrated",
         "DataStaqAI is the SI model rebuilt for the mid-market on engineering economics")
twocol(s,"GLOBAL SIs (Accenture · Deloitte · IBM)",["Real delivery capability + enterprise trust","But: $M+ engagements, multi-quarter timelines","Optimized for Global-2000 transformation programs","Mechanical Orchard's platform is 'built to be operated by SIs'"],
       "DATASTAQAI (mid-market delivery)",["Engineering economics: agents + subagents + MCPs, ~$2–5k/mo","Weeks, not quarters; the client owns the outcome (and the code)","Wire best-of-breed agents into the client's SoR + governance","Same delivery role the leading methods require — for the middle"],
       lfill=b.SOFT,lt_c=b.NAVY,rfill=b.NAVY,rt_c=b.TEAL)
band(s,Inches(5.5),"The market's best methods explicitly NEED a delivery layer — and aim it at the Global 2000. DataStaqAI is that "
     "layer, repriced and re-architected for the mid-market.",h=Inches(0.85),size=13.5)
d.footer(s,24,46)
notes(s,("This slide handles the most direct competitor to DataStaqAI's actual function — the systems integrators — and "
 "turns their existence into proof rather than threat. The global SIs (Accenture, Deloitte, IBM) have genuine delivery "
 "capability and deep enterprise trust; they are the only archetype that truly does the wiring, governance and operation "
 "that the delivery layer requires. But they do it as million-dollar-plus engagements on multi-quarter timelines, "
 "optimized for Global-2000 transformation programs. The most important external validation in the entire deck sits "
 "here: Mechanical Orchard — the best-funded company using the leading behavior-first modernization method — states its "
 "platform is 'built to be operated and delivered by system integrators,' and it serves only the Global 2000. In other "
 "words, the market's most advanced methods explicitly require a delivery layer and explicitly aim it at the largest "
 "enterprises. DataStaqAI is that same delivery layer, repriced and re-architected for the mid-market: engineering "
 "economics rather than billable armies — agents, subagents and thousands of MCP integrations at roughly $2–5k/month — "
 "delivering in weeks rather than quarters, with the client owning the outcome and, in the build plays, the code. The "
 "argument to land is that DataStaqAI is not inventing a new category; it is taking a proven, necessary role (systems "
 "integration for the agent era) and bringing it to a segment the incumbent SIs cannot economically serve. That is a far "
 "more credible and fundable story than 'a new kind of company,' because investors and buyers already understand SIs — "
 "the novelty is only the economics and the segment. With the three comparison archetypes covered, the next two slides "
 "quantify the competition with the pricing and funding data, before sub-iteration two moves to coverage, white space, "
 "SWOT, the disruption matrix and why DataStaqAI wins."))

# 25 — pricing comparison (chart)
s=d.slide(fill=b.WHITE)
d.header(s,"Pricing has bifurcated — enterprise ACV vs usage — and DataStaqAI's band undercuts the floor",
         "The mid-market sits below every published incumbent floor but GRC")
s.shapes.add_picture(str(A/"chart2_price_floor_gap.png"),d.M,Inches(1.75),width=Inches(7.4))
sigs=[("TWO PRICING WORLDS","Enterprise ACV ($50K–$4.8M/yr) ↔ usage/outcome ($0.40–1.50 per resolution)"),
      ("THE FLOOR","Legal $360K · NL-analytics $150K · agent-assist $60K · search $40K /yr"),
      ("OUR BAND","$24–60K/yr ($2–5k/mo) undercuts every floor but GRC ($4K → compete on integration, not price)")]
yy=2.0
for t,x in sigs:
    d.rect(s,Inches(8.2),Inches(yy),Inches(4.5),Inches(1.4),b.SOFT,radius=0.05,shadow=True)
    d.text(s,t,Inches(8.4),Inches(yy+0.13),Inches(4.1),Inches(0.35),size=12,color=b.ACCENT,bold=True)
    d.text(s,x,Inches(8.4),Inches(yy+0.5),Inches(4.1),Inches(0.8),size=11,color=b.INK,shrink=True,ls=1.05)
    yy+=1.55
d.footer(s,25,46)
notes(s,("Now quantify the competition, starting with pricing, because price is where the mid-market gap is most legible to "
 "a buyer. The chart shows the published enterprise entry floors across the use cases that disclose them, sorted, with "
 "DataStaqAI's $24–60K/year band shaded. The story is in three parts. First, pricing has bifurcated into two worlds that "
 "do not meet in the middle: enterprise annual contracts running from roughly $50K to several million dollars a year, "
 "versus usage and outcome pricing at $0.40–1.50 per resolution. The model a buyer signs determines their unit economics "
 "for years, and neither world is built for a mid-market company that wants a delivered outcome at a predictable price. "
 "Second, the floor: legal AI starts around $360K/year, NL-analytics around $150K, agent-assist around $60K, enterprise "
 "search around $40K — these are the entry points, before the agent engineers the buyer must also supply. Third, "
 "DataStaqAI's band sits below every one of those floors except GRC, where Sprinto already starts near $4K — which is "
 "exactly why our position in GRC is to compete on integration and evidence provenance rather than price, and everywhere "
 "else to lead with mid-market affordability plus delivery. The strategic point is that this is not 'we're cheaper'; it "
 "is 'we're priced for a segment the floor structurally excludes, and we deliver the outcome the cheaper SMB tools "
 "don't.' Caution the audience that seventeen of twenty-five use cases lack a cleanly published floor, so this chart is "
 "the disclosed subset, not the whole market — but the disclosed subset is consistent and one-directional. The next "
 "slide pairs this with the funding picture, which tells us where to avoid head-on competition and where to enter under "
 "the radar."))

# 26 — funding comparison (chart)
s=d.slide(fill=b.WHITE)
d.header(s,"Capital concentrated in Security and Customer — out-integrate, don't out-raise",
         "Where the venture money clusters tells us where NOT to fight head-on")
s.shapes.add_picture(str(A/"chart5_funding_by_cluster.png"),d.M,Inches(1.75),width=Inches(7.2))
pts=[("CONCENTRATION","Security ~$1.9B · Creative ~$1.2B · Customer ~$1.0B raised (disclosed, 42 vendors)"),
     ("VALUATION CEILING","Sierra $15.8B · Harvey $11B · Glean $7.2B — we ride on these, never out-build them"),
     ("THE PLAY","Capital ≠ delivery. Out-integrate the funded natives; compete on the layer they underfund")]
yy=2.0
for t,x in pts:
    d.rect(s,Inches(8.05),Inches(yy),Inches(4.65),Inches(1.4),b.SOFT,radius=0.05,shadow=True)
    d.text(s,t,Inches(8.25),Inches(yy+0.13),Inches(4.25),Inches(0.35),size=12,color=b.ACCENT,bold=True)
    d.text(s,x,Inches(8.25),Inches(yy+0.5),Inches(4.25),Inches(0.8),size=11,color=b.INK,shrink=True,ls=1.05)
    yy+=1.55
d.footer(s,26,46)
notes(s,("Close sub-iteration one with the funding picture, which answers a question every operator and investor asks: if "
 "this opportunity is real, why won't the well-funded AI-natives simply take it? The chart shows disclosed venture "
 "capital raised by cluster across the 42 named vendors in our base: Security at roughly $1.9B, Creative around $1.2B, "
 "Customer around $1.0B, with Employee, Code and Data lower. Read alongside the valuation ceiling — Sierra $15.8B, "
 "Harvey $11B, Glean $7.2B — the message is that capital has concentrated heavily in a few lanes, and those are exactly "
 "the lanes where trying to out-build or out-raise the natives would be suicidal. But here is the strategic inversion "
 "that makes the funding picture an argument FOR DataStaqAI rather than against it: capital is not delivery. The billions "
 "raised fund model and agent development and enterprise go-to-market; almost none of it funds mid-market integration and "
 "operation, because that work has services-like economics that venture-scale product companies actively avoid. So the "
 "concentration of capital tells us precisely where to NOT fight head-on (build a better support agent than Sierra) and "
 "where to enter under the radar (deliver that agent into a mid-market company Sierra won't sell to). The play is to "
 "out-integrate, not out-raise. Note the honest limit: 32 of 42 vendors disclose totals, so the bars are a disclosed "
 "floor, not a census — but the directional concentration is unambiguous. That completes the competitive picture's "
 "supply side. Sub-iteration two builds on it: the coverage heat map showing which functions each archetype actually "
 "serves, the explicit white-space analysis, the SWOT, the disruption matrix, why competitors stop short, and finally "
 "why DataStaqAI wins — the synthesis the whole chapter has been building toward."))

out=H/"DataStaqAI-Book-Ch4a-Competitive-A.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)
# spec
defs=[("19","Enterprise AI ecosystem — value migrating to the unowned delivery layer","4-layer stack diagram"),
      ("20","Market segmentation — the mid-market done-for-you cell is empty","2x2 segmentation grid"),
      ("21","Five competitor archetypes — each optimized away from the mid-market","5 archetype cards + DataStaqAI 6th"),
      ("22","Incumbents own distribution + SoR but can't disrupt the seat","Strengths/limits two-column"),
      ("23","AI-natives build the best agents, priced for the Fortune 500","Strengths/limits two-column + valuations"),
      ("24","The integrators that deliver serve only the Global 2000","SI vs DataStaqAI two-column"),
      ("25","Pricing bifurcated — DataStaqAI undercuts the floor","Price-floor chart + 3 callouts"),
      ("26","Capital concentrated in Security & Customer — out-integrate","Funding-by-cluster chart + 3 callouts")]
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 4 (a) — Competitive Analysis, Slides 19–26\n","Diagram-forward; headline · viz · 300w speaker notes. Figures source-traceable.\n"]
for (n,hl,vz),t in zip(defs,nt):
    spec+=[f"\n## Slide {n} — {hl}\n",f"**Recommended visualization.** {vz}\n",f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter4a-Competitive.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter4a-Competitive.md")
