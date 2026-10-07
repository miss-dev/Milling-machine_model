# Phase 2 Review: Design

> Worked example. See [examples/README.md](README.md).

- **Gate:** Design Review
- **Gate date:** 2026-10-30
- **Prepared by:** Amara Okafor, Kofi Mensah, Mei Lin
- **Phase dates:** planned 2026-09-21 → 2026-10-28; actual end 2026-10-30
- **Slides:** `assets/phase-2-design-review.pdf`

## 1. Summary

The design is complete and the long-lead parts have been ordered. The two highest technical risks have been retired or reduced by experiment: on-device model accuracy (EXP-2026-10-14) and the node's energy budget (EXP-2026-10-21). The gate is two days late because of a lab closure, but this does not affect later gates. The main concern going into Phase 3 is integration: the LoRaWAN link from node to The Things Stack to the server has not been tested end to end, and the PSRAM workaround is untested with the radio running.

## 2. Gate checklist

- [x] Concepts: 3 concepts, selection justified (concepts.md, TS-001)
- [x] Trade studies: inference location (TS-001), node board (TS-002), server and dashboard stack (TS-003)
- [x] Design decisions: DDR-001 to DDR-006
- [x] Architecture: all sections complete (architecture.md)
- [x] Subsystem docs: Node Hardware, Power, Detection, Comms, Server and Dashboard. Each has an owner
- [x] Data plan and dataset card: LeafWatch leaves v2, split by greenhouse row ([dataset card](dataset-example.md))
- [x] BOM v1 with costs: $52 per node; $286 planned in total against a $350 budget
- [x] Long-lead parts ordered: node boards, solar panels, LoRa modules (BOM E01, P02, E03)
- [x] Test plan v1: T-01 to T-06 cover all mandatory FRs and PRs
- [x] Traceability: first four columns complete
- [x] Early experiments: EXP-2026-10-14 (int8 model accuracy), EXP-2026-10-21 (node sleep current)
- [x] Risk register and schedule updated (review log 2026-10-29)
- [ ] Power board schematic is only 80% done. Remaining: camera load switch and battery protection. Due 2026-11-03 (Kofi, #31)

## 3. Key accomplishments

| Accomplishment | Evidence |
|---|---|
| Inference location selected and validated by experiment | TS-001, DDR-002, EXP-2026-10-14 |
| Camera power-gated with a load switch after the sleep-current measurement found 18.5 mA in deep sleep, because the camera stayed powered. Estimated run time without sun (1600 mAh usable) rises from under 4 days to over 3 months | EXP-2026-10-21, DDR-005 |
| Dataset v2: 3,900 labelled images, split by greenhouse row | [Dataset card](dataset-example.md) |
| LoRaWAN payload format defined | architecture.md section 4 |
| Enclosure v1 printed and tested for fit | `hardware/cad/enclosure/`, photos in `media/photos/` |

## 4. Requirements status

| Status | Count | Notes |
|---|---|---|
| Verified | 0 | Expected at this stage |
| In progress | 15 | |
| At risk | 1 | PR-01 (recall ≥ 90% target): 89.0% on the test set, which only has images from 08:00 to 16:00, and 74% on 07:00 images. Moving the first check to 08:30 should help, but is untested |
| Changed this phase | 2 | PR-01 and PR-02 test set changed; FR-D2 removed (see change log) |

## 5. Schedule

| | Planned | Actual / forecast |
|---|---|---|
| This phase gate | 2026-10-28 | 2026-10-30 |
| Next phase gate (Integration Review) | 2026-11-25 | 2026-11-25 |
| Final submission | 2026-12-14 | 2026-12-14 |

The two-day slip was caused by the B204 lab closure. Phase 3 started on schedule in parallel (firmware bring-up began 2026-10-26), so the Integration Review date is unchanged.

## 6. Risks

| ID | Risk | Score | Change since last review |
|---|---|---|---|
| R-03 | If integrating the LoRaWAN link (join, duty cycle, The Things Stack, server) takes longer than planned, then T-02 and T-03 slip | 16 | New in top 3; the link has not been tested end to end |
| R-08 | If accuracy drops in morning, evening or overcast light, then PR-01 may fail | 12 | New |
| R-01 | If the node boards arrive late, then the node build slips | 4 | Reduced from 12: boards arrived 2026-10-24 |

## 7. Budget

**Spent:** $138 of $350 · **Forecast at completion:** $305 (including $45 contingency)

## 8. Issues and blockers

- The PSRAM workaround (#15) adds 170 ms per inference (610 ms → 780 ms). Acceptable for now.
- Permission to mount nodes on the plant rows granted 2026-10-20. No blockers.

## 9. Team

Amara: server and dashboard design, schedule, budget (LOG-04, LOG-05). Kofi: node electronics, power, enclosure and LoRaWAN (LOG-04, LOG-05). Mei: dataset, model and test plan (LOG-03, LOG-04). Work was well balanced. The team agreed to add a short stand-up on Wednesdays, because two integration questions waited a full week for the weekly meeting.

## 10. Plan for the next phase

| Goal / deliverable | Owner | Due |
|---|---|---|
| Power board with camera load switch built | Kofi | 2026-11-06 |
| Every check reaches The Things Stack | Kofi | 2026-11-10 |
| Detection running on a node in the greenhouse | Mei | 2026-11-12 |
| Dashboard and email alerts from the server | Amara | 2026-11-17 |
| End-to-end demo: a node detects early blight on an infected plant and the email reaches Ruth Amadi's phone | All | 2026-11-24 |

## 11. Retrospective

| Keep doing | Stop doing | Start doing |
|---|---|---|
| Running quick experiments before committing to a design | Leaving schematics until after the CAD is finished | Wednesday stand-up for integration questions |

---

## Mentor assessment

- **Outcome:** Pass with actions
- **Strengths:** Decisions are backed by evidence. Splitting the dataset by row instead of by image was exactly right. The sleep-current measurement found a problem that would have sunk T-04 in Phase 4.
- **Concerns:** PR-01 is genuinely at risk under real light. One week of October images will not represent December. Integration has no slack before 2026-11-24.
- **Required actions (with due dates):** (1) Power schematic, including battery protection, reviewed by me before the board is powered on, by 2026-11-04. (2) Add a fallback plan for PR-01 to the risk register by 2026-11-06 (for example, more training images across times of day, or a small LED fill light).
- **Mentor and date:** Dr. Sam Taylor, 2026-10-30
