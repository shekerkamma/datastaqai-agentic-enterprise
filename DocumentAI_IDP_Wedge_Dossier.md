# Agentic Wedge Dossier — IDP / OCR SaaS (Document AI / Extraction)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — r/Accounting verbatim: NetSuite OCR "chokes on half our invoices"; manual entry *rose* from 60% to 66% despite billions in automation spend.

## 1. Target SaaS & Use Case
- **Agent Type:** Data
- **Use Case:** Document AI / extraction
- **SaaS in the crosshairs:** IDP / OCR SaaS (template-based capture)
- **Taxonomy Verdict:** REPLACE (downstream system of record stays; capture-tool seats + the clerk role go)
- **Deployed proof points:** Document AI deployments parsing invoices/forms/contracts at scale

## 2. OSINT Source Map & Methodology
Mined an r/Accounting-sourced AP analysis, a workflow breakdown of why OCR fails, and AP cost/time studies.

| # | Source | URL |
|---|--------|-----|
| 1 | ImageToTable — Why AP Teams Still Enter Invoices Manually (r/Accounting quote) | https://imagetotable.ai/blog/why-ap-teams-still-manual-invoice-data-entry |
| 2 | DEV — Why Basic OCR Failed Our B2B Clients | https://dev.to/lyriryl/why-basic-ocr-failed-our-b2b-clients-and-what-actually-fixed-it-kb3 |
| 3 | Peakflo — AI Invoice Capture (Aberdeen time data) | https://peakflo.co/blog/ai-invoice-capture-eliminate-manual-data-entry |
| 4 | ValueDX — 7 Hidden Costs of Manual Data Entry in AP | https://valuedx.com/manual-data-entry-in-accounts-payable-costs/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The r/Accounting reality check.** Verbatim, via ImageToTable: *"We get maybe 1,500–2,000 invoices a month from suppliers. I keep hearing AP automation is basically solved at this point, but our process is still: invoices hit a shared inbox as PDF attachments, someone opens each one, types the header info into NetSuite, matches to PO manually, routes for approval via email, chases down approvers when they ignore it. We tried the OCR thing built into NetSuite but it chokes on half our invoices because every machine shop and raw materials supplier formats theirs differently."* And the kicker: in 2023, 60% of AP teams keyed manually; *"Two years and billions in automation investment later, that number is 66%."* (Source 1)
- **Template OCR breaks on the long tail.** *"Template OCR works by remembering where fields are on a known layout… The moment a vendor changes their invoice template — or you add a new vendor — those coordinates stop being correct."* (Source 1)
- **OCR solves the wrong 10%.** DEV: *"a basic OCR tool solves the wrong problem… Routing that string into your accounting software, archiving the original PDF…, triggering approvals, and logging an audit trail — none of that is OCR. It is the other 90% of the workflow."* A team running 15 hrs/week reclaims 11–13. (Source 2)
- **The cost, quantified.** Peakflo (Aberdeen 2026): *"8-12 minutes per invoice… For organizations processing 2,000+ monthly invoices, manual data entry consumes 267-400 hours monthly—equivalent to 3.3-5 full-time employees doing nothing but typing invoice headers."* ValueDX: AP specialists spend *"60 and 70 percent of their working hours on data entry,"* with a 1–3.6% error rate driving rework. (Sources 3, 4)

## 4. User Psychographics
- **Roles:** AP clerks, finance ops managers, controllers at companies with diverse vendor bases.
- **Emotional state:** Skeptical and worn down — told "automation is solved" while still typing thousands of invoices, re-keying after errors, chasing approvers; paying twice (entry + rework).
- **The acute bottleneck:** Template-based capture that breaks on every vendor format variation — exactly the long tail that generates the most manual work — plus the un-automated 90% (routing, matching, approval, audit).

## 5. The Agentic Wedge
**Wedge name:** "Read-Like-a-Human Document Agent (End-to-End AP)"

**How it works:** A VLM-based agent that reads any invoice format with no templates (understands "INV-2025-08472 next to 'Invoice #' or 'Ref' is the invoice number" regardless of position), then does the other 90% — PO matching, validation, approval routing, filing, audit log — flagging only low-confidence exceptions for humans.

**Why it wins:** It directly defeats the #1 cited failure (template OCR choking on format variety) and absorbs the full clerk workflow, not just field extraction. The ERP/system of record stays; the capture-tool seats and the manual-keying role are displaced. REPLACE.

**Buyer trigger:** Realizing 3.3–5 FTE are "doing nothing but typing invoice headers" while the OCR add-on still chokes on half the inbox.
