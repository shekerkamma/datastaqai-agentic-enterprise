#!/usr/bin/env python3
"""Chapter 1 — Executive Thesis (slides 1–5).
Single source of truth: defines slide content + speaker notes, renders a branded
.pptx WITH notes, and writes the companion markdown spec. Validated on save.
"""
import sys
sys.path.insert(0, "/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN
from pathlib import Path

H = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
H.mkdir(parents=True, exist_ok=True)
d = Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 1: Executive Thesis")
b = d.b

def notes(s, text):
    s.notes_slide.notes_text_frame.text = text

def card(s, x, y, w, h, title, lines, *, fill, tcol, bcol, tsize=13, bsize=11):
    d.rect(s, x, y, w, h, fill, radius=0.04, shadow=True)
    d.text(s, title, x+Inches(0.22), y+Inches(0.16), w-Inches(0.44), Inches(0.4), size=tsize, color=tcol, bold=True)
    d.text(s, [{"text":t,"bullet":True,"space_before":5,"size":bsize,"color":bcol} for t in lines],
           x+Inches(0.22), y+Inches(0.66), w-Inches(0.44), h-Inches(0.84), shrink=True, ls=1.06)

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — Title / thesis statement
s = d.slide(fill=b.NAVY)
d.rect(s, d.W-Inches(0.22), 0, Inches(0.22), d.H, b.TEAL)
d.text(s, "THE AGENTIC ENTERPRISE  ·  A STRATEGY BRIEF BY DATASTAQAI", d.M, Inches(0.95), Inches(11.5), Inches(0.4),
       size=14, color=b.TEAL, bold=True)
d.text(s, "From software-assisted work\nto AI-orchestrated work", d.M, Inches(1.7), Inches(11.6), Inches(1.9),
       size=40, color=b.WHITE, bold=True, shrink=True)
d.rect(s, d.M, Inches(3.95), Inches(2.2), Inches(0.06), b.TEAL)
d.text(s, "The value will accrue to whoever delivers the orchestration — not to the model, and not to the seat.",
       d.M, Inches(4.2), Inches(11.4), Inches(0.8), size=18, color=b.LIGHT_TEAL, shrink=True)
d.text(s, "Chapter 1 · Executive Thesis  |  Chapters: 1 Thesis · 2 Market Evolution · 3 Function Disruption · "
          "4 Competitive Intelligence · 5 White Space · 6 DataStaqAI · 7 Revenue · 8 Investment",
       d.M, Inches(6.3), Inches(12), Inches(0.7), size=11, color=b.MUTED, shrink=True)
notes(s, ("This document is a strategy brief, not a product pitch. Its job is to establish, in eight chapters, why a "
 "done-for-you AI engineering firm is positioned to capture disproportionate value as enterprises move from "
 "software-assisted workflows to AI-orchestrated ones. Open on the central claim: the enterprise software era "
 "organised work around seats — humans operating tools. The agentic era reorganises work around agents that operate "
 "the tools on the human's behalf. That is not a feature upgrade; it is a change in who, or what, does the "
 "orchestration. The strategic question every operator now faces is where the value accrues in that shift. Our "
 "thesis is that it does not accrue primarily to the foundation model (rapidly commoditising), nor to the legacy "
 "per-seat platform (defending, not disrupting). It accrues to whoever can deliver a working agent wired into the "
 "customer's systems of record, governed, and operated — the orchestration layer. Chapter 1 makes the thesis and "
 "quantifies the opening; Chapters 2–5 prove it with market, function, competitor and white-space evidence; "
 "Chapters 6–8 turn it into DataStaqAI's strategy, revenue path and investment case. Tell the audience what "
 "standard of proof to expect: every number in this deck is source-traceable to named vendors, funding rounds, "
 "pricing pages and analyst market sizings gathered in our competitive research base of 25 agentic use cases across "
 "six functional clusters and 40-plus named vendors. Where a figure is not publicly disclosed, the cell is left "
 "blank rather than estimated. Set the tone: this is a partner-level read, designed to change the decision in the "
 "room, not to survey the category."))

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 2 — The shift (transition)
s = d.slide(fill=b.WHITE)
d.header(s, "Every function is crossing the same line — from tools humans operate to agents that operate the tools",
         "The shift is synchronized across the enterprise, and the growth rates prove it is already underway")
# FROM card
card(s, d.M, Inches(1.9), Inches(5.2), Inches(2.9), "FROM — Software-assisted (per-seat SaaS)",
     ["Humans operate the tool; value billed per seat",
      "Deterministic rules, dashboards, playbooks, macros",
      "More work = more seats = linear cost",
      "Examples: help-desk seats, BI dashboards, SOAR playbooks, CPQ grids"],
     fill=b.SOFT, tcol=b.INK, bcol=b.INK)
d.text(s, "→", Inches(6.0), Inches(2.9), Inches(1.3), Inches(1.0), size=54, color=b.TEAL, bold=True, align=PP_ALIGN.CENTER)
# TO card
card(s, Inches(7.3), Inches(1.9), Inches(5.43), Inches(2.9), "TO — AI-orchestrated (agentic)",
     ["The agent operates the tools; value billed per outcome",
      "Reasoning over context; the agent decides the next step",
      "More work = more agent runs = decoupled from headcount",
      "Examples: autonomous tier-1 resolution, text-to-SQL, auto-remediation, conversational quoting"],
     fill=b.LIGHT_TEAL, tcol=b.ACCENT, bcol=b.INK)
d.rect(s, d.M, Inches(5.05), d.CW, Inches(1.5), b.NAVY, radius=0.03)
d.text(s, "STRATEGIC IMPLICATION", d.M+Inches(0.25), Inches(5.2), Inches(6), Inches(0.35), size=12, color=b.TEAL, bold=True)
d.text(s, "The seat is the unit being dismantled. Whoever re-orchestrates the work around agents — wired into the "
          "existing systems of record — captures the budget the seat used to hold.",
       d.M+Inches(0.25), Inches(5.55), d.CW-Inches(0.5), Inches(0.9), size=15, color=b.WHITE, shrink=True)
d.footer(s, 2, 5)
notes(s, ("This slide establishes the macro premise the rest of the document depends on: the transition from "
 "software-assisted to AI-orchestrated work is not a single-category event, it is happening across every enterprise "
 "function at once. Walk the audience left to right. On the left is the model that built the SaaS industry: a human "
 "sits in front of a tool and operates it, and the vendor charges per seat. The intelligence lives in the human; "
 "the software is a deterministic substrate of rules, dashboards, macros and playbooks. Critically, cost scales "
 "linearly — more work means more seats. On the right is the agentic model: the agent operates the tools on the "
 "human's behalf, reasoning over context to decide the next step, and value is increasingly billed per outcome "
 "(per resolution, per ticket, per investigation) rather than per seat. Cost decouples from headcount. The four "
 "examples on each side are deliberately drawn from different functions — support, data, security, sales — to make "
 "the point that this is synchronized, not isolated. Then bring the evidence: this is not speculative. The "
 "agentic sub-markets are compounding at rates that only happen when a transition is genuinely underway — the "
 "autonomous-SOC market at ~24.8% CAGR, AI customer-support at ~23.1%, AI code-review at ~20.2%, DAM and fraud in "
 "the mid-teens. Markets do not grow at those rates during incremental upgrades; they grow that way during "
 "platform shifts. Land the strategic implication at the bottom: the seat is the unit being dismantled. That is the "
 "single most important sentence in the chapter, because everything downstream — the competitive split, the "
 "white space, DataStaqAI's wedge — follows from it. Whoever re-orchestrates the work around agents, wired into "
 "the systems of record the enterprise already trusts, captures the budget the seat used to hold. Foreshadow the "
 "tension for slide 3: a shift this valuable attracts two very different kinds of players, and the way they "
 "compete leaves a structural gap."))

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 3 — The structural split + the hole
s = d.slide(fill=b.WHITE)
d.header(s, "Each category has split into two camps — and both price the mid-market out",
         "Incumbents defend the seat; AI-natives sell the agent enterprise-first. Neither serves the middle.")
card(s, d.M, Inches(1.9), Inches(5.9), Inches(2.7), "INCUMBENTS — defend the seat",
     ["Bolt AI onto the platform they already sell; won't cannibalise seat revenue",
      "Distribution + compliance are the moat",
      "Pricing stays per-seat / per-tier (e.g. Salesforce Revenue Cloud $200/seat)",
      "Outcome: AI as an add-on line item, not a re-architecture"],
     fill=b.NAVY, tcol=b.TEAL, bcol=b.LIGHT_TEAL)
card(s, Inches(6.73), Inches(1.9), Inches(6.0), Inches(2.7), "AI-NATIVES — sell the agent, enterprise-first",
     ["Best-in-class agents, but six-figure ACVs + dedicated agent engineers",
      "Valuations: Sierra $15.8B · Harvey $11B · Glean $7.2B · Decagon $4.5B · Vanta $4.15B",
      "Entry floors: Legal $360K · NL-analytics $150K · agent-assist $60K · search $40K /yr",
      "Outcome: the Fortune 500 wins; the mid-market is priced and staffed out"],
     fill=b.LIGHT_TEAL, tcol=b.ACCENT, bcol=b.INK)
d.rect(s, d.M, Inches(4.85), d.CW, Inches(1.7), b.GOLD, radius=0.03)
d.text(s, "THE HOLE — the mid-market", d.M+Inches(0.25), Inches(5.0), Inches(6), Inches(0.35), size=12, color=b.NAVY, bold=True)
d.text(s, "Companies too large for manual workflows but too small for $50–360K/yr agents and the engineers to run "
          "them. They can't afford the AI-native, won't get re-architected by the incumbent, and have no team to "
          "integrate either. That unserved middle is the entire opportunity of this document.",
       d.M+Inches(0.25), Inches(5.4), d.CW-Inches(0.5), Inches(1.0), size=14, color=b.NAVY, bold=True, shrink=True)
d.footer(s, 3, 5)
notes(s, ("This is the structural heart of the thesis, so spend time here. The claim is that in every one of the 25 "
 "agentic use cases we studied, the market has bifurcated into two camps that compete in opposite directions and, "
 "in doing so, leave the same gap. On the left, the incumbents — Zendesk, Salesforce, Splunk, Workday, OutSystems, "
 "Looker and their peers — bolt AI onto the seat they already sell. They cannot lead the disruption because their "
 "revenue is the seat; cannibalising it is structurally irrational. Their moat is distribution and compliance, and "
 "their AI shows up as an add-on line item (Salesforce's Revenue Cloud at $200/seat is the archetype), not a "
 "re-architecture of the work. On the right, the AI-natives build genuinely excellent agents — but they go to "
 "market enterprise-first. The valuations make the strategy explicit: Sierra at $15.8B, Harvey $11B, Glean $7.2B, "
 "Decagon $4.5B, Vanta $4.15B are priced for winner-take-most enterprise capture, and the published entry floors "
 "follow — $360K/yr for legal, $150K for NL-analytics, $60K for agent-assist, $40K for enterprise search, plus the "
 "requirement that the buyer supply dedicated agent engineers or accept forward-deployed teams. The result is that "
 "both camps optimise for the Fortune 500. Now land the gold band: the hole is the mid-market — companies too "
 "large to keep running manual workflows but too small to afford a $50–360K/yr agent and the engineers to operate "
 "it. They can't afford the AI-native, the incumbent won't re-architect them, and they have no internal team to do "
 "the integration. Emphasise that this is not a niche; it is the structural by-product of how the entire category "
 "competes. Every subsequent chapter quantifies and attacks this gap. Pre-empt the obvious objection — 'won't the "
 "AI-natives just move down-market?' — and preview slide 4's answer: when they try, they bolt on services, which "
 "proves the gap rather than closing it."))

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 4 — The white space is proven, not asserted
s = d.slide(fill=b.WHITE)
d.header(s, "The white space is proven, not asserted — the agent-natives have already conceded it",
         "Four independent signals show mid-market delivery is the unmet need, and the models punish wrappers, not fortresses")
cards=[("Managed tiers are appearing",
        ["Crescendo runs a BPO and bought PartnerHero's 3,000 CX staff",
         "Botpress & Maven ship 'Managed'; Decagon fields forward-deployed engineers; Sierra sells 6-figure services"]),
       ("The leading method needs a delivery layer",
        ["Mechanical Orchard (best-funded behavior-first modernizer) says its platform is 'built to be operated and delivered by system integrators'",
         "And it serves only the Global 2000 — the mid-market is explicitly out of scope"]),
       ("Models kill wrappers, not fortresses",
        ["Anthropic's Claude legal plug-ins triggered a ~$285B incumbent selloff…",
         "…yet the data-fortress moats (Thomson Reuters, Glean) held. Sell ON TOP of systems, never a thin wrapper"]),
       ("Price floors are collapsing — so 'cheap' and 'managed' are table stakes",
        ["$0.40–1.50 per resolution; $10/mo travel agents",
         "The defensible anchor is integration + workflow ownership + governance + the client owns the outcome"])]
xs=[d.M, Inches(6.73)]; ys=[Inches(1.95), Inches(4.35)]
for i,(t,ls) in enumerate(cards):
    card(s, xs[i%2], ys[i//2], Inches(5.9) if i%2==0 else Inches(6.0), Inches(2.2), t, ls,
         fill=b.SOFT, tcol=b.NAVY, bcol=b.INK, tsize=13.5, bsize=11)
d.footer(s, 4, 5)
notes(s, ("The most common failure of a 'white space' argument is that it is asserted rather than demonstrated. This "
 "slide demonstrates it with four independent signals, each from a different part of the market, so the conclusion "
 "is triangulated rather than narrative. First signal: the AI-natives themselves are bolting on managed and "
 "done-for-you tiers, which is what you do when buyers cannot operate your product alone. Crescendo went so far as "
 "to run a BPO and acquire PartnerHero's 3,000-person CX workforce; Botpress and Maven advertise 'Managed' tiers; "
 "Decagon fields forward-deployed engineers; Sierra attaches six-figure implementation services. If the product "
 "were truly self-serve for the mid-market, none of that would exist. Second signal: the best-funded company using "
 "the leading next-gen method — Mechanical Orchard in legacy modernization — explicitly states its platform is "
 "'built to be operated and delivered by system integrators,' and it serves only the Global 2000. The leading "
 "method therefore requires a delivery layer and ignores the middle by design. Third signal, and the most "
 "strategically important: when Anthropic shipped Claude legal plug-ins in early 2026, it wiped roughly $285B off "
 "incumbent software, financial-data and asset-management stocks in a single session — but the genuine data "
 "fortresses (Thomson Reuters' proprietary legal corpus, Glean's context graph) held their value. The lesson is "
 "precise: frontier models destroy thin wrappers, not systems with proprietary data and workflow. The strategic "
 "instruction that follows is to sell ON TOP of the customer's systems of record, never as a wrapper the next model "
 "release will eat. Fourth signal: price floors are collapsing toward $0.40–1.50 per resolution and $10/month "
 "travel agents, which means 'cheap' and even 'managed' are commoditising into table stakes. Close by stating the "
 "only defensible anchor that remains: integration depth, workflow ownership, governance, and the client owning "
 "the outcome. That is the position Chapter 6 will build DataStaqAI on."))

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 5 — DataStaqAI thesis + quantified opportunity
s = d.slide(fill=b.NAVY)
d.rect(s, 0, 0, d.W, Inches(0.16), b.TEAL)
d.text(s, "The opening is the mid-market integration gap — not another agent", d.M, Inches(0.5), d.CW, Inches(0.8),
       size=27, color=b.WHITE, bold=True, shrink=True)
d.rect(s, d.M, Inches(1.32), Inches(1.45), Inches(0.05), b.TEAL)
stats=[("20 / 25", "use cases are INTEGRATE+WORKFLOW — the job is wiring agents into systems of record, not building or reselling them"),
       ("$24–60K/yr", "DataStaqAI's band sits below every published incumbent floor but one (GRC) — the mid-market price wedge"),
       ("$1.9B vs $1.0B", "VC concentrated in Security & Customer — out-integrate, don't out-raise the funded natives"),
       ("2 BUILD plays", "Legacy modernization + low-code escape: lowest density, owned-code outcome, rivals are Global-2000-only")]
xs=[d.M, Inches(6.73)]; ys=[Inches(1.65), Inches(3.95)]
for i,(big,small) in enumerate(stats):
    x=xs[i%2]; y=ys[i//2]; w=Inches(5.9) if i%2==0 else Inches(6.0)
    d.rect(s, x, y, w, Inches(2.05), b.NAVY_2, radius=0.05, shadow=True)
    d.text(s, big, x+Inches(0.25), y+Inches(0.2), w-Inches(0.5), Inches(0.8), size=30, color=b.GOLD, bold=True, shrink=True)
    d.text(s, small, x+Inches(0.25), y+Inches(1.0), w-Inches(0.5), Inches(0.95), size=12.5, color=b.LIGHT_TEAL, shrink=True)
d.text(s, "DataStaqAI is the delivery layer for the agent era: we wire best-of-breed agents into your systems, own "
          "the workflow + governance, and run it — at mid-market price, with the client owning the outcome.",
       d.M, Inches(6.25), d.CW, Inches(0.8), size=14, color=b.WHITE, bold=True, shrink=True)
d.footer(s, 5, 5, dark=True)
notes(s, ("This slide converts the thesis into four numbers and states the company's position, closing Chapter 1 on "
 "evidence rather than rhetoric. Take each stat deliberately. Twenty of twenty-five use cases resolve to an "
 "INTEGRATE+WORKFLOW posture — meaning the repeatable job across the portfolio is not inventing agents (the funded "
 "natives already did) and not reselling licenses, but wiring best-of-breed agents into the customer's systems of "
 "record and owning the workflow around them. Only two use cases are pure BUILD and three are DEPLOY-and-tune; the "
 "shape of the work is integration. Second, the price wedge: DataStaqAI's $24–60K/yr band (roughly $2–5k per month) "
 "sits below every published incumbent entry floor except GRC, where Sprinto already starts near $4K — so in GRC we "
 "compete on provenance and integration, not price, and everywhere else the mid-market affordability gap is real "
 "and quantified. Third, capital concentration: disclosed VC raised clusters in Security (~$1.9B) and Customer "
 "(~$1.0B), which tells us precisely where NOT to try to out-build or out-raise the natives, and instead to "
 "out-integrate them. Fourth, the two BUILD plays — legacy modernization and low-code escape — sit alone in the "
 "low-competitive-density lane, their deliverable is owned code no vendor can hand the client, and their funded "
 "rivals serve only the Global 2000; these are the highest-defensibility entry points and where we lead. Then "
 "deliver the positioning line as the chapter's conclusion: DataStaqAI is the delivery layer for the agent era — "
 "we wire the agents in, own the workflow and governance, run it, price it for the mid-market, and the client owns "
 "the outcome. Hand off to Chapter 2: having established the thesis and the size of the opening, the next chapter "
 "traces the market evolution in depth — how each functional market is moving, how fast, and which segments cross "
 "the line first — so the reader can see the timing, not just the shape, of the opportunity."))

out = H / "DataStaqAI-Book-Ch1-Executive-Thesis.pptx"
d.save(str(out))
print("OUTPUT:", out, "| slides:", d.n)

# ── companion markdown spec (same source of truth) ────────────────────────────
md = H / "Chapter1-Executive-Thesis.md"
spec = []
spec.append("# Chapter 1 — Executive Thesis (Slides 1–5)\n")
spec.append("Production standard: insight headline · supporting analysis · evidence · visualization · speaker notes (300–500w). "
            "Figures source-traceable to the competitive research base (25 use cases, 40+ vendors).\n")
defs = [
 ("1","From software-assisted work to AI-orchestrated work — value accrues to whoever delivers the orchestration",
  "Frames the 8-chapter brief and the central claim.",
  "Eight agentic sub-markets growing 15–25% CAGR; 25 use cases / 40+ vendors researched.",
  "Title slide (navy), thesis statement + chapter map."),
 ("2","Every function is crossing the same line — from tools humans operate to agents that operate the tools",
  "The shift is synchronized across functions; cost decouples from seats.",
  "Autonomous-SOC ~24.8% CAGR, AI support ~23.1%, code-review ~20.2%; per-outcome pricing emerging.",
  "FROM→TO transition (two cards + arrow) + navy implication band."),
 ("3","Each category has split into two camps — and both price the mid-market out",
  "Incumbents defend the seat; AI-natives sell enterprise-first; the middle is unserved.",
  "Sierra $15.8B / Harvey $11B / Glean $7.2B / Vanta $4.15B; floors $40–360K/yr; 20/25 INTEGRATE.",
  "Two comparison cards (incumbents vs AI-natives) + gold 'the hole' band."),
 ("4","The white space is proven, not asserted — the agent-natives have already conceded it",
  "Four independent signals; models punish wrappers, not data fortresses.",
  "Crescendo+PartnerHero 3,000 staff; Mechanical Orchard 'operated by SIs'; ~$285B selloff; $0.40–1.50/resolution.",
  "Four evidence cards."),
 ("5","The opening is the mid-market integration gap — not another agent",
  "Thesis → four numbers + DataStaqAI's position.",
  "20/25 INTEGRATE; $24–60K/yr band; VC $1.9B (Security) vs $1.0B (Customer); 2 BUILD plays.",
  "Four gold stat cards (navy) + positioning line."),
]
notetexts=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
for (n,hl,an,ev,vz),nt in zip(defs,notetexts):
    spec.append(f"\n## Slide {n} — {hl}\n")
    spec.append(f"**Supporting analysis.** {an}\n")
    spec.append(f"**Evidence.** {ev}\n")
    spec.append(f"**Recommended visualization.** {vz}\n")
    spec.append(f"**Speaker notes.**\n\n{nt}\n")
md.write_text("\n".join(spec), encoding="utf-8")
print("SPEC:", md)
