#!/usr/bin/env python3
"""PART VII — Investment Thesis (slides 44–46). The close.
Renders branded .pptx with notes + spec. Validated on save."""
import sys
sys.path.insert(0,"/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path
H=Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
d=Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 7: Investment Thesis"); b=d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t
def band(s,y,txt,h=Inches(0.8),fill=None,col=None,size=14):
    d.rect(s,d.M,y,d.CW,h,fill or b.NAVY,radius=0.03)
    d.text(s,txt,d.M+Inches(0.25),y,d.CW-Inches(0.5),h,size=size,color=col or b.WHITE,bold=True,anchor=MSO_ANCHOR.MIDDLE,shrink=True)

# 44 — Why now
s=d.slide(fill=b.WHITE)
d.header(s,"Why now: demand, supply shock and price reset have converged — the window is 12–24 months",
         "Three forces are open simultaneously; they will not stay open")
cards=[("DEMAND","Agentic sub-markets compounding 10–25%/yr; 'wait and see' is over (58% of procurement already piloting AI)"),
       ("SUPPLY SHOCK","Incumbents forcing migrations — Salesforce CPQ End-of-Sale (6,000+ orgs); Claude legal plug-ins → ~$285B selloff"),
       ("PRICE RESET","Outcome pricing collapsing to $0.40–1.50/resolution — the question is now 'who makes it work,' not 'can we afford it'")]
xs=[Inches(0.6),Inches(4.66),Inches(8.72)]
for x,(t,txt) in zip(xs,cards):
    d.rect(s,x,Inches(2.0),Inches(3.9),Inches(2.7),b.SOFT,radius=0.05,shadow=True)
    d.rect(s,x,Inches(2.0),Inches(3.9),Inches(0.55),b.NAVY,radius=0.05)
    d.text(s,t,x+Inches(0.2),Inches(2.0),Inches(3.5),Inches(0.55),size=13.5,color=b.TEAL,bold=True,anchor=MSO_ANCHOR.MIDDLE)
    d.text(s,txt,x+Inches(0.22),Inches(2.75),Inches(3.5),Inches(1.85),size=12,color=b.INK,shrink=True,ls=1.07)
d.text(s,"↓        ↓        ↓",d.M,Inches(4.85),d.CW,Inches(0.4),size=16,color=b.TEAL,bold=True,align=PP_ALIGN.CENTER)
band(s,Inches(5.35),"THE WINDOW: in-market buyers + forced migrations + resetting prices = a 12–24-month opening to land the "
     "mid-market before the floors fall and the natives or SIs push down.",h=Inches(1.0),fill=b.GOLD,col=b.NAVY,size=14)
d.footer(s,44,48)
notes(s,("Open the investment thesis with timing, because 'why now' is the question that separates a real opportunity from "
 "a good idea that is early or late. Three independent forces are open at the same moment. Demand: the agentic "
 "sub-markets are compounding at ten to twenty-five percent a year and the 'wait and see' era is demonstrably over — "
 "fifty-eight percent of procurement organizations alone are already using or piloting AI, and similar adoption is "
 "visible across every function in Chapter 3. Supply shock: the incumbents themselves are forcing buyers into the "
 "market — Salesforce putting CPQ into End-of-Sale strands over six thousand organizations into a reimplementation "
 "decision, and Anthropic's Claude legal plug-ins erased roughly $285B of incumbent value in a single session, "
 "destabilizing installed bases across categories. A forced buyer is the best buyer a delivery firm can have. Price "
 "reset: outcome pricing is collapsing toward $0.40–1.50 per resolution, which flips the buyer's question from 'can we "
 "afford AI' to 'who will make it actually work in our environment' — and that second question is precisely what "
 "delivery answers. The strategic conclusion, in the gold window band, is that these three forces are open "
 "simultaneously now and will not stay open: as price floors keep falling and forced migrations peak, and as the "
 "AI-natives and SIs eventually look down-market, the uncontested window to land the mid-market is on the order of "
 "twelve to twenty-four months. The investment implication is urgency without recklessness: the path in Chapter 6 is "
 "capital-efficient, so the bet is not 'spend huge to capture a land grab' but 'move decisively now while the buyers "
 "are in motion and the position is uncontested.' That timing argument sets up the next slide — why DataStaqAI "
 "specifically is the team built to capture this window."))

# 45 — Why DataStaqAI
s=d.slide(fill=b.WHITE)
d.header(s,"Why DataStaqAI: the only team built to own the mid-market delivery layer",
         "Position + operating model + economics + a compounding moat — aligned to the exact gap")
pill=[("Category position, not a feature","Owns the empty mid-market done-for-you cell the other five archetypes structurally vacate"),
      ("Agent-native operating model","Delivers with the same tech it sells — OpenHands + subagents + thousands of MCPs — so it dogfoods its own leverage"),
      ("Capital-efficient by design","Services entry on a software trajectory: margin rises with library reuse; few logos + NRR>130% reach $5–10M"),
      ("A compounding moat","Reusable agent/connector library + embedding in the system of record raise switching cost and cut delivery cost over time")]
xs=[Inches(0.6),Inches(6.73)]; ys=[Inches(1.95),Inches(4.05)]
for i,(t,x) in enumerate(pill):
    cx=xs[i%2]; cy=ys[i//2]
    d.rect(s,cx,cy,Inches(5.95),Inches(1.9),b.SOFT,radius=0.05,shadow=True)
    d.rect(s,cx,cy,Inches(0.12),Inches(1.9),b.TEAL)
    d.text(s,t,cx+Inches(0.3),cy+Inches(0.16),Inches(5.4),Inches(0.5),size=14,color=b.NAVY,bold=True,shrink=True)
    d.text(s,x,cx+Inches(0.3),cy+Inches(0.74),Inches(5.4),Inches(1.05),size=12,color=b.INK,shrink=True,ls=1.06)
band(s,Inches(6.15),"The position, the tech, the economics and the moat all point at the same gap. That alignment — not any single "
     "feature — is why DataStaqAI is the team to own this layer.",h=Inches(0.9))
d.footer(s,45,48)
notes(s,("This slide answers 'why this team' by showing that four things align on the exact same gap — and alignment, not "
 "any one feature, is the investment case. First, category position: DataStaqAI owns the empty mid-market done-for-you "
 "cell that the other five archetypes structurally vacate, which is a place on the map rather than a feature a "
 "competitor can copy. Second, the operating model is agent-native: the company delivers using the very technology it "
 "sells — OpenHands with subagents and thousands of MCP integrations — so it dogfoods its own leverage and improves its "
 "delivery engine every time it ships a client, a compounding advantage a traditional SI or a non-technical managed "
 "provider cannot replicate. Third, it is capital-efficient by design: a services entry on a software trajectory, where "
 "gross margin rises as the reusable library matures and where few logos plus net revenue retention above 130% reach "
 "$5–10M — meaning the company can grow without venture-scale burn, which de-risks the investment. Fourth, the moat "
 "compounds: the reusable agent and connector library plus embedding in the customer's system of record simultaneously "
 "raise switching costs for customers and lower delivery costs for DataStaqAI, so the position strengthens with every "
 "engagement. The synthesis to land, in the band, is that the position, the technology, the economics and the moat all "
 "point at the same gap — that is the rare alignment that makes a company the natural owner of a category rather than "
 "one competitor among many. Be candid that execution risk remains real (the SWOT named it), but frame the bet "
 "precisely: this is not a wager on a single product winning a feature race; it is a wager on a team structurally "
 "positioned, technically equipped, and economically built to occupy a gap the funded field concedes. The final slide "
 "translates that into the headline outcome — why this becomes a $5–10M company."))

# 46 — Why $5–10M
s=d.slide(fill=b.NAVY)
d.rect(s,0,0,d.W,Inches(0.16),b.TEAL)
d.text(s,"Why this becomes a $5–10M company",d.M,Inches(0.55),d.CW,Inches(0.8),size=28,color=b.WHITE,bold=True)
d.rect(s,d.M,Inches(1.35),Inches(1.45),Inches(0.05),b.TEAL)
stats=[("~40–50","accounts at ~$120k/yr, reduced further by expansion, reach the $5–10M band"),
       ("NRR > 130%","growth comes mostly from within the base — the most capital-efficient growth there is"),
       ("50% → 70%","gross margin rising with library reuse: a services entry on a software trajectory"),
       ("12–24 mo","an open window against a gap the funded field structurally concedes")]
xs=[d.M,Inches(6.73)]; ys=[Inches(1.7),Inches(4.0)]
for i,(big,small) in enumerate(stats):
    cx=xs[i%2]; cy=ys[i//2]
    d.rect(s,cx,cy,Inches(5.95),Inches(2.0),b.NAVY_2,radius=0.05,shadow=True)
    d.text(s,big,cx+Inches(0.3),cy+Inches(0.2),Inches(5.4),Inches(0.8),size=30,color=b.GOLD,bold=True,shrink=True)
    d.text(s,small,cx+Inches(0.3),cy+Inches(1.0),Inches(5.4),Inches(0.9),size=12.5,color=b.LIGHT_TEAL,shrink=True,ls=1.06)
d.text(s,"A proven delivery role (systems integration for the agent era), repriced for the mid-market, on a "
         "capital-efficient, expansion-led path. The model commoditizes; the agent is funded; DataStaqAI owns the layer "
         "that turns them into outcomes.",d.M,Inches(6.2),d.CW,Inches(0.9),size=13.5,color=b.WHITE,bold=True,shrink=True)
d.footer(s,46,48,dark=True)
notes(s,("Close the book on the headline outcome, framed as arithmetic plus position rather than aspiration. The four "
 "numbers are the whole case. Roughly 40–50 accounts at about $120k a year reach the $5–10M band, and expansion reduces "
 "even that count — so this is not a business that needs hundreds of logos or a huge sales machine. Net revenue "
 "retention above 130% means growth comes mostly from within the installed base, which is the most capital-efficient "
 "growth there is and the reason the path does not require venture-scale funding. Gross margin rising from a "
 "services-like 50% toward a software-like 70% as the reusable library matures is the trajectory that makes the revenue "
 "valuable, not just large. And the 12–24-month window against a gap the funded field structurally concedes is the "
 "timing that makes now the moment. Tie it together with the closing statement, which is the thesis of the entire "
 "document compressed to three clauses: the model commoditizes, the agent is funded, and DataStaqAI owns the layer that "
 "turns them into outcomes — the mid-market delivery layer, a proven role (systems integration for the agent era) "
 "repriced and re-architected for a segment the incumbents, AI-natives and global SIs all leave open. Remind the "
 "audience that every claim was earned across the book: Chapters 1–2 established the shift and the timing, Chapter 3 "
 "mapped the function-level opportunity, Chapter 4 proved the white space and why competitors stop short, Chapters 5–6 "
 "showed the model and a capital-efficient path, and this chapter set the why-now, why-us and why-$5–10M. The ask, "
 "stated plainly to whatever audience is in the room — investor, partner, or hire — is to back the team building the "
 "delivery layer for the agent era while the window is open. End there: confident, evidence-backed, and specific."))

out=H/"DataStaqAI-Book-Ch7-Investment-Thesis.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)
defs=[("44","Why now — demand + supply shock + price reset; 12–24-mo window","3 force cards → gold window band"),
      ("45","Why DataStaqAI — position + operating model + economics + moat align","4 pillar cards"),
      ("46","Why $5–10M — capital-efficient, expansion-led, software trajectory","4 stat cards (navy) + close")]
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 7 — Investment Thesis (Slides 44–46)\n","The close. Headline · viz · 300w notes. Numbers illustrative.\n"]
for (n,hl,vz),t in zip(defs,nt):
    spec+=[f"\n## Slide {n} — {hl}\n",f"**Recommended visualization.** {vz}\n",f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter7-Investment-Thesis.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter7-Investment-Thesis.md")
