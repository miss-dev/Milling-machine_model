# Requirements: LeafWatch (example)

> Worked example. See [examples/README.md](README.md).

## 1. Functional requirements

### 1.1 Mandatory

| ID | The system shall… | Rationale / source | Verification | Test(s) | Status |
|---|---|---|---|---|---|
| FR-01 | detect early blight on the tomato leaves in its camera view. | Use case step 2 | T | T-01 | Agreed |
| FR-02 | check its plants at least 3 times a day without anyone touching it. | Use case step 1; nobody visits every plant every day | D | T-02 | Agreed |
| FR-03 | send the result of every check, with air temperature, humidity and battery level, to a server. | Use case step 3 | D | T-02 | Agreed |
| FR-04 | email the greenhouse manager when early blight is detected. | Use case step 4 | D | T-03 | Agreed |
| FR-05 | show each node's latest result and history on a web dashboard. | Use case step 5 | D | T-03 | Agreed |

### 1.2 Desirable

| ID | The system shall… | Rationale / source | Verification | Test(s) | Status |
|---|---|---|---|---|---|
| FR-D1 | keep the last 50 images on the node for download during maintenance. | Lets the team and the manager see what the model saw | D | T-06 | Agreed |
| FR-D2 | send the image that triggered an alert to the manager. | The manager wants to confirm before spraying | D | — | Removed (see change log) |

## 2. Performance requirements

| ID | Related FR | Metric | Target | Minimum acceptable | Test conditions | Verification | Test(s) | Status |
|---|---|---|---|---|---|---|---|---|
| PR-01 | FR-01 | Early blight recall (share of diseased images detected) | ≥ 90% | ≥ 80% | Greenhouse test set: ≥ 200 images per class, taken by node cameras, never used for training | T | T-01 | Agreed |
| PR-02 | FR-01 | Early blight precision (share of early blight results that are correct) | ≥ 90% | ≥ 75% | As PR-01 | T | T-01 | Agreed |
| PR-03 | FR-04 | Time from the confirming check to email received | ≤ 2 min | ≤ 10 min | 4 nodes in the greenhouse, 20 triggered detections | T | T-03 | Agreed |
| PR-04 | FR-03 | Share of checks that reach the server | ≥ 98% | ≥ 95% | 4 nodes, 14-day greenhouse trial | T | T-05 | Agreed |

## 3. Non-functional requirements

| ID | Category | The system shall… | Verification | Test(s) | Status |
|---|---|---|---|---|---|
| NFR-01 | Safety | have no exposed conductors, and a battery protected against short circuit, overcharge and over-discharge. | I | — | Agreed |
| NFR-02 | Cost | cost no more than USD 60 in parts per node. | I | — | Agreed |
| NFR-03 | Endurance | run for at least 7 days on a full battery with no sunlight. | T | T-04 | Agreed |
| NFR-04 | Environment | keep working at 10–40 °C and up to 95% relative humidity. | T | T-05 | Agreed |
| NFR-05 | Privacy | not store or send images in which people can be identified. | I | — | Agreed |
| NFR-06 | Maintainability | allow the model on a node to be updated in under 5 minutes without opening the enclosure. | D | — | Agreed |

## 4. Change log

| Date | Requirement(s) | Change | Reason | Agreed with |
|---|---|---|---|---|
| 2026-09-18 | All | v1 agreed | Phase 1 gate | Dr. Sam Taylor |
| 2026-10-13 | PR-01, PR-02 | Test set changed from public PlantVillage images to greenhouse images taken by the node cameras | PlantVillage photos are single leaves on plain backgrounds and do not show what the node will see | Dr. Sam Taylor |
| 2026-10-30 | FR-D2 | Removed | A LoRaWAN uplink carries tens of bytes, not an image (DDR-002). Images are kept on the node instead (FR-D1) | Dr. Sam Taylor |
