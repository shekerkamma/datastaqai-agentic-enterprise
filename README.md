# The Agentic Enterprise — DataStaqAI Strategy Package

A complete, source-grounded market + competitive strategy package for **DataStaqAI**, the done-for-you AI engineering firm positioned as **the delivery layer for the agent era** (mid-market).

> **Private / confidential.** Contains competitive intelligence, an illustrative financial model, GTM, and positioning.

## Thesis
Enterprise work is moving from **software-assisted** (per-seat SaaS) to **AI-orchestrated** (agentic). Value accrues not to the commoditizing model nor the seat-defending incumbent, but to whoever **delivers the orchestration** — the agent wired into the customer's systems of record, governed and operated. Every category has split into incumbents and AI-natives; both leave the **mid-market done-for-you delivery layer** unowned. DataStaqAI occupies that layer.

## What's inside
```
/                         25 agentic-wedge dossiers (*_Wedge_Dossier.md) + _INDEX.md
                          POSITIONING.md (25 pitch/positioning cards) · COMPETITIVE.md (shallow first pass)
                          COMPETITIVE_{Customer,Employee,Creative,Code,Data,Security}.md  (deep research, 6 clusters, 40+ vendors)
                          prospects.csv · _PROSPECTS_top6.md (lead/ICP signals)
/analysis/                competitive_dataset.csv (25 use cases) · vendors.csv (42 vendors)
                          7 charts (PNG) · analysis scripts (*.py) · FINDINGS.md · analysis deck (.pptx)
/book/                    "The Agentic Enterprise" — 8 chapters
                          DataStaqAI-The-Agentic-Enterprise.pptx          (48-slide master deck, speaker notes)
                          DataStaqAI-Competitive-Battlecards.pptx         (24-slide sales battlecards)
                          DataStaqAI-The-Agentic-Enterprise-Report.docx   (Word report + figures)
                          DataStaqAI-Competitor-Database.xlsx             (vendors · use cases · funding)
                          DataStaqAI-Financial-Model.xlsx                (editable 3-yr model, live formulas)
                          DataStaqAI-90-Day-GTM-Plan.docx                (execution plan)
                          per-chapter decks + Chapter*.md specs + build_*.py (reproducible builders) + DECK_TOC.md
```

## Key outputs
- **48-slide master deck** (7 parts: Executive Thesis · AI Transformation · Business Use Cases · Competitive Analysis · Business Model · Path to $5–10M · Investment Thesis), speaker notes on every slide.
- **24-slide battlecards** (5 archetypes + 13 named competitors + objection handling) — internal sales enablement.
- **Editable financial model** (driver-based; default planning case → ~$4.8M ending recurring ARR by Y3, exit run-rate in the $5–10M band).

## Provenance & honest caveats
- Vendor figures, pricing, and market sizes are **source-traceable** to the deep-research files (gathered via Exa). Blanks = not publicly disclosed (not zero).
- **Financial figures in Parts V–VII and the model are illustrative**, with stated assumptions — replace with real win/loss + cost-to-serve before external use.
- **Competitive density and where-to-play scoring are judgment**, not measured indices (labeled).
- Decks were validated for OOXML correctness and visually QA'd via a matplotlib proxy (`preview_pptx`), **not** PowerPoint itself — open once in PowerPoint to confirm rendering.

## Reproduce
Builders are stdlib + `python-pptx` / `python-docx` / `openpyxl` / `matplotlib`. Re-run any `book/build_*.py` or `analysis/analyze_*.py`; `book/merge_book.py` reassembles the master deck.
