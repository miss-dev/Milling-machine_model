# Requirements

<!-- GUIDE: Draft v1 in Phase 1 and agree it with your mentor at the Phase 1 gate. After
     that, change requirements only through the change log at the bottom.
     See templates/examples/requirements-example.md for a complete worked example. -->

## How to write a good requirement

- Use **"The system shall …"**, one requirement per row.
- Say **what** the system must do, not **how** it does it. "Shall localize itself", "shall report the temperature every minute" and "shall flag defective parts" are requirements; "shall use a LiDAR", "shall use MQTT" and "shall use a neural network" are design decisions. The exception is a genuine constraint, such as hardware your mentor requires you to use.
- Make it **verifiable**: someone must be able to test, demonstrate, inspect or analyse it and say pass or fail.
- Any number belongs in a **performance requirement**, with a unit and a test condition.
- For anything learned from data, state the metric (accuracy, recall, precision, F1, mean error…) **and the data it is measured on**: a test set that was never used for training, collected in conditions like real use. "90% accuracy" on its own means nothing.
- **Mandatory** requirements must be met for the project to succeed. **Desirable** requirements are stretch goals.
- Every requirement traces back to the [use case](../00-project/overview.md#use-case) or a [constraint](../00-project/overview.md#constraints). If you cannot say where it comes from, question whether you need it.

**Verification methods:** **T** = Test (measured), **D** = Demonstration (observed working), **I** = Inspection (look at it or measure it once), **A** = Analysis (calculation or simulation).

**Status values:** Proposed → Agreed → In progress → Verified / Failed. Use *Removed* instead of deleting a row.

## 1. Functional requirements

### 1.1 Mandatory

| ID | The system shall… | Rationale / source | Verification | Test(s) | Status |
|---|---|---|---|---|---|
| FR-01 | EXAMPLE: detect signs of disease on the plant leaves in its camera view. | EXAMPLE: Use case step 2 | T | T-01 | Proposed |
| FR-02 | TODO | TODO | TODO | TODO | Proposed |

### 1.2 Desirable

| ID | The system shall… | Rationale / source | Verification | Test(s) | Status |
|---|---|---|---|---|---|
| FR-D1 | TODO | TODO | TODO | TODO | Proposed |

## 2. Performance requirements

<!-- GUIDE: Each performance requirement adds a number to a functional requirement.
     "Target" is what you are aiming for. "Minimum acceptable" is the threshold for a pass. -->

| ID | Related FR | Metric | Target | Minimum acceptable | Test conditions | Verification | Test(s) | Status |
|---|---|---|---|---|---|---|---|---|
| PR-01 | FR-01 | EXAMPLE: Share of diseased images detected (recall) | ≥ 90% | ≥ 80% | Test set of 200 diseased and 200 healthy images taken by the device on site, never used for training | T | T-01 | Proposed |
| PR-02 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | Proposed |

## 3. Non-functional requirements

<!-- GUIDE: Qualities rather than functions. Typical categories: safety, cost, size and
     weight, power and endurance, environment (temperature, water, dust), reliability,
     security, privacy and data protection, usability, maintainability (including software
     and model updates), documentation. -->

| ID | Category | The system shall… | Verification | Test(s) | Status |
|---|---|---|---|---|---|
| NFR-01 | Safety | EXAMPLE: have no exposed conductors, and protect its battery against short circuit and over-discharge. | I | — | Proposed |
| NFR-02 | Cost | TODO | I | — | Proposed |

## 4. Change log

<!-- GUIDE: Every change after Phase 1 is agreed gets a row. Requirements creep or get cut
     in every project. This log shows you managed that deliberately. -->

| Date | Requirement(s) | Change | Reason | Agreed with |
|---|---|---|---|---|
| TODO | — | v1 agreed | Phase 1 gate | TODO: mentor name |
