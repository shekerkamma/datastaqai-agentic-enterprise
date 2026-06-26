#!/usr/bin/env python3
"""Competitive Battlecards — comprehensive sales-ready deck.
Framing + 5 archetype cards + 13 named-competitor cards + close. Validated on save."""
import sys
sys.path.insert(0,"/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path
H=Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
d=Deck(footer="DataStaqAI · Competitive Battlecards · 2026"); b=d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def band(s,y,txt,h=Inches(0.7),fill=None,col=None,size=13.5,sub=None):
    d.rect(s,d.M,y,d.CW,h,fill or b.NAVY,radius=0.03)
    d.text(s,txt,d.M+Inches(0.25),y+Inches(0.08),d.CW-Inches(0.5),Inches(0.5),size=size,color=col or b.WHITE,bold=True,shrink=True)
    if sub: d.text(s,sub,d.M+Inches(0.25),y+h-Inches(0.34),d.CW-Inches(0.5),Inches(0.3),size=10.5,color=col or b.LIGHT_TEAL,shrink=True)
def quad(s,x,y,w,h,title,lines,*,fill,tc,bc,traps=None):
    d.rect(s,x,y,w,h,fill,radius=0.05,shadow=True); d.rect(s,x,y,Inches(0.1),h,b.TEAL)
    d.text(s,title,x+Inches(0.26),y+Inches(0.12),w-Inches(0.45),Inches(0.35),size=11.5,color=tc,bold=True,shrink=True)
    runs=[{"text":t,"bullet":True,"space_before":4,"size":10.5,"color":bc} for t in lines]
    if traps: runs+=[{"text":"TRAPS: "+ " · ".join(traps),"size":10,"color":b.CORAL,"bold":True,"space_before":8}]
    d.text(s,runs,x+Inches(0.26),y+Inches(0.5),w-Inches(0.5),h-Inches(0.62),shrink=True,ls=1.04)
TOTAL=None
def battlecard(card,page):
    s=d.slide(fill=b.WHITE)
    d.header(s,card["name"],"Their pitch: “"+card["pitch"]+"”   ·   Archetype: "+card["tag"])
    quad(s,Inches(0.6),Inches(1.62),Inches(5.95),Inches(1.95),"THEY WIN ON",card["win"],fill=b.SOFT,tc=b.ACCENT,bc=b.INK)
    quad(s,Inches(6.73),Inches(1.62),Inches(6.0),Inches(1.95),"WHERE THEY STOP SHORT (mid-market)",card["short"],fill=b.SOFT,tc=b.CORAL,bc=b.INK)
    quad(s,Inches(0.6),Inches(3.67),Inches(5.95),Inches(1.95),"HOW WE WIN  (counter + proof)",card["counter"],fill=b.NAVY,tc=b.TEAL,bc=b.LIGHT_TEAL)
    quad(s,Inches(6.73),Inches(3.67),Inches(6.0),Inches(1.95),"DISCOVERY QUESTIONS",card["disco"],fill=b.SOFT,tc=b.NAVY,bc=b.INK,traps=card.get("traps"))
    band(s,Inches(5.78),"KILL POINT: "+card["kill"],h=Inches(0.95),fill=b.GOLD,col=b.NAVY,size=13.5,
         sub="Win when: "+card["winwhen"]+"     |     Lose when: "+card["losewhen"])
    d.footer(s,page,TOTAL)
    notes(s,card.get("notes",""))

# ── framing ──
def cover():
    s=d.slide(fill=b.NAVY); d.rect(s,d.W-Inches(0.22),0,Inches(0.22),d.H,b.TEAL)
    d.text(s,"COMPETITIVE BATTLECARDS",d.M,Inches(1.6),Inches(11),Inches(0.4),size=15,color=b.TEAL,bold=True)
    d.text(s,"How DataStaqAI Wins —\nArchetype by Archetype, Vendor by Vendor",d.M,Inches(2.2),Inches(11.6),Inches(1.8),size=38,color=b.WHITE,bold=True,shrink=True)
    d.rect(s,d.M,Inches(4.35),Inches(2.0),Inches(0.06),b.TEAL)
    d.text(s,"5 archetype cards · 13 named-competitor cards · discovery questions · objection handling",d.M,Inches(4.6),Inches(11),Inches(0.5),size=15,color=b.LIGHT_TEAL)
def howto():
    s=d.slide(fill=b.WHITE); d.header(s,"How to use these battlecards","One per archetype and per named competitor — built for the live call")
    d.text(s,[{"text":t,"bullet":True,"space_before":9,"size":13.5} for t in [
     "Each card: where they genuinely win · where they stop short for the mid-market · how WE win (counter + proof) · discovery questions to plant · the kill point.",
     "Golden rule: we RIDE the agents, we don't out-build them. Never enter a model or agent-quality bake-off.",
     "Always reframe to the unowned layer: integration + workflow + governance + operation, at mid-market price, client owns the outcome.",
     "Plant discovery questions early — they make the buyer surface the gap (who integrates? who operates? all-in cost? do you own the code?).",
     "Match the card to the buyer's incumbent; the kill point is the one line that flips the deal."]],
     d.M,Inches(1.8),d.CW,Inches(4.6),shrink=True)
    d.footer(s,2,TOTAL)
def matrix():
    s=d.slide(fill=b.WHITE); d.header(s,"The five archetypes at a glance","Their pitch · why they stop short · our one-line counter")
    cols=["Archetype","Their pitch","Stops short (mid-market)","Our counter"]
    rows=[["Incumbent Defender","'Stay on our platform, now with AI'","AI is an add-on, not a re-architecture","Wire the agent INTO their SoR + own the workflow"],
          ["AI-native Point Solution","'Buy our best-in-class agent'","6-figure floor + you supply the engineers","We deploy/integrate it FOR you, mid-market price"],
          ["Managed / BPO Hybrid","'We'll run it with our people'","Labor-cost economics; CX pocket","Software leverage, cross-function, you own assets"],
          ["Global Systems Integrator","'We'll run the transformation'","$1M+ / multi-quarter / Global-2000","Same role, mid-market price, weeks, you own code"],
          ["Horizontal Agent Platform","'Build your own agents'","Sells tools, not outcomes","We deliver the outcome on top of it"]]
    x0=Inches(0.6); cw=[Inches(2.6),Inches(3.2),Inches(3.3),Inches(3.0)]
    def cx(j): return Inches(0.6+sum(c.inches for c in cw[:j]))
    y=1.8; rh=0.5
    for j,c in enumerate(cols):
        d.rect(s,cx(j),Inches(y),cw[j],Inches(rh),b.NAVY)
        d.text(s,c,cx(j)+Inches(0.08),Inches(y),cw[j]-Inches(0.16),Inches(rh),size=11,color=b.WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    for r in rows:
        y+=rh
        for j,v in enumerate(r):
            fill=b.SOFT if (int((y-1.8)/rh))%2 else b.WHITE
            d.rect(s,cx(j),Inches(y),cw[j],Inches(0.78),fill)
            d.text(s,v,cx(j)+Inches(0.1),Inches(y),cw[j]-Inches(0.2),Inches(0.78),size=10.5,color=(b.NAVY if j==0 else b.INK),bold=(j==0),anchor=MSO_ANCHOR.MIDDLE,shrink=True)
        rh=0.78 if y>1.8 else rh
    d.footer(s,3,TOTAL)
def discovery():
    s=d.slide(fill=b.WHITE); d.header(s,"Universal discovery questions — make the buyer surface the gap","Ask these in any deal; the answers bias toward delivery + mid-market")
    qs=[("AFTER THE DEMO",["'Who integrates this into your systems — and who operates it after go-live?'","'What's the all-in cost including the engineers needed to run it?'"]),
        ("OWNERSHIP & FIT",["'At the end, do you own the code and the workflow — or rent the runtime?'","'Is it wired to YOUR process, or a generic agent you adapt?'"]),
        ("CAPACITY",["'Do you have an internal team to build, tune and maintain agents?'","'How long until the first real outcome — weeks or quarters?'"]),
        ("ECONOMICS",["'Is the price per-seat, per-resolution, or a 6-figure platform fee?'","'What happens to that cost as volume scales?'"])]
    xs=[Inches(0.6),Inches(6.73)]; ys=[Inches(1.9),Inches(4.05)]
    for i,(t,ls) in enumerate(qs):
        cx=xs[i%2]; cy=ys[i//2]
        quad(s,cx,cy,Inches(5.95) if i%2==0 else Inches(6.0),Inches(1.95),t,ls,fill=b.SOFT,tc=b.NAVY,bc=b.INK)
    band(s,Inches(6.15),"Every one of these answers points at the layer we own. Plant them early — let the buyer conclude the gap themselves.",h=Inches(0.85))
    d.footer(s,4,TOTAL)
def objections():
    s=d.slide(fill=b.WHITE); d.header(s,"Universal objection handling","The six objections you'll hear — and the response")
    cols=["Objection","Response"]
    rows=[["'Won't [incumbent] just ship this?'","They bolt AI on the seat they defend — it's an add-on, never the re-architecture. We wire the agent into their platform and own your workflow."],
          ["'Why not buy [AI-native] directly?'","You'd still supply the engineers and pay a 6-figure floor. We deliver the same agent wired in, at mid-market price."],
          ["'Aren't you just a consultancy?'","No — engineering economics: reusable agents + MCPs. Margin scales with reuse, not headcount; you own the outcome (and code)."],
          ["'What if the model/agent commoditizes?'","Good for us — we're model-agnostic and wire into your data. Every model improvement upgrades your outcome for free."],
          ["'We'll build it in-house'","Most mid-market teams lack the agent-eng capacity and the months. We deliver in weeks and hand you owned, governed code."],
          ["'You're small / unproven'","We're the SI for the agent era at your size — fixed-scope BUILD wins, owned code, references, and we're aligned with your systems, not replacing them."]]
    x0=Inches(0.6); cw=[Inches(4.0),Inches(8.13)]
    def cx(j): return Inches(0.6+sum(c.inches for c in cw[:j]))
    y=1.8
    for j,c in enumerate(cols):
        d.rect(s,cx(j),Inches(y),cw[j],Inches(0.45),b.NAVY); d.text(s,c,cx(j)+Inches(0.1),Inches(y),cw[j]-Inches(0.2),Inches(0.45),size=11,color=b.WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE)
    for i,r in enumerate(rows):
        y+=0.45 if i==0 else 0.78
        for j,v in enumerate(r):
            fill=b.SOFT if i%2 else b.WHITE
            d.rect(s,cx(j),Inches(y),cw[j],Inches(0.78),fill)
            d.text(s,v,cx(j)+Inches(0.12),Inches(y),cw[j]-Inches(0.24),Inches(0.78),size=10.5,color=(b.NAVY if j==0 else b.INK),bold=(j==0),anchor=MSO_ANCHOR.MIDDLE,shrink=True)
    d.footer(s,5,TOTAL)

ARCH=[
{"name":"Incumbent Defender","tag":"Incumbent","pitch":"Stay on the platform you already own — now with AI.",
 "win":["Distribution, installed base, procurement trust","Owns the system of record + compliance","AI is a low-friction add-on to a contract you have"],
 "short":["AI is an add-on, not a re-architecture — it won't kill the seat","Slow committee roadmaps; per-seat pricing preserved","Generic; not wired to YOUR workflow or data"],
 "counter":["We wire the agent INTO their platform — additive, not rip-replace","We own the client-specific workflow + governance they won't build","Outcome-priced, live in weeks"],
 "disco":["'How much time does their AI add-on actually save your team?'","'Who makes it work inside your workflow?'"],
 "traps":["Don't attack the SoR — you partner with it","Don't say 'rip and replace'"],
 "kill":"Their AI defends the seat; ours removes the work — and makes their platform finally deliver.",
 "winwhen":"buyer keeps the SoR but the add-on underdelivers","losewhen":"buyer wants zero new vendors / one throat to choke",
 "notes":"Coaching: never fight the incumbent on distribution. Concede it, then move the conversation to the workflow the add-on doesn't touch. Position yourself as the layer that makes their existing investment pay off — you're the incumbent's friend, not its rival."},
{"name":"AI-native Point Solution","tag":"AI-native","pitch":"Buy our best-in-class agent.",
 "win":["Best agent quality + shipping velocity","Category brand + deep capital","Strong fit for large enterprises with eng teams"],
 "short":["6-figure floors + you must supply agent engineers","Sits on a SEPARATE tool → integration TCO lands on you","Wrapper-risk where no data moat; mid-market not served"],
 "counter":["We deploy/INTEGRATE the best-of-breed agent FOR you — often theirs","Mid-market price; no agent-eng team required","We own the integration + governance they push back to you"],
 "disco":["'Who integrates and operates it after the demo?'","'What's the all-in cost incl. the engineers to run it?'"],
 "traps":["Don't claim a better agent — you ride theirs","Never enter a model bake-off"],
 "kill":"Great agent, no delivery. We're how the mid-market actually gets it running.",
 "winwhen":"buyer is sub-enterprise / lacks an agent-eng team","losewhen":"Fortune-500 with an in-house AI platform team",
 "notes":"Coaching: praise the agent sincerely — you may deploy it. The wedge is everything after the demo. Make the buyer compute the all-in cost (license + integration + the engineers to operate it) and the gap appears on its own."},
{"name":"Managed / BPO Hybrid","tag":"Managed/BPO","pitch":"We'll run it for you — with our people.",
 "win":["Done-for-you (the right instinct)","Human escalation coverage","Proves the mid-market wants delivery"],
 "short":["Labor-cost scaling caps margin and price","People, not engineering leverage → less defensible","CX-pocket focused, not cross-function"],
 "counter":["Engineering economics (agents + MCPs), not bodies → better price + scale","Cross-function (finance, security, eng), not one pocket","Client owns the outcome and the reusable assets"],
 "disco":["'Is this software leverage or outsourced headcount?'","'Does it span beyond support — finance, security, eng?'"],
 "traps":["Acknowledge their model validates yours — don't dismiss done-for-you"],
 "kill":"They scale with people; we scale with software — same outcome, better economics.",
 "winwhen":"buyer wants outcomes beyond CX at software margins","losewhen":"pure CX-volume play that wants humans-in-the-loop now",
 "notes":"Coaching: Crescendo et al. are your strongest 'the white space is real' proof — use them to validate the category, then differentiate on economics (software vs labor) and breadth (cross-function vs CX)."},
{"name":"Global Systems Integrator","tag":"Global SI","pitch":"We'll run the transformation.",
 "win":["Real delivery capability + enterprise trust","Scale, brand, change management"],
 "short":["$1M+ engagements, multi-quarter timelines","Built for the Global 2000, not the mid-market","Billable-hours economics; you may not own the IP/code"],
 "counter":["Same delivery role at mid-market price ($2–5k/mo), weeks not quarters","Engineering economics, not billable armies","Client OWNS the code (BUILD plays)"],
 "disco":["'What's the floor on their engagement and the timeline?'","'Do you own the code at the end?'"],
 "traps":["Don't claim Big-SI scale — claim speed + price + ownership for your size"],
 "kill":"The SIs do exactly this — for the Global 2000. We're the SI for the mid-market.",
 "winwhen":"mid-market buyer priced out of an SI","losewhen":"buyer needs global scale + brand cover for the board",
 "notes":"Coaching: the SI is your most flattering comparison — cite that the leading method (Mechanical Orchard) is 'built to be operated by SIs.' You're not a new category; you're a proven role, repriced for a segment the SI can't economically serve."},
{"name":"Horizontal Agent Platform","tag":"Horizontal platform","pitch":"Build your own agents on our platform.",
 "win":["Flexible primitives + many connectors","Good for teams with real engineering capacity"],
 "short":["Sells tools, not outcomes — delivery is YOUR problem","Needs in-house builders the mid-market lacks","Long time-to-value; maintenance on you"],
 "counter":["We deliver the outcome on top of it — sometimes building ON it","No internal build team required","We own build + run; you get the result"],
 "disco":["'Who builds and maintains the agents — with what team?'","'What's your time to first real outcome?'"],
 "traps":["Don't disparage the platform — you may build on it"],
 "kill":"A toolkit isn't an outcome. We turn the platform into a running result.",
 "winwhen":"buyer has no internal agent builders","losewhen":"buyer has a strong platform team that wants to DIY",
 "notes":"Coaching: position the platform as a supplier, not a rival. Your value is the delivery the toolkit explicitly leaves to the customer."},
]
NAMED=[
{"name":"Sierra","tag":"AI-native · CX","pitch":"The premium enterprise CX agent.",
 "win":["Top agent quality; Bret Taylor brand","~$15.8B valuation, Fortune-50 logos"],
 "short":["~$150K+ floor + multi-month, services-led rollout","Requires a separate helpdesk → integration TCO on you"],
 "counter":["We deploy a resolution agent wired to YOUR helpdesk, per-ticket","Mid-market price; bootstrapped off your ticket history"],
 "disco":["'What's the all-in with implementation services?'","'Who operates it after the six-figure rollout?'"],
 "traps":["Don't knock the agent — knock the price/fit for your size"],
 "kill":"Built for the Fortune 50. You shouldn't pay $150K + an implementation team to resolve tier-1.",
 "winwhen":"sub-enterprise CX team without agent engineers","losewhen":"large consumer brand wanting a marquee vendor",
 "notes":"Sierra is the valuation bellwether — concede excellence, win on price + fit + speed for the mid-market."},
{"name":"Decagon","tag":"AI-native · CX","pitch":"Enterprise agentic CX with forward-deployed engineers.",
 "win":["Strong autonomy + workflow depth; $4.5B val","Forward-deployed engineers = real delivery"],
 "short":["$50K platform fee + per-conv; Vendr median ~$386K","FDE model = enterprise economics, not mid-market"],
 "counter":["We're the FDE model at mid-market price, on your helpdesk","Per-ticket, no platform floor"],
 "disco":["'What's the platform fee before usage?'","'Is the FDE team included or extra?'"],
 "traps":["Don't model-bake-off; win on economics + segment"],
 "kill":"Their FDE model proves delivery matters — we bring it to companies their floor excludes.",
 "winwhen":"mid-market priced below their platform fee","losewhen":"enterprise wanting Decagon's brand + FDEs",
 "notes":"Decagon's own FDE motion is your proof that delivery is the need; you simply serve the segment their economics skip."},
{"name":"Zendesk / Intercom Fin","tag":"Incumbent · CX","pitch":"Native AI inside the helpdesk you already run.",
 "win":["Native to the helpdesk; low friction; Fin's resolution rate","Distribution + trust"],
 "short":["Per-resolution + add-on sprawl; AI cold-start (1,000+ tickets)","Generic; not wired to your back-end actions/workflow"],
 "counter":["We wire a resolution agent + back-end actions into the same helpdesk","No cold-start (bootstrapped on your history); own the workflow"],
 "disco":["'What's the AI bill once resolutions stack up?'","'Does it take actions in your other systems, or just answer?'"],
 "traps":["Partner with the helpdesk — don't try to replace it"],
 "kill":"Their bot answers; our agent acts across your systems — on the helpdesk you keep.",
 "winwhen":"buyer on Zendesk/Intercom wanting cross-system action","losewhen":"buyer happy with native deflection only",
 "notes":"This is an additive play — you make their helpdesk investment do more, not less."},
{"name":"Glean","tag":"AI-native · Enterprise search","pitch":"Work AI search across all your tools.",
 "win":["Strong cross-app search; $7.2B val, $300M ARR","Former-Google search pedigree"],
 "short":["~$40K/yr floor; 2-week implementation; can't trial on your corpus","Answer quality wavers on stale/poorly-tagged data → adoption drops"],
 "counter":["ACL-respecting agent over your stack, trial-able on YOUR corpus","SMB pricing; we own the governed-context layer that drives quality"],
 "disco":["'Can you test it on your own data before signing?'","'Who maintains the source quality the answers depend on?'"],
 "traps":["Don't claim better retrieval tech — claim fit, price, governed context"],
 "kill":"Priced for thousands of seats; you want answers on your data at your size, tested first.",
 "winwhen":"sub-200-person org priced out of Glean","losewhen":"large enterprise wanting the category brand",
 "notes":"Lead with the governed-context angle — the layer that makes search accurate is exactly what we own and they push onto you."},
{"name":"Harvey","tag":"AI-native · Legal","pitch":"BigLaw-grade legal AI.",
 "win":["Strong research/draft quality; $11B val, $300M ARR","AmLaw brand + adoption"],
 "short":["$1,200–2,000/seat, ~$360K entry → priced for BigLaw","Hallucination/citator risk still needs governance"],
 "counter":["Citator-verified research/draft agent for the mid-firm","Mid-firm price + AI-use governance; corpus kept as hybrid"],
 "disco":["'What's the per-seat all-in for a 100-attorney firm?'","'Who's accountable if a citation is wrong in court?'"],
 "traps":["Don't claim to beat Harvey's depth — win on price + verification + segment"],
 "kill":"A $20 tool matches a $270 seat — but one fake cite gets you sanctioned. We deliver the verified, governed version at mid-firm price.",
 "winwhen":"45–250-attorney firm priced out of Harvey","losewhen":"AmLaw-100 firm standardizing on Harvey",
 "notes":"Verification + governance is the wedge — it's where the mid-firm's real fear (sanctions) lives."},
{"name":"Vanta / Drata","tag":"AI-native · GRC","pitch":"Automated compliance + continuous control monitoring.",
 "win":["Mature evidence automation; Vanta $4.15B/$300M ARR","Broad integrations; fast first SOC 2"],
 "short":["Floors near $4K (Sprinto) → don't compete on price here","'Automated' evidence is often organized manual work that breaks silently; doesn't replace a program"],
 "counter":["Source-grounded evidence agent with real provenance + integration","We wire it to YOUR systems and own the workflow they leave to you"],
 "disco":["'When an integration token expires, who notices before the auditor?'","'Is your evidence truly source-generated or uploaded screenshots?'"],
 "traps":["Don't undercut on license — win on provenance + integration"],
 "kill":"They give you a dashboard; we give you evidence that's source-true and never silently breaks.",
 "winwhen":"buyer burned by evidence gaps / failed-audit risk","losewhen":"startup just wants the cheapest SOC-2 checkbox",
 "notes":"GRC is the one lane NOT to price-compete — anchor entirely on provenance, integration and 'doesn't replace a program.'"},
{"name":"Prophet / Torq","tag":"AI-native · SecOps","pitch":"Autonomous SOC / SOAR replacement.",
 "win":["Real autonomous investigation; Torq $1.2B; Tines $1.1B","Strong enterprise + MSSP traction"],
 "short":["Enterprise deployments need a team to stand up + tune","Mid-market + smaller MSSPs can't run it alone"],
 "counter":["We DEPLOY+TUNE the agent on your existing SIEM, end to end","Often self-funds via SIEM-ingest reduction; we own correlation"],
 "disco":["'Do you have the team to deploy and tune this yourselves?'","'What's your SIEM ingest bill — could the agent cut it?'"],
 "traps":["Don't claim a better SOC agent — you deploy theirs"],
 "kill":"You're hiring L1s to triage alerts an agent can investigate — we stand it up and tune it, often paying for itself in SIEM cuts.",
 "winwhen":"mid-market SOC/MSSP hiring L1, no deployment team","losewhen":"large SOC with its own detection engineers",
 "notes":"SOC-analyst job posts are the lead list; lead with the self-funding SIEM-cost angle."},
{"name":"CodeRabbit / Greptile","tag":"AI-native · Code review","pitch":"AI code review in your PRs.",
 "win":["Cheap ($24/mo), viral, benchmark-leading","Easy GitHub install"],
 "short":["Noise/rubber-stamp at scale without tuning + gating","It's a tool, not a delivery — value depends on workflow fit"],
 "counter":["We DEPLOY+TUNE it at commit-time with the right gates + conventions","An attach to a bigger BUILD/INTEGRATE engagement"],
 "disco":["'Is the bot's noise training your team to rubber-stamp?'","'Who tunes it to your conventions?'"],
 "traps":["Don't try to sell against a $24 tool head-on — attach it to delivery"],
 "kill":"The tool is cheap; making it signal-not-noise is the work — and that's delivery, which we do.",
 "winwhen":"as an attach inside an eng engagement","losewhen":"buyer just wants the cheap PR bot, standalone",
 "notes":"Don't lead with code review — it's a low-margin attach. Use it to widen an Engineering BUILD deal."},
{"name":"OutSystems / Mendix","tag":"Incumbent · Low-code","pitch":"Build apps fast on our low-code platform.",
 "win":["Fast initial delivery; large installed base","Governance + scale for what they cover"],
 "short":["Lock-in: logic in proprietary XML; bill balloons; no export-to-code","Re-pricing forces costly migrations; talent siloing"],
 "counter":["BUILD: reverse-engineer the estate into OWNED React/Node in months","No runtime rent; you keep the code + add the AI layer they block"],
 "disco":["'Does your low-code bill now exceed your eng payroll?'","'Could you add the AI features you need inside the platform?'"],
 "traps":["This is a BUILD play — sell owned-code outcome, not a subscription"],
 "kill":"You adopted low-code for speed and woke up in a cage. We get you out — into code you own — in a quarter.",
 "winwhen":"3+ yrs in, re-priced, AI-blocked","losewhen":"happy, stable, low-volume internal apps (a KEEP)",
 "notes":"The sharpest BUILD wedge — lead Engineering deals here; deliverable is owned code no vendor can hand them."},
{"name":"Rossum / Esker","tag":"AI-native · IDP/Finance","pitch":"AI document/invoice automation.",
 "win":["Template-free VLM extraction; mature AP suites","Strong for whole-suite adopters"],
 "short":["Whole-suite consolidation tax; off-suite ERPs underserved","Tool extracts; the other 90% (match/post/approve/audit) is yours"],
 "counter":["No-template AP agent wired into YOUR Dynamics/SAP/Oracle","We own 3-way match, posting, approval, audit — rescue a failed OCR"],
 "disco":["'Did a prior OCR choke on half your vendor formats?'","'Who does the 3-way match and ERP posting today?'"],
 "traps":["Don't out-claim extraction accuracy — own the full workflow"],
 "kill":"OCR reads characters; we do the other 90% — wired into the ERP you already run.",
 "winwhen":"off-suite mid-market mfr/distributor, failed prior OCR","losewhen":"company standardizing on a full AP suite",
 "notes":"'Rescue the failed OCR rollout' is the highest-intent opener in Finance."},
{"name":"Ramp","tag":"AI-native · Finance","pitch":"All-in-one finance ops + AI accounting agent.",
 "win":["$44B, Accounting Agent, 70k customers; huge momentum","Real close automation on its own platform"],
 "short":["Value concentrated in the Ramp ecosystem (cards/spend)","Doesn't re-architect YOUR existing ERP/close across diverse systems"],
 "counter":["ERP-agnostic close/reconciliation agent wired to your stack","We own cross-system workflow for non-Ramp finance estates"],
 "disco":["'Are you ready to move spend onto Ramp to get the agent?'","'Who automates close across your existing ERP + tools?'"],
 "traps":["Ramp is strong — target the non-Ramp ERP estate, don't fight head-on"],
 "kill":"Ramp automates the Ramp world; we automate the close across the ERP you already run.",
 "winwhen":"mid-market not adopting Ramp's full ecosystem","losewhen":"company happy to consolidate onto Ramp",
 "notes":"Don't fight Ramp's momentum — serve the finance estates that won't re-platform onto it."},
{"name":"Zip / Coupa","tag":"Procurement","pitch":"Intake-to-pay procurement orchestration.",
 "win":["Zip $371M, 50+ agents; Coupa $9.5T data + Navi","Strong enterprise orchestration"],
 "short":["Enterprise-first, configuration-heavy; rip-replace to adopt","Mid-market wants orchestration without a new suite"],
 "counter":["Wire an intake→approval→sourcing agent across existing systems","Own the approval orchestration + policy guardrails; no suite swap"],
 "disco":["'Do you want to replace Coupa/Ariba — or just fix the messy middle?'","'Who orchestrates approvals across legal/finance/risk today?'"],
 "traps":["Don't sell a suite — sell the orchestration layer on top"],
 "kill":"You don't need a new procurement suite — you need the messy middle orchestrated. That's us.",
 "winwhen":"mid-market wanting orchestration sans rip-replace","losewhen":"enterprise standardizing on Zip/Coupa/Ariba",
 "notes":"Lead with 'fix the messy middle' — agents across the systems they keep."},
{"name":"ServiceNow / Moveworks","tag":"Incumbent · Operations","pitch":"Autonomous workforce / employee-support AI.",
 "win":["ServiceNow Autonomous Workforce + Moveworks; huge scale","Out-of-box L1 service-desk specialist; deep ITSM"],
 "short":["Enterprise ITSM scale + cost; heavy to deploy","Mid-market can't run a Moveworks-scale deployment alone"],
 "counter":["DEPLOY+TUNE the right agent on your existing ITSM/sensor stack","KEEP/enrichment framing — make the investment finally pay off"],
 "disco":["'Are you on ServiceNow at enterprise scale — or something lighter?'","'Who deploys and tunes this for your team size?'"],
 "traps":["Don't fight ServiceNow's scale — serve the lighter mid-market estate"],
 "kill":"Their autonomous workforce is built for 200M-employee scale; we deliver it at yours.",
 "winwhen":"mid-market ops on lighter ITSM, no deployment team","losewhen":"large ServiceNow shop going all-in on Now AI",
 "notes":"KEEP/enrichment framing for regulated, risk-averse ops buyers — ride the data, fix the workflow."},
]
def close():
    s=d.slide(fill=b.NAVY); d.rect(s,0,0,d.W,Inches(0.16),b.TEAL)
    d.text(s,"The 3 questions that flip almost any deal",d.M,Inches(0.55),d.CW,Inches(0.8),size=26,color=b.WHITE,bold=True)
    d.rect(s,d.M,Inches(1.35),Inches(1.45),Inches(0.05),b.TEAL)
    qs=[("1 · Who operates it?","After the demo, who integrates, tunes and runs it — and with what team? (They don't have one.)"),
        ("2 · What's the all-in?","License + integration + the engineers to run it — vs our $2–5k/mo, outcome-priced."),
        ("3 · Who owns the result?","Do you own the code, the workflow, the outcome — or rent a runtime / a seat?")]
    xs=[d.M,Inches(6.73)]; ys=[Inches(1.65),Inches(3.55)]
    for i,(t,x) in enumerate(qs):
        cx=xs[i%2]; cy=ys[i//2]
        d.rect(s,cx,cy,Inches(5.95),Inches(1.75),b.NAVY_2,radius=0.05,shadow=True); d.rect(s,cx,cy,Inches(0.12),Inches(1.75),b.TEAL)
        d.text(s,t,cx+Inches(0.3),cy+Inches(0.16),Inches(5.4),Inches(0.5),size=15,color=b.GOLD,bold=True,shrink=True)
        d.text(s,x,cx+Inches(0.3),cy+Inches(0.72),Inches(5.4),Inches(0.9),size=12.5,color=b.LIGHT_TEAL,shrink=True,ls=1.06)
    d.rect(s,Inches(6.73),Inches(3.55),Inches(6.0),Inches(1.75),b.GOLD,radius=0.05,shadow=True)
    d.text(s,"THE THROUGHLINE",Inches(7.0),Inches(3.7),Inches(5.5),Inches(0.4),size=12,color=b.NAVY,bold=True)
    d.text(s,"We ride the agents, we don't out-build them. We win on delivery, mid-market price, and owned outcomes — the layer every competitor leaves to you.",
           Inches(7.0),Inches(4.1),Inches(5.5),Inches(1.05),size=12.5,color=b.NAVY,bold=True,shrink=True)
    d.text(s,"DataStaqAI · the delivery layer for the agent era",d.M,Inches(6.4),d.CW,Inches(0.5),size=13,color=b.LIGHT_TEAL,align=PP_ALIGN.CENTER)

TOTAL=5+len(ARCH)+len(NAMED)+1
cover(); howto(); matrix(); discovery(); objections()
page=6
for c in ARCH: battlecard(c,page); page+=1
for c in NAMED: battlecard(c,page); page+=1
close()
out=H/"DataStaqAI-Competitive-Battlecards.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n,"| TOTAL const:",TOTAL)
