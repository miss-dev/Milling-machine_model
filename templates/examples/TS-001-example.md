# TS-001: Where should LeafWatch run its disease classifier?

> Worked example. See [examples/README.md](README.md).

- **ID:** TS-001
- **Date:** 2026-10-09
- **Author(s):** Mei Lin, Amara Okafor
- **Related requirements:** FR-01, PR-01, NFR-02, NFR-03
- **Resulting decision:** DDR-002

## Question

Where should LeafWatch run the classifier that detects early blight, so that it can meet PR-01 (≥ 80% recall) within the per-node budget (NFR-02) and on battery and solar power alone (NFR-03)?

## Options

| Option | Description | Key specs | Cost |
|---|---|---|---|
| A: Cloud inference over cellular | Node uploads each ~25 KB JPEG over LTE-M; a server runs a full-size model | ~95% accuracy reported for server-size models [3]; ~20 s upload per image | $82 per node, plus $4 per month data |
| B: On-node inference | Int8 MobileNetV2 runs on the node's ESP32-S3; only a 12-byte result is sent over LoRaWAN, which carries tens of bytes per uplink at its slowest data rates [2] | ~88% reported for similar int8 models on PlantVillage tomato classes [4], unknown on our images; < 1 s inference expected | $52 per node |
| C: Greenhouse hub | Nodes send JPEGs over the hub's own Wi-Fi to a Raspberry Pi 5 at the greenhouse door (mains socket); the hub runs a larger model and forwards results over LoRaWAN | ~95% (same model as A) | $44 per node, plus a $120 hub shared by all nodes |

## Must-meet criteria

| Must-meet criterion | A | B | C |
|---|---|---|---|
| Node parts ≤ $60 (NFR-02) | **Fail**: $82 per node, plus $4 per month data | Pass ($52) | Pass ($44; the $120 hub is shared and counted in the project budget) |
| No mains power needed at the node | Pass | Pass | Pass |

Option A is eliminated. It is still scored below for comparison.

## Weighted criteria

| Criterion | Weight | What a 5 looks like | What a 1 looks like |
|---|---|---|---|
| Accuracy on greenhouse images | 30 | ≥ 95% | < 70% |
| Implementation effort and risk | 25 | Team has done it before; well-documented libraries | New to the team; many unknowns |
| Energy per check (radio plus processing) | 20 | < 0.1 mAh | > 1 mAh |
| Cost per node, including a share of shared hardware at 4 nodes | 15 | < $40 | > $80 |
| Robustness | 10 | Each node works on its own | One failure stops every node |
| **Total** | **100** | | |

For accuracy, 4 = 90–95%, 3 = 85–90% and 2 = 70–85%.

## Scoring

| Criterion (weight) | A | B | C |
|---|---|---|---|
| Accuracy (30) | 5 | 3 | 5 |
| Effort and risk (25) | 4 | 3 | 3 |
| Energy (20) | 1 | 5 | 3 |
| Cost (15) | 1 | 4 | 2 |
| Robustness (10) | 3 | 4 | 2 |
| **Weighted total** | 3.15 (eliminated) | **3.65** | 3.35 |

## Justification of scores

- **B accuracy 3:** similar int8 models report ~88% on PlantVillage tomato classes [4]. But PlantVillage photos are single leaves on plain backgrounds, and ours will be harder. To be measured by experiment EXP-2026-10-14 before the decision is final.
- **A and C accuracy 5:** a full-size model on a server or a Pi 5 has no memory limit.
- **B effort 3:** TensorFlow Lite Micro on the ESP32-S3 is new to the team, but Espressif's examples cover a similar model.
- **A energy 1:** an LTE-M image upload takes about 20 s at ~200 mA (≈ 1.1 mAh) [5].
- **C cost 2:** $44 + $120 / 4 = $74 per node at 4 nodes.
- **C robustness 2:** if the hub or its Wi-Fi fails, every node goes blind.

## Sensitivity check

| Change | B | C | Winner |
|---|---|---|---|
| None (baseline) | 3.65 | 3.35 | B |
| Accuracy 40, Effort 15 | 3.65 | 3.55 | B |
| Accuracy 40, Energy 10 | 3.45 | 3.55 | **C** |
| As above, with B's accuracy scored 4 (if the experiment confirms ≥ 90%) | 3.85 | 3.55 | B |

The winner flips when accuracy is weighted more heavily. So the decision depends on B's accuracy score, which comes from someone else's dataset. If B reaches 90% on our greenhouse images, it wins in every case we tried. We therefore ran EXP-2026-10-14 before accepting it.

## Recommendation

Option B: on-node inference, provided the experiment shows ≥ 90% accuracy on greenhouse images, run on the ESP32-S3. Revisit option C if it does not.

## References

1. LeafWatch requirements, v1.
2. LoRa Alliance, *LoRaWAN Regional Parameters* (RP002).
3. Example reference for server-side plant disease classification accuracy, invented for this example.
4. Example reference for int8 MobileNet accuracy on PlantVillage, invented for this example.
5. Example LTE-M module datasheet, invented for this example.
