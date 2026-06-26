# Competitive Analysis — Findings (AI-Analyst pass)

**Question:** Across the 25 agentic use cases, where should DataStaqAI play, and what quantifies the positioning?
**Dataset:** `competitive_dataset.csv` (25 use cases), figures traced to the 6 `COMPETITIVE_*.md` deep-research files. Blanks = no clean public figure (not zero). **Competitive density is labeled judgment, not measured.** Charts in this folder.

## Validation / tie-out
- 25 use cases load cleanly: Customer 5 · Employee 5 · Creative 4 · Code 3 · Data 4 · Security 4.
- Posture mix: **INTEGRATE+WORKFLOW 20 · DEPLOY+TUNE 3 · BUILD 2.**
- Pattern mix: **REPLACE 10 · RENEGOTIATE 9 · KEEP 6.**
- Enterprise floors with published figures: 8 of 25 ($4K–$360K/yr). One unit error caught & removed (CPQ $200 is per-seat/mo, not an annual floor).

## Finding 1 — The motion is integration, not invention (chart 1)
**20 of 25 use cases are INTEGRATE+WORKFLOW; only 2 are BUILD.** DataStaqAI's repeatable job is wiring best-of-breed agents into the client's systems of record and owning the workflow — not building agents from scratch (the funded natives already did) and not reselling licenses. The 2 BUILD plays are the exception that matters: they're the only places the deliverable is **owned code** no vendor can hand the client.

## Finding 2 — We sit below every incumbent floor but one (chart 2)
Of the 8 use cases with published enterprise floors, DataStaqAI's **$24–60K/yr band ($2–5k/mo)** is *below* all but GRC. The widest gaps — where "priced out of the enterprise tool" is the sharpest wedge — are **Legal ($360K/yr)** and **NL Analytics/Text-to-SQL ($150K/yr)**, then Agent-Assist ($60K), Conversational Support ($50K), HR ($48K), Enterprise Search ($40K), SIEM ($36K). **Exception: GRC floors at ~$4K (Sprinto)** — do **not** price-compete there; win on integration + evidence provenance.

## Finding 3 — The biggest sourced markets aren't the crowded ones (chart 3)
Sourced 2025 TAMs span **$1.8B (code review) → $165.9B (AI-in-travel), $140B (market research), $32B (fraud), $26.9B (low-code).** The largest sourced markets (travel, market research, fraud, low-code) are *not* the most VC-saturated agent lanes (conversational support, legal, code review) — i.e. attention and market size are misaligned, which is where an integrator can enter under the radar.

## Finding 4 — The two BUILD plays own the open lane (chart 4)
On the density × pattern map, **Legacy Modernization (#16) and Low-code Escape (#17) sit alone in the low-density column** — lowest competition, and their funded challengers (Mechanical Orchard, Replay, vFunction) are explicitly **Global-2000-only**. Combined sourced TAM **$7.9B + $26.9B**, and the outcome is owned code. This is the highest-defensibility entry point in the portfolio.

## Recommendation — where to play
1. **Lead with the BUILD plays (#16, #17):** low density + owned-code outcome + competitors that skip the mid-market. Highest defensibility.
2. **In crowded REPLACE lanes (legal, conversational support, code review):** don't try to out-agent the funded natives. Win on **mid-market price (below their $40–360K floors) + integration + the client owns the outcome.**
3. **KEEP / enrichment lanes (SIEM, fraud, predictive ops, GRC, DAM):** DEPLOY+TUNE for regulated, risk-averse buyers; lead with "make the investment you already made finally pay off."
4. **Don't price-compete in GRC ($4K floor):** anchor on integration + source-grounded evidence provenance, not license undercutting.

## Honest limits
- 17 of 25 use cases lack a clean public enterprise floor, and ~half lack a single-source TAM; those cells are blank, not estimated.
- Density is a judgment call from funding/competitor counts in the research, not a measured index.
- Vendor-level funding/valuation figures live in the `COMPETITIVE_*.md` files (per-vendor, sourced); this pass aggregates at the use-case level.

## Vendor-level findings (chart 5–7)
- **Funding concentration (chart 5):** disclosed VC raised by cluster — **Security $1.9B · Creative $1.2B · Customer $1.0B · Employee $0.5B · Code $0.37B · Data $0.36B** (42 vendors; 32 with disclosed totals). The most-capitalized lanes (Security, Customer) are where you *out-integrate*, not out-raise.
- **Valuation leaders (chart 6):** the agent-natives DataStaqAI rides on top of, not against — **Sierra $15.8B · Harvey $11B · Glean $7.2B · Decagon $4.5B · Vanta $4.15B** (incumbents Canva $42B, OutSystems $9.5B, Retool $3.2B shown grey).
- **Valuation vs ARR (chart 7):** rich revenue multiples across the board (e.g., Sierra $15.8B on ~$165M ARR; Decagon $4.5B on ~$35M). The valuation is priced for a winner-take-most product outcome — the *integration + delivery* layer underneath is the unfunded gap DataStaqAI occupies.
- **Coverage/limits:** 24/42 vendors have a public valuation, 13/42 a public ARR, 32/42 a disclosed total raised; blanks are omitted (not zero). Legora's valuation is disputed across sources and was left blank. Figures trace to `vendors.csv` → `COMPETITIVE_*.md`.
