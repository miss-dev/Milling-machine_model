# Concepts and Brainstorming

<!-- GUIDE: Phase 2, before you commit to a design. The goal is to show that you considered
     real alternatives before choosing. Put sketches and photos in docs/02-design/assets/.
     Hand sketches photographed on a phone are fine. -->

## 1. Break down the problem

<!-- GUIDE: List the functions the system must perform, independent of any hardware or
     software choice. Take them from your requirements. Typical functions: sense, process,
     detect or predict, decide, act (move, switch, display), communicate, store data, power,
     interact with the user. -->

| Function | From requirement(s) |
|---|---|
| TODO: e.g. Detect the event the user cares about | TODO: FR-01 |
| TODO | TODO |

## 2. Options for each function (morphological chart)

<!-- GUIDE: For each function, list at least 2–3 ways it could be done. Combining one option
     from each row gives you a complete concept. -->

| Function | Option A | Option B | Option C |
|---|---|---|---|
| TODO: e.g. Power | TODO: e.g. Mains adapter | TODO: e.g. Battery | TODO: e.g. Battery + solar |
| TODO: e.g. Connectivity | TODO: e.g. Wi-Fi | TODO: e.g. LoRaWAN | TODO: e.g. Cellular (LTE-M) |
| TODO: e.g. Where the model runs | TODO: e.g. On the device | TODO: e.g. On a local hub | TODO: e.g. In the cloud |
| TODO: e.g. Locomotion | TODO: e.g. Differential drive | TODO: e.g. Mecanum wheels | TODO: e.g. Tracks |

## 3. Concepts

<!-- GUIDE: At least 3 complete concepts. Each one gets a sketch, a short description and
     honest pros and cons. -->

### Concept A: TODO name

TODO: Add a sketch, e.g. `![Concept A sketch](assets/concept-a.jpg)`

**Description:** TODO

| Pros | Cons |
|---|---|
| TODO | TODO |

### Concept B: TODO name

TODO: Sketch, description, pros and cons.

### Concept C: TODO name

TODO: Sketch, description, pros and cons.

## 4. Concept selection

<!-- GUIDE: Compare the concepts with a trade study (python tools/new.py trade-study "...")
     and record the outcome as a design decision (python tools/new.py decision "...").
     Summarise and link them here. -->

**Selected concept:** TODO

**Trade study:** TODO: link to TS-xxx · **Decision:** TODO: link to DDR-xxx

## 5. Design iterations

<!-- GUIDE: Each time the physical design, the software or the model changes significantly, add a row.
     Before/after images make this one of the most convincing parts of a final report. -->

| Version | Date | What changed | Why | Image |
|---|---|---|---|---|
| v1 | TODO | Initial design | — | TODO |
