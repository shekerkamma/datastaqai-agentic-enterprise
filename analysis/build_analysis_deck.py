#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN
from pathlib import Path

H = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/analysis")
d = Deck(footer="DataStaqAI · Competitive Analysis (AI-Analyst) · 2026")
b = d.b

def chart_slide(title, takeaway, img):
    s = d.slide(fill=b.WHITE)
    d.header(s, title, takeaway)
    d.picture_centered(s, str(H / img), top=Inches(1.7), width=Inches(10.6), max_bottom=Inches(7.0))
    return s

# cover
s = d.slide(fill=b.NAVY)
d.rect(s, d.W - Inches(0.22), 0, Inches(0.22), d.H, b.TEAL)
d.text(s, "COMPETITIVE ANALYSIS · AI-ANALYST PASS", d.M, Inches(1.6), Inches(11), Inches(0.4), size=15, color=b.TEAL, bold=True)
d.text(s, "Where DataStaqAI Plays —\nQuantified", d.M, Inches(2.2), Inches(11.4), Inches(1.8), size=44, color=b.WHITE, bold=True, shrink=True)
d.rect(s, d.M, Inches(4.35), Inches(2.0), Inches(0.06), b.TEAL)
d.text(s, "25 use cases · posture mix · price-floor gap · TAM · opportunity map", d.M, Inches(4.6), Inches(11), Inches(0.5), size=16, color=b.LIGHT_TEAL)

# method
s = d.slide(fill=b.WHITE)
d.header(s, "Method & validation", "Source-traceable, judgment labeled")
d.text(s, [{"text": t, "bullet": True, "space_before": 8, "size": 14} for t in [
    "Dataset: 25 use cases; figures traced to the 6 COMPETITIVE_*.md deep-research files. Blanks = no clean public figure (not zero).",
    "Tie-out: 25 use cases load (Customer 5 · Employee 5 · Creative 4 · Code 3 · Data 4 · Security 4).",
    "One unit error caught and removed: Salesforce CPQ $200 is per-seat/mo, not an annual floor.",
    "Competitive density is a judgment call from funding/competitor counts — not a measured index.",
]], d.M, Inches(1.8), d.CW, Inches(4.5), shrink=True)
d.footer(s, 2, 11)

chart_slide("Our motion is integration, not invention", "20 of 25 use cases are INTEGRATE+WORKFLOW; only 2 are BUILD", "chart1_posture_mix.png")
chart_slide("We sit below every incumbent floor but one", "Widest gaps: Legal $360K/yr and NL-Analytics $150K/yr", "chart2_price_floor_gap.png")
chart_slide("The biggest sourced markets aren't the crowded ones", "Travel, research, fraud, low-code dwarf the crowded agent lanes", "chart3_tam_by_usecase.png")
chart_slide("The two BUILD plays own the open lane", "Lowest density + owned-code outcome; rivals are Global-2000-only", "chart4_opportunity_map.png")
chart_slide("VC has concentrated in Security and Customer", "Security $1.9B, Creative $1.2B, Customer $1.0B raised — out-integrate, don't out-raise", "chart5_funding_by_cluster.png")
chart_slide("We don't out-build these valuations — we wire them in", "Sierra $15.8B, Harvey $11B, Glean $7.2B, Vanta $4.2B lead the agent-natives", "chart6_valuation_leaders.png")
chart_slide("Agent-natives carry rich multiples — the bubble we sell around", "High valuation per $ of ARR; the integration layer is the unfunded gap", "chart7_valuation_vs_arr.png")

# recommendation
s = d.slide(fill=b.NAVY)
d.rect(s, 0, 0, d.W, Inches(0.16), b.TEAL)
d.text(s, "Recommendation — where to play", d.M, Inches(0.5), d.CW, Inches(0.7), size=28, color=b.WHITE, bold=True)
d.rect(s, d.M, Inches(1.25), Inches(1.45), Inches(0.05), b.TEAL)
d.text(s, [{"text": t, "bullet": True, "space_before": 10, "size": 14, "color": b.LIGHT_TEAL} for t in [
    "Lead with the BUILD plays (#16 Legacy modernization, #17 Low-code escape): low density + owned-code outcome + competitors that skip the mid-market. Highest defensibility.",
    "In crowded REPLACE lanes (legal, conversational support, code review): don't out-agent the funded natives — win on mid-market price (below $40–360K floors) + integration + client owns the outcome.",
    "KEEP / enrichment lanes (SIEM, fraud, predictive ops, GRC, DAM): DEPLOY+TUNE for regulated buyers — 'make the investment you already made finally pay off.'",
    "Don't price-compete in GRC ($4K floor): anchor on integration + source-grounded evidence provenance.",
]], d.M, Inches(1.5), d.CW, Inches(5.0), shrink=True)
d.footer(s, 10, 11, dark=True)

# close
s = d.slide(fill=b.NAVY)
d.rect(s, 0, Inches(3.1), d.W, Inches(0.06), b.TEAL)
d.text(s, "Attention and market size are misaligned.\nThat gap is the integrator's opening.", d.M, Inches(2.4),
       Inches(12), Inches(1.5), size=30, color=b.WHITE, bold=True, align=PP_ALIGN.CENTER, shrink=True)
d.text(s, "DataStaqAI · done-for-you AI engineering · ~$2–5k/mo", d.M, Inches(4.5), Inches(12), Inches(0.5),
       size=15, color=b.LIGHT_TEAL, align=PP_ALIGN.CENTER)

out = H / "DataStaqAI-Competitive-Analysis-reviewed.pptx"
d.save(str(out))
print("OUTPUT:", out)
