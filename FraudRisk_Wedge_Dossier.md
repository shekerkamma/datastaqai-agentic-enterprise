# Agentic Wedge Dossier — Fraud / Risk Add-ons (Fraud & Risk Detection)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — a documented case: a merchant *abandoned* its anti-fraud tool after false positives spiked, ending up reviewing 20% of orders with 15 added staff and 19%/month declines. **Enrichment** wedge (KEEP).

## 1. Target SaaS & Use Case
- **Agent Type:** Security
- **Use Case:** Fraud & risk detection
- **SaaS in the crosshairs:** Fraud / risk add-ons (rules engines + manual-review queues)
- **Taxonomy Verdict:** KEEP (bank's transaction data + models are the moat; being wrong is expensive, so humans stay in the loop; agent augments)
- **Deployed proof points:** Citi, Wells Fargo (risk/fraud analysis), Commerzbank "Bene"

## 2. OSINT Source Map & Methodology
Mined a J.P. Morgan merchant case study, a fraud-ops metrics primer, and false-positive cost analyses.

| # | Source | URL |
|---|--------|-----|
| 1 | J.P. Morgan — When false positives spiked, company abandoned fraud tools | https://www.jpmorgan.com/insights/payments/data-intelligence/cnp-fraud-prevention-combat-chargebacks |
| 2 | Fraud Attacks — Fraud Operations & Metrics | https://fraudattacks.com/learningcenter/fraud-basics/fraud-operations-metrics |
| 3 | The Cloud Community — False Positives: The Silent Drain | https://www.thecloudcommunity.net/business-performance/fraud/false-positives-the-silent-drain-on-fraud-teams/ |
| 4 | Experian — The Pros and Cons of Manual Fraud Reviews | https://www.experian.com/blogs/insights/pros-cons-manual-fraud-reviews/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The death spiral, documented.** J.P. Morgan: an online booking client *"initially deployed an automated anti-fraud solution, but soon abandoned its use due to a rise in false positives… within weeks chargebacks increased to more than 3 percent… the retailer was reviewing over 20 percent of all orders, requiring the addition of 15 employees dedicated to the task. When order declines reached a high-water mark of 19 percent per month, seriously eroding revenues…"* Industry trend: *"as much as 35 percent of rejected orders turning out to be good, up from 25 percent year-over-year."* (Source 1)
- **False positives are the silent, invisible cost.** Fraud Attacks: *"A false positive is a legitimate transaction that your system flagged as fraudulent. High false positive rates mean you're blocking good customers, wasting analyst time reviewing clean transactions, and damaging the customer experience… Declined customers rarely complain. They just leave. The cost of false positives is often larger than fraud losses, but harder to measure."* (Source 2)
- **80–95% noise in banking.** The Cloud Community: *"Especially across banking and payment providers, false positives can account for 80–95% of all alerts… analysts spend hours validating non-fraud events, and real threats get less attention."* The cause: context (device, behavior, history) *"lives in other systems."* (Source 3)
- **Manual review loses customers.** Experian: practitioners reported *"more than 50% of those customers were lost"* to manual-review delay/friction; manual review also *"doesn't support policy development"* because the reviewer's reasoning can't be reconstructed. (Source 4)

## 4. User Psychographics
- **Roles:** Fraud analysts, risk-ops managers, payments/risk leads at issuers, banks, and e-commerce.
- **Emotional state:** Caught in a two-front war — block fraud vs. don't lose good customers; buried in review queues; aware the false-positive cost (silent churn) likely exceeds actual fraud losses.
- **The acute bottleneck:** Context-poor rules engines that escalate everything to a manual queue, blocking good customers and consuming analyst hours, with no way to reconstruct reviewer reasoning.

## 5. The Agentic Wedge
**Wedge name:** "Case-File Fraud Agent (Enrich → Prioritize → Evidence)"

**How it works:** An agent that enriches each flagged event with cross-system context (device reputation, behavioral history, location), auto-prioritizes the review queue, compiles a complete case file with an evidence packet, and routes — auto-approve low-risk, step-up medium, auto-decline high-risk with documented reasoning — leaving only genuinely ambiguous cases for humans.

**Why it wins:** It attacks the proven pains (false-positive flood, review-queue overload, lost good customers, un-reconstructable decisions) while *augmenting* the bank's proprietary data and models — the moat. KEEP: being wrong is expensive, so humans stay in the loop; the agent makes them faster and their decisions auditable.

**Buyer trigger:** A false-positive spike forcing added review headcount and rising good-customer declines.
