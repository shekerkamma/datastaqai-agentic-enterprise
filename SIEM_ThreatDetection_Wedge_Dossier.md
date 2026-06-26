# Agentic Wedge Dossier — SIEM Tier-1 (Threat Detection / SecOps)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — r/cybersecurity verbatim: "L1 SOC analyst here—drowning in false positives," 90%+ FP, real alerts missed. This is an **enrichment** wedge (KEEP).

## 1. Target SaaS & Use Case
- **Agent Type:** Security
- **Use Case:** Threat detection / SecOps (tier-1 triage)
- **SaaS in the crosshairs:** SIEM tier-1 (Splunk/Sentinel/QRadar-class)
- **Taxonomy Verdict:** KEEP (SIEM stays system of record; incident history is the moat; the L1 seat compresses)
- **Deployed proof points:** Google Security Operations deployments (signal correlation, agent-surfaced detection)

## 2. OSINT Source Map & Methodology
Mined a r/cybersecurity "drowning in false positives" thread analysis, an alert-fatigue root-cause study, an analyst-attrition essay, and SecurityWeek.

| # | Source | URL |
|---|--------|-----|
| 1 | Command Zero — The L1 SOC Analyst Crisis (r/cybersecurity verbatim) | https://www.commandzero.ai/blog/the-l1-soc-analyst-crisis-reddit-thread-reveals-whats-really-breaking-security-operations |
| 2 | D3 Security — SIEM Alert Fatigue Has Five Root Causes | https://d3security.com/blog/reduce-siem-alert-fatigue/ |
| 3 | Simplico — The Alert Tax (analyst attrition) | https://simplico.net/2026/05/18/the-alert-tax-why-your-soc-is-burning-out-your-best-people/ |
| 4 | SecurityWeek — Alert Fatigue Is Becoming a Security Threat of Its Own | https://www.securityweek.com/alert-fatigue-is-becoming-a-security-threat-of-its-own/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The plea.** r/cybersecurity L1 at an MSSP (via Command Zero): *"I'm working as an L1 SOC analyst at an MSSP… the insane volume of alerts, thousands of offenses per day, and honestly, 90%+ are false positives… There is no structured approach for rule creation or fine-tuning. Everyone just experiments… It feels like chaos with no methodology."* Conclusion: *"I feel like I'm stuck in an endless loop of closing the same false positives every day and as a result, real alerts often get missed."* (Source 1)
- **The numbers behind the loop.** D3: *"The average enterprise SOC receives over 4,400 alerts per day… Analysts investigate only 37% of them… Over 50% of SIEM alerts are false positives. Some organizations report rates as high as 80%… Analysts spend 56 minutes gathering context before investigation even begins… Over 70% of SOC analysts report burnout. The average analyst stays in the role under three years… 61% of SOC teams have ignored alerts that later proved to be genuine security incidents."* (Source 2)
- **Why your best people quit.** Simplico: *"She didn't quit because of the hours… She quit because for 18 months she has triaged the same five false-positive alerts, in the same five tools that don't talk to each other, against the same three-paragraph playbook PDFs that nobody has updated since 2022. She quit because the work had stopped meaning anything."* (Source 3)
- **Fatigue as a threat vector.** SecurityWeek: noise correlation is *"difficult, boring, and often pointless… continuous long hours and continuous stress with no escape. This is a seedbed for burnout."* (Source 4)

## 4. User Psychographics
- **Roles:** L1/L2 SOC analysts, MSSP triage teams, SOC managers watching attrition.
- **Emotional state:** Learned helplessness — closing the same false positives daily, "hearing alerts in their dreams," knowing real threats slip through, one bad week from quitting.
- **The acute bottleneck:** Context-free, single-signal alerts at 4,400+/day; analysts manually gather 56 min of context per alert and only investigate 37%.

## 5. The Agentic Wedge
**Wedge name:** "Autonomous Investigation Agent (Report, Don't Triage)"

**How it works:** An agent that rides on the SIEM and performs the full L2-grade investigation on *every* alert — correlating signals, gathering the 56 minutes of context automatically, and delivering a completed investigation report with documented reasoning — so analysts *review and validate* instead of *building from raw alerts*.

**Why it wins:** It eliminates the proven bottleneck (manual triage of 4,400 noisy alerts) and the attrition it drives, while *riding on* the SIEM's data and incident history — the moat. KEEP: the SIEM stays system of record; the repetitive L1 triage seat compresses into a review/hunt role.

**Buyer trigger:** A genuine incident missed in the noise — or a third SOC analyst resigning in a year.
