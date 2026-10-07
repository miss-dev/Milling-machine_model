# DDR-002: Run the disease classifier on the node and send only results over LoRaWAN

> Worked example. See [examples/README.md](README.md).

- **ID:** DDR-002
- **Date:** 2026-10-16
- **Status:** Accepted
- **Decided by:** Whole team; reviewed with Dr. Sam Taylor on 2026-10-13
- **Author:** Mei Lin
- **Related:** FR-01, PR-01, PR-02, NFR-03, TS-001, EXP-2026-10-14, R-04

## Context

LeafWatch must detect early blight (FR-01) with at least 80% recall on greenhouse images (PR-01), and run for 7 days without sun (NFR-03). LoRaWAN is the only link that reaches the greenhouse, and one uplink carries tens of bytes, so images cannot be sent over it. Cellular is over the per-node budget (TS-001). A hub at the greenhouse door would make every node depend on one box.

## Options considered

| Option | Pros | Cons |
|---|---|---|
| Cloud inference over cellular | Most accurate model; model updated in one place | $82 per node plus $4 per month, so fails NFR-02 (eliminated in TS-001); ~1.1 mAh per image upload |
| On-node inference, results over LoRaWAN | Cheapest option that passes; lowest energy per check; each node works on its own; uses the farm's existing gateway | Small int8 model may lose accuracy; TensorFlow Lite Micro is new to the team; model updates need a visit to each node |
| Greenhouse hub (Pi 5, nodes on Wi-Fi) | Full-size model; model updated in one place | $74 per node at 4 nodes; the hub is a single point of failure; Wi-Fi image uploads cost more energy |

## Decision

We will run an int8 MobileNetV2 (α 0.35, 96 × 96 input) with TensorFlow Lite Micro on each node's ESP32-S3. Each check sends one 12-byte LoRaWAN uplink with the result; no images leave the node.

## Rationale

- TS-001 ranked this option highest (3.65 vs 3.35), but the sensitivity check showed that the result depended on its accuracy score.
- EXP-2026-10-14 measured 91.5% accuracy and 89.0% early blight recall on the ESP32-S3 with greenhouse test images, only 1.3 points below the float32 model. That is an accuracy score of 4, so this option wins under every weighting we tried.
- It has the lowest energy per check of the three options, which matters for NFR-03.
- It is about $22 per node cheaper than the hub option at 4 nodes.

## Consequences

- **Easier:** each node works on its own, and tiny radio messages keep energy use low.
- **Harder:** a new model must be flashed onto each node by hand, because LoRaWAN cannot carry model updates. That is why NFR-06 (update in under 5 minutes through a sealed USB-C gland) matters. Nobody can see the image behind an alert.
- **New risk:** accuracy may drop in light conditions that are not in the dataset: morning, evening and overcast (new risk R-08).
- **Requirement impact:** FR-D2 (send the alert image to the manager) cannot be met. We will propose removing it at the Design Review. FR-D1 (keep the last 50 images on the node) becomes more important, because it is now the only way to see what the model saw.

## Follow-up actions

- [x] Ask Ruth Amadi for permission to mount nodes on the plant rows (Amara, done 2026-10-20)
- [x] Order XIAO ESP32S3 Sense boards (Kofi, BOM E01)
- [ ] Experiment: accuracy in morning and late-afternoon light (Mei, issue #24)
- [ ] Keep the last 50 images on the SD card (Mei, issue #25)
