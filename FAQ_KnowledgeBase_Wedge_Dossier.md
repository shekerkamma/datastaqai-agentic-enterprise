# Agentic Wedge Dossier — FAQ / Knowledge-Base & Deflection Tools (In-Product Owner Assistant)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — maintenance pain is the single most-cited CX complaint (59% of teams, unprompted), with vivid recurring "death spiral" language.

## 1. Target SaaS & Use Case
- **Agent Type:** Customer
- **Use Case:** In-product owner assistant / self-service deflection
- **SaaS in the crosshairs:** Manuals / FAQ / knowledge-base / call-deflection tools
- **Taxonomy Verdict:** RENEGOTIATE (enrich the product; strip the standalone KB/deflection bolt-ons)
- **Deployed proof points:** Volkswagen myVW (camera-at-dashboard multimodal answers), GM OnStar voice intent

## 2. OSINT Source Map & Methodology
Mined CX-practitioner blogs synthesizing operator interviews + support-team forum sentiment around KB rot and deflection failure.

| # | Source | URL |
|---|--------|-----|
| 1 | CustomerThink — Six Help Center Problems That Sabotage CX | https://customerthink.com/six-help-center-problems-that-quietly-sabotage-cx-and-undermine-ai-powered-support/ |
| 2 | HappySupport — The Documentation Maintenance Trap | https://happysupport.ai/blog/documentation-maintenance-trap |
| 3 | Vidocu — The Documentation Death Spiral | https://vidocu.ai/blog/the-documentation-death-spiral-why-your-help-center-has-stopped-working |
| 4 | Supportbench — KB that deflects (and doesn't go outdated) | https://www.supportbench.com/create-knowledge-base-deflect-tickets-prevent-outdated-content/ |
| 5 | Supp — Does a KB actually reduce tickets? | https://supp.support/blog/knowledge-base-roi |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The headline complaint, in a practitioner's own words.** A head of CX at a European CRM company: *"Maintaining the documentation is a bigger problem than creating it."* CustomerThink reports this pain was *"surfaced by 59 percent of teams without prompting."* (Source 1)
- **Agents have already given up on it.** *"When agents route around the help center to answer questions themselves, they have already concluded that keeping documentation up to date is someone else's problem."* (Source 2)
- **The Monday-morning ritual.** Vidocu's death-spiral description: *"Every release breaks a few articles. Every Monday a customer files a ticket that has been 'answered' in the KB since 2024. The team writes a new article. The pile grows. The number of tickets does not shrink."* (Source 3)
- **It poisons the AI you bolt on top.** *"Run a freshness audit… If it is under 30 percent, your AI is probably hallucinating from your own content. That is a number you can put in front of a CFO."* (Source 1)
- **The bottleneck isn't writing — it's change detection.** *"Hiring more writers does not solve the trap because the bottleneck is not writing speed. The bottleneck is change detection. Writers cannot update articles affected by a release unless someone tells them which articles were affected. In most companies, nobody does."* (Source 2)
- **Silent churn.** *"The customer who encounters a broken help center article does not always file a ticket. Sometimes they just stop trusting the product… That cost never shows up in a support ticket report. It shows up in the renewal rate six months later."* (Source 2)

## 4. User Psychographics
- **Roles:** Knowledge managers, CX leads, technical writers, support-team leads at product-velocity B2B SaaS companies.
- **Emotional state:** Resigned/guilty — they *know* the KB is wrong, can't keep up, and feel the maintenance loop "runs inside individual support agents' heads."
- **The acute bottleneck:** No signal linking a product/UI change to the articles it just invalidated; the KB is "the only part of the support stack with no scoreboard."

## 5. The Agentic Wedge
**Wedge name:** "Self-Healing Knowledge Agent (Change-Detection First)"

**How it works:** An agent that (1) watches product release/commit/UI-diff signals, (2) auto-flags and rewrites the exact articles each change invalidates, and (3) answers owner questions live from the *source* (product data) instead of from stale prose — so deflection content never decays.

**Why it wins:** It attacks the proven #1 pain (maintenance > authoring) at its real root (change detection, not writing speed). The product/KB system of record stays; the standalone authoring + deflection seats lose their reason to exist. RENEGOTIATE: keep the substrate, drop the bolt-ons.

**Buyer trigger:** A freshness audit showing <30% of articles updated in 90 days — i.e., "your AI is hallucinating from your own docs."
