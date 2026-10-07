# Risk Register

<!-- GUIDE: At least 5 risks by the Phase 1 gate. Review the whole table at least every
     two weeks and at every gate. When a trigger fires, act on the mitigation and record it
     in the review log. -->

## How to score a risk

Write each risk as **"If <cause>, then <consequence>"**. That forces you to say both what might happen and why it matters.

| Score | Likelihood (L) | Consequence (C) |
|---|---|---|
| 1 | Very unlikely (< 10%) | Negligible: absorbed without schedule or performance impact |
| 2 | Unlikely (10–30%) | Minor: a few days' delay, or slight performance loss |
| 3 | Possible (30–50%) | Moderate: about a week's delay, or a desirable requirement lost |
| 4 | Likely (50–80%) | Major: several weeks' delay, or a mandatory requirement at risk |
| 5 | Almost certain (> 80%) | Severe: project cannot succeed, or someone could be hurt |

**Risk score = L × C.** 15–25 is **High** (act now), 6–12 is **Medium** (mitigate and monitor), 1–5 is **Low** (monitor).

**Types:** Technical, Schedule, Cost, People, Safety, External (suppliers, lab access, etc.)

**Status:** Open, Mitigating, Occurred, Closed

## Active risks

| ID | Risk (If…, then…) | Type | L | C | Score | Mitigation | Trigger (early warning) | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | EXAMPLE: If the main board ships late, then integration slips by 2+ weeks | Schedule | 3 | 4 | 12 | EXAMPLE: Order in Phase 2 week 1; identify a local alternative supplier | EXAMPLE: Not shipped 7 days after ordering | TODO | Open |
| R-02 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | Open |

<!-- GUIDE: Risks to consider. Keep the ones that apply to your project.
     Almost every project:
     - A team member is unavailable (illness, exams, other courses)
     - Integration takes much longer than expected
     - Scope creep: adding features instead of finishing core ones
     - Budget overrun
     - Lab, workshop or test-site access is limited
     Hardware (robotics, embedded, IoT):
     - A key component arrives late, is out of stock, or is dead on arrival
     - A component is damaged during testing (burnt driver, shorted board, cracked print)
     - Battery or power problems (brown-outs, insufficient run time)
     - Perception or localization is not accurate enough
     Connected systems (IoT, AIoT):
     - Connectivity at the real site is worse than in the lab
     - A cloud service, free tier or API changes or stops
     - Device credentials leak, or the system is reachable by strangers
     Machine learning:
     - Not enough data, or labels are wrong or inconsistent
     - The model scores well on the test set but poorly in real conditions
     - Test data leaks into training, so results look better than they are
     - Training compute (GPU time) is not available when needed
     - The data involves people and needs consent or ethics approval -->

## Closed risks

| ID | Risk | Closed on | What happened |
|---|---|---|---|
| — | — | — | — |

## Review log

| Date | Reviewed by | Changes |
|---|---|---|
| TODO | TODO | Initial register |
