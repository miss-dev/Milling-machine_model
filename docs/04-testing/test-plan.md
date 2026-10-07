# Test Plan

<!-- GUIDE: Draft v1 at the Phase 2 gate (every mandatory FR and every PR has at least one
     test), refine it in Phase 3, and execute it in Phase 4. Results go in results.md, not
     here. This document says HOW you will test, so anyone on the team could run each test
     the same way. -->

## 1. Test strategy

| Level | What is tested | Where it is recorded | When |
|---|---|---|---|
| Component / experiment | A single part or idea (sensor noise, current draw, motor torque, message loss, model accuracy) | [experiments/](experiments/README.md) | Phases 2–3 |
| Subsystem | One subsystem on its own, against its interface spec | Subsystem doc + [experiments/](experiments/README.md) | Phase 3 |
| Integration | Two or more subsystems working together | [results.md](results.md) | Phases 3–4 |
| System validation | The full system against the requirements, in the final scenario | [results.md](results.md) | Phase 4 |

## 2. Test environment and equipment

<!-- GUIDE: Where tests happen and what you need, e.g. lab room, test course or field site,
     tape measure, stopwatch, multimeter or power profiler, camera for recording runs, laptop
     with logging set up, the frozen test dataset and the machine that runs the evaluation. -->

| Item | Details |
|---|---|
| Test location(s) | TODO |
| Measurement equipment | TODO |
| Recording | TODO: e.g. every validation run is filmed; logs saved to `data/` |

## 3. Test summary

| ID | Name | Level | Requirement(s) | Pass criteria | Owner | Planned date |
|---|---|---|---|---|---|---|
| T-01 | EXAMPLE: Detection on the held-out test set | Subsystem | FR-01, PR-01 | EXAMPLE: Recall ≥ 80% on the device, identical results on every device | TODO | TODO |
| T-02 | TODO | TODO | TODO | TODO | TODO | TODO |

## 4. Test procedures

<!-- GUIDE: One section per test, written precisely enough that a teammate could run it
     without asking you anything. Copy the block below for each test. -->

### T-01: EXAMPLE: Detection on the held-out test set

| Field | Details |
|---|---|
| **Objective** | EXAMPLE: Verify that the model, running on the device, detects enough diseased leaves in images it has never seen |
| **Requirements verified** | FR-01, PR-01 |
| **Elements tested** | EXAMPLE: Detection (model and on-device preprocessing) |
| **Location** | EXAMPLE: Lab bench |
| **Equipment** | EXAMPLE: 3 devices, microSD card with the test set, laptop with the evaluation script |
| **Setup** | EXAMPLE: Copy the test set (version recorded in its dataset card) to the microSD card. Check that none of its images appear in the training split. Flash the release firmware and note its commit hash and model version. |
| **Procedure** | EXAMPLE: 1. Insert the card and start the device in test mode. 2. The device classifies every image and logs the result, confidence and inference time. 3. Copy the log to `data/T-01-<date>/`. 4. Run `evaluate.py` on the log to compute recall, precision and the confusion matrix. 5. Repeat on the other two devices. |
| **Data recorded** | EXAMPLE: Prediction and confidence per image, inference time (ms), firmware commit, model version, test-set version |
| **Pass criteria** | EXAMPLE: Recall ≥ 80% (PR-01), and all 3 devices give identical predictions |
| **Number of trials** | EXAMPLE: 1 run of 400 images on each of 3 devices |

### T-02: TODO

TODO: Copy the table above.

## 5. Final validation scenario

<!-- GUIDE: The script for your final demonstration: the scenario, the steps and the metrics
     you will report. Base it on your use case. Rehearse it during Phase 4. -->

**Scenario:** TODO

**Steps:**

1. TODO

**Metrics reported:**

| Metric | Target | Requirement |
|---|---|---|
| TODO | TODO | TODO |
