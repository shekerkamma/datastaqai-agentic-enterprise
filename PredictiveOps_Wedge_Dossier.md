# Agentic Wedge Dossier — Predictive-Analytics SaaS (Forecasting / Predictive Ops)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — "the boy who cried wolf": an $1.8M deployment fired 87,000 alerts/month, missed a real failure for 11 days ($340k). This is an **enrichment** wedge (KEEP).

## 1. Target SaaS & Use Case
- **Agent Type:** Data
- **Use Case:** Forecasting / predictive ops (predictive maintenance)
- **SaaS in the crosshairs:** Predictive-analytics SaaS
- **Taxonomy Verdict:** KEEP (moat = proprietary sensor/operational data; agent augments the model, doesn't replace the platform)
- **Deployed proof points:** Honeywell, Geotab (predictive maintenance + fleet forecasting on proprietary telematics)

## 2. OSINT Source Map & Methodology
Mined a manufacturer's named "cried wolf" post-mortem, a machine-health vendor on alarm fatigue, a "dead end" practitioner essay, and a production-lessons retro.

| # | Source | URL |
|---|--------|-----|
| 1 | 21Tech — 100,000 Alerts a Day, Your Team Reads 12 | https://21tech.com/your-predictive-maintenance-platform-generates-100000-alerts-a-day-your-team-reads-12/ |
| 2 | Augury — Why Your Team Stopped Trusting PdM Alerts | https://www.augury.com/blog/machine-health/why-your-team-has-stopped-trusting-their-predictive-maintenance-alerts/ |
| 3 | IIoT World — Is Predictive Maintenance at a Dead End? | https://www.iiot-world.com/predictive-analytics/predictive-maintenance/is-predictive-maintenance-at-a-dead-end/ |
| 4 | Manufacturing Mag — Predictive Maintenance Reality | https://www.manufacturingmag.com/article/predictive-maintenance-reality |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **"The boy who cried wolf."** 21Tech: an Ohio auto-parts maker spent *"$1.8 million deploying IoT sensors across 340 production assets… The system generated over 87,000 alerts in its first full month. The four-person maintenance crew investigated roughly 50 per day… an average of 3 led to actual corrective action. The other 47 were false positives… In February, a genuine spindle bearing failure went unnoticed for 11 days. The resulting unplanned downtime cost $340,000."* (Source 1)
- **Teams quietly stop acting.** Augury: *"they have a predictive maintenance program, alerts are coming in, and the team has quietly stopped acting on most of them. Not because they don't care. Because they've been burned too many times by alerts that turned out to be nothing."* It's *"an accuracy problem, not a volume problem."* (Source 2)
- **Chasing one's own tail.** IIoT World: *"predictive maintenance is like chasing one's own tail… the same problems don't recur, the patterns are never the same."* (Source 3)
- **Pilot vs floor.** Manufacturing Mag: *"Seventy percent of predictive maintenance initiatives fail within two years… Sensors flag anomalies, but technicians chase ghosts. False positives consume 40% of wrench time… Leadership pushes PdM for 20-30% uptime gains seen in pilots; floor reality delivers 2-5% at best."* (Source 4)

## 4. User Psychographics
- **Roles:** Reliability/maintenance engineers, plant managers, ops leaders who bought a 6–7-figure PdM platform.
- **Emotional state:** Burned and distrustful — "cried wolf" fatigue, embarrassed by a $1.8M system that missed a real failure, over-maintaining ghosts while real problems slip.
- **The acute bottleneck:** Single-sensor anomaly alerts with no context and no CMMS integration — a flood of false positives that destroys trust and buries the real signal.

## 5. The Agentic Wedge
**Wedge name:** "Trustworthy Triage Agent (Fuse → Contextualize → Work-Order)"

**How it works:** An agent layered on the existing PdM platform that (1) fuses multi-sensor signals into a composite health score, (2) applies operating context (load, schedule, maintenance history) to suppress process-fluctuation noise, and (3) emits not an alert but a CMMS work order — "Bearing 4B, +22% vibration over 14 days, schedule replacement within 10 days, parts in stock."

**Why it wins:** It fixes the proven trust-killer (false-positive flood, alerts-not-work-orders) while *riding on* the platform's proprietary sensor data — which is the moat. KEEP: the agent makes the predictive-analytics investment finally pay off; spend consolidates onto the data-owning platform rather than disappearing.

**Buyer trigger:** A real failure missed amid the noise (a "$340k while we ignored the dashboard" moment).
