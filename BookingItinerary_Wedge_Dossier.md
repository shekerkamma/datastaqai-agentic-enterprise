# Agentic Wedge Dossier — Booking / Itinerary Tools (Travel & Booking Planner)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — GDS pain is extreme and specific: agents buy "errors insurance" against a 1980s text terminal; gate agents "avoid it like the plague."

## 1. Target SaaS & Use Case
- **Agent Type:** Customer
- **Use Case:** Travel & booking planner (plan-and-book loop)
- **SaaS in the crosshairs:** Booking / itinerary tools (GDS front-ends, agent booking seats)
- **Taxonomy Verdict:** REPLACE (human-facing booking-tool seats shrink; reservation system of record stays)
- **Deployed proof points:** Agoda AI Vacation Planner, Priceline trip tools, LATAM "Cosmos," Virgin Voyages "Rovey"

## 2. OSINT Source Map & Methodology
Mined **Hacker News** (a practicing travel agent's first-person account), **Airliners.net** and **FlyerTalk** (gate/reservations-agent forums), **Amadeus** and **SAP Concur** community threads.

| # | Source | URL |
|---|--------|-----|
| 1 | Hacker News — travel agent on SABRE internals | https://news.ycombinator.com/item?id=34152434 |
| 2 | Airliners.net — Why Is Sabre Still Used? | https://www.airliners.net/forum/viewtopic.php?t=756661 |
| 3 | FlyerTalk — United's Poor GDS (systems & processes) | https://www.flyertalk.com/forum/united-airlines-mileageplus/2068280-united-s-poor-gds-systems-current-processes.html |
| 4 | SAP Concur Community — Changes / Ticket Reissue (Amadeus) | https://community.concur.com/t5/Concur-Travel-Forum/Changes-Ticket-Reissue/m-p/21775 |
| 5 | Amadeus Community — new hotel format complaints | https://live-travel.community.amadeus.com/c/portal/view-thread/1253290475/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The 1980s terminal you can't afford to mistype in.** HN, practicing travel agent: *"The technology is incredibly antiquated. Most of the US runs on a system called SABRE, which is basically a MS-DOS system with a text command line interface and its own language… straight out of the 80s. Travel agents need to buy special 'errors' insurance to cover any losses caused by fucking it up (a typo could accidentally cancel a ticket and cause the client thousands in losses rebooking it)."* (Source 1)
- **Even airline staff refuse to use it.** Airliners.net: *"Gate agents from DFW to JFK seem to avoid it like the plague. The people I know there say it takes way too long to do anything."* On repricing: *"The fact that it takes 20 minutes IS Sabre's fault."* (Source 2)
- **Customers out-know the agents on fare rules.** FlyerTalk: *"one more hour invested and united still wants $1400 to make the change… as a customer I know the rules better than they do."* On exchanges: *"it's about 50/50 on being able to auto-price an exchange on a partially used ticket, and that goes to 0% if there were previous irrops."* (Source 3)
- **Automated exchanges barely work.** SAP Concur (Amadeus user): *"post-ticketing changes only apply to a very small percentage of the tickets… For the ticket changes that Concur can handle, they land on a queue for an agent to finish up. We've found that oftentimes, Concur does not price the new ticket in the lowest fare. We have to reprice it, and then redo the exchange."* (Source 4)
- **UI "upgrades" make it worse.** Amadeus community: *"It is very frustrating to use. How can we go back to using the old version?"* — answered with a cryptic-command workaround because no rollback exists. (Source 5)

## 4. User Psychographics
- **Roles:** Travel agents, corporate-travel TMC staff, airline reservations/gate agents, OTA ops.
- **Emotional state:** Anxious (one typo = client loses thousands), exhausted by 20-minute reprices and exchange edge-cases, distrustful of "modern" GUI layers that are slower than cryptic mode.
- **The acute bottleneck:** Mid-trip exchanges/rebooking where automation fails ~50–100% of the time and dumps to a manual agent queue that mis-prices the fare.

## 5. The Agentic Wedge
**Wedge name:** "Exchange & Re-book Agent (Fare-Rule Native)"

**How it works:** An agent that reads live inventory + IATA fare rules and executes the plan-and-book and the *exchange/reissue* loop end-to-end in natural language — auto-pricing the lowest valid fare, handling irrops and partially-used tickets, and surfacing the cryptic GDS commands it ran for auditability.

**Why it wins:** It targets the most acute, least-automated slice — mid-trip exchanges where existing tools fail and a typo is financially catastrophic. The GDS/reservation system of record stays (you can't rip out SABRE); the human booking-tool seats shrink. REPLACE at the seat layer.

**Buyer trigger:** "Errors insurance" premiums + the agent-queue backlog on exchanges.
