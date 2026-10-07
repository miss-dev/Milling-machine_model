# LOG-03: Progress Log, Mei Lin

> Worked example. See [examples/README.md](README.md).

- **Author:** Mei Lin
- **Date:** 2026-10-16
- **Period covered:** 2026-10-12 → 2026-10-16
- **Current phase:** Phase 2, Design
- **Hours this period:** 12

## 1. Review of last period's plan

| Planned | Done? | If not, why |
|---|---|---|
| Finish the greenhouse dataset (1,500 labelled images) | ✅ done | |
| Finish TS-001 inference location trade study | ✅ done | |
| Get TensorFlow Lite Micro running on the ESP32-S3 together with the camera | ⚠️ partly | The model runs, but the firmware crashes when the camera is also started (see Challenges) |
| Order microSD cards for the nodes | ❌ not done | Waiting for budget approval from the department; Amara is following up |

## 2. Summary

The quantisation experiment confirmed that the int8 model keeps 91.5% accuracy when it runs on the ESP32-S3. That was the main open question behind our inference choice, and DDR-002 is now accepted. The firmware crash when the camera and the model run together is worked around, but at the cost of slower inference.

## 3. Work completed

| Work | Evidence |
|---|---|
| Greenhouse dataset v2: 1,500 labelled images, split by greenhouse row | PR #12; dataset card (LeafWatch leaves v2) |
| int8 model accuracy experiment on the ESP32-S3, 600 test images | EXP-2026-10-14-int8-model-accuracy; data in `data/EXP-2026-10-14-int8-model-accuracy/` |
| TS-001 trade study finished, with sensitivity check added after mentor feedback | TS-001; meeting 2026-10-13 |
| Wrote DDR-002 with Amara | DDR-002 |
| Investigated the firmware crash when camera and model start together | Issue #15 (7 comments) |

## 4. Challenges

**Firmware aborts when the camera and the model start together (issue #15).** At start-up, the firmware aborts when both the camera driver and the model are initialised. The model's 310 KB tensor arena and the camera's frame buffers both want internal RAM, and the allocation fails.

- Tried: a smaller tensor arena. The model then fails to allocate its tensors.
- Tried: a lower camera resolution. It still fails.
- **Current workaround:** allocate the tensor arena in PSRAM with `heap_caps_malloc(..., MALLOC_CAP_SPIRAM)`. Inference slows from 610 ms to 780 ms. That is still well under 1 s, so it is not blocking. I used the PSRAM build for EXP-2026-10-14 so that the timing matches the real node.

## 5. Teamwork

- Kofi finished the enclosure v1 CAD. In the 13 Oct meeting we agreed that the camera sits 40 cm above the canopy, which is the height I used for data collection.
- Amara reviewed PR #12 and caught that the training script split images randomly, so photos of the same plant were in both the training and test sets. We switched to a split by greenhouse row, and test accuracy dropped from 97% to a more honest 92.8%.
- I helped Kofi set up the current measurement for the node sleep-current experiment (EXP-2026-10-21).

## 6. Plan for next period

- [ ] Merge the PSRAM fix and document it in the Detection subsystem doc (#15)
- [ ] Repeat the experiment with images taken at 07:00 and 17:00 (#24)
- [ ] Draft procedures for T-01 and T-02 in the test plan
- [ ] Collect and label 300 more images of leaves with mixed problems (#26)

## 7. Risks and blockers

- R-04 (model not accurate enough on greenhouse images) reduced from 12 to 6 after the experiment. Updated in the risk register.
- New risk R-08: accuracy may drop in morning, evening or overcast light, because the dataset only has images from 08:00 to 16:00. Added to the register; the experiment in #24 will tell us.
- The microSD card order is blocked on budget approval (Amara is following up).

## 8. Help needed from mentor

Is there a plant pathologist in the agriculture department who could check a sample of our labels? We are not experts, and label errors would make our accuracy numbers meaningless.
