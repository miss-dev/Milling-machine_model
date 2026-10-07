# Meeting: 2026-10-13 (mentor)

> Worked example. See [examples/README.md](README.md).

- **Date and time:** 2026-10-13, 10:00–10:35
- **Type:** mentor
- **Attendees:** Amara Okafor, Kofi Mensah, Mei Lin, Dr. Sam Taylor
- **Absent:** None
- **Note-taker:** Kofi Mensah

## Open actions from the last meeting

| Action | Owner | Status |
|---|---|---|
| Finish inference location trade study (TS-001) | Mei | Done |
| Enclosure CAD v1 | Kofi | Done |
| Submit budget request to department | Amara | In progress: submitted 10 Oct, no reply yet |

## Agenda

1. Inference location trade study (TS-001)
2. Enclosure and camera mount
3. Budget approval
4. Design Review date

## Discussion

### 1. Inference location trade study

Mei presented TS-001. On-node inference scored 3.65 and the greenhouse hub 3.35. Dr. Taylor asked how much the result depends on the weights. We had not checked. Dr. Taylor then pointed out that the accuracy score for on-node inference comes from PlantVillage, which is lab photos of single leaves on plain backgrounds, and suggested measuring accuracy on our own greenhouse images, on the real board, before committing. For the same reason, PR-01 should be measured on greenhouse images too (requirement change 2026-10-13). Mei can run the experiment this week.

### 2. Enclosure and camera mount

Kofi showed the enclosure CAD with the camera 25 cm above the canopy. Discussion: closer gives more detail per leaf but sees fewer leaves, and the dataset was collected at 40 cm. The farm's existing sensors log humidity above 90% most early mornings, so condensation will form on the camera window. Agreed 40 cm to match the dataset, plus an anti-fog coating on the window to try.

### 3. Budget approval

Still waiting for the department. Dr. Taylor will email the department administrator.

### 4. Design Review date

Proposed 28 Oct. Lab B204 is closed 27–28 Oct, so we moved it to 30 Oct.

## Decisions

| Decision | DDR |
|---|---|
| Proceed with on-node inference, subject to an experiment confirming ≥ 90% accuracy on greenhouse images, run on the ESP32-S3 | DDR-002 (to be written after the experiment) |
| Measure PR-01 and PR-02 on greenhouse images taken by the node cameras | — (requirements change log) |
| Camera 40 cm above the canopy | — (recorded in Node Hardware subsystem doc) |
| Design Review on 2026-10-30 | — |

## Action items

| Action | Owner | Due | Issue |
|---|---|---|---|
| Add sensitivity check to TS-001 | Mei | 2026-10-15 | — |
| Experiment: int8 accuracy on the ESP32-S3 with greenhouse images | Mei | 2026-10-15 | #14 |
| Update enclosure: camera mount at 40 cm; anti-fog window | Kofi | 2026-10-17 | #16 |
| Email department about budget | Dr. Taylor | 2026-10-14 | — |
| Update schedule with Design Review date | Amara | 2026-10-14 | — |

## Mentor feedback

- "A trade study without a sensitivity check is only half done. Show me the decision holds if your weights are a bit wrong."
- "Your real risk isn't accuracy on this week's photos. It's what happens when the light changes, or the plants look different in December. Design for the model being wrong."
- "Order the solar panels now. Lead times have been 2–3 weeks."
