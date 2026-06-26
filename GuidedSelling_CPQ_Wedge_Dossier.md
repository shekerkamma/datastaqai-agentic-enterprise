# Agentic Wedge Dossier — Guided-Selling / CPQ (AI Shopping & Sales Consultant)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — Salesforce CPQ generates a dense, vocal "shadow-spreadsheet" complaint corpus; reps abandon the tool entirely.

## 1. Target SaaS & Use Case
- **Agent Type:** Customer
- **Use Case:** AI shopping / sales consultant (guided selling)
- **SaaS in the crosshairs:** Guided-selling / CPQ (configure-price-quote) SaaS
- **Taxonomy Verdict:** REPLACE (per-seat CPQ/merchandising assistants compress; commerce platform stays)
- **Deployed proof points:** Mercedes-Benz gen-AI smart sales assistant, Mobiauto "Shopping Consultant" (Gemini + BigQuery), Best Buy guided product selection

## 2. OSINT Source Map & Methodology
Mined the **Salesforce Trailblazer Community** (power-user Q&A), RevOps practitioner analyses, and vendor post-mortems on CPQ failure.

| # | Source | URL |
|---|--------|-----|
| 1 | Salesforce Trailblazer Community — most common CPQ complaints | https://trailhead.salesforce.com/trailblazer-community/feed/0D5KX00000anTeW0AU |
| 2 | Valor X — Salesforce CPQ: Maybe? Maybe Not? | https://www.valorx.com/blog/salesforce-cpq-good-or-bad |
| 3 | Valor X — CPQ Challenges for Enterprises [Q&A] | https://www.valorx.com/blog/cpq-challenges-enterprises |
| 4 | servicepath — Legacy Salesforce CPQ Is Breaking RevOps | https://servicepath.co/2025/11/legacy-salesforce-cpq-is-breaking-revops-what-end-of-sale-means-for-2026/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The top-5 pain list, straight from the community.** Trailblazer thread: *"Low Sales Adoption – Clunky UX means reps avoid using CPQ altogether, defeating the entire purpose; Slow Time-to-Market – 8-16 weeks just to launch new products or update pricing… Migration & Entitlement Nightmares… Approval Bottlenecks… System Disconnects… These aren't just minor inconveniences – they're business-critical issues that directly impact revenue."* (Source 1)
- **Reps quietly defect to Excel.** Valor X: *"users take their quoting offline in spreadsheets, negating many of the benefits of having Salesforce CPQ."* And: *"What could take minutes in an Excel spreadsheet can take hours or days in Salesforce CPQ."* (Source 2)
- **It crashes under real volume.** *"The Salesforce CPQ engine slows down significantly, or altogether crashes, when dealing with hundreds and hundreds of quote lines… users often get stopped in their tracks unexpectedly."* (Source 2)
- **The irony of the implementers.** *"Ironically, the organizations helping businesses implement Salesforce CPQ are often unable to use it themselves due to the complexities of services quoting."* (Source 2)
- **Shadow CPQ as a governance problem.** servicepath: *"Sales and pre-sales teams fall back to Excel or local tools when CPQ can't handle real-world complexity… CPQ failure case studies repeatedly highlight 'shadow CPQ' as a governance and data-quality problem."* Cites that *"up to two-thirds of CPQ implementations fail to reach full completion or adoption."* (Source 4)
- **Knowledge trapped in heads and brittle scripts.** *"Pricing and configuration knowledge lives in experts' heads and brittle scripts, not in a governed platform."* (Source 4)

## 4. User Psychographics
- **Roles:** RevOps leaders, sales engineers, deal-desk admins, CPQ administrators at complex-product B2B sellers.
- **Emotional state:** Defeated and resentful — forced to use a tool slower than the 40-year-old spreadsheet it replaced, blamed for low adoption they can't fix, bracing for the Salesforce CPQ end-of-sale migration.
- **The acute bottleneck:** Record-by-record quote-line editing and weeks-long change cycles where "everything has to go through IT."

## 5. The Agentic Wedge
**Wedge name:** "Conversational Quote Agent (Catalog-Grounded)"

**How it works:** An agent grounded in the product catalog, pricing rules, and inventory that builds a complete, compliant quote from a natural-language brief — bulk-editing quote lines, applying entitlement/rebate logic, and routing approvals — without the record-by-record grid or 8–16-week config cycle.

**Why it wins:** It does the consultative selling and quote assembly the per-seat CPQ tool scripts, but at conversation speed, killing the #1 cited pain (reps abandoning to Excel). The commerce platform stays as system of record; the guided-selling seats compress. REPLACE at the seat layer.

**Buyer trigger:** Salesforce CPQ End-of-Sale — every month on legacy CPQ hard-wires migration risk deeper.
