# EXP-2026-10-14-int8-model-accuracy: On-device accuracy of the quantised classifier

> Worked example. See [examples/README.md](README.md).

- **ID:** EXP-2026-10-14-int8-model-accuracy
- **Date(s):** 2026-10-14
- **Author(s):** Mei Lin
- **Subsystem:** Detection
- **Related requirements / tests:** PR-01, PR-02; supports TS-001 and DDR-002
- **Related issue:** #14
- **Code version:** `a3f9c21`
- **Data:** `data/EXP-2026-10-14-int8-model-accuracy/`
- **Status:** Complete

## 1. Objective

How much accuracy does the early blight classifier lose when it is quantised to int8 and run on the ESP32-S3, measured on greenhouse test images? And how long does one inference take?

## 2. Hypothesis / expected result

Post-training int8 quantisation usually costs 1–2 percentage points of accuracy [4 in TS-001]. The float32 model scored about 92% during validation, so we expect about 90% for the int8 model. Based on Espressif's examples for models of a similar size, we expect one inference to take less than 1 s at 240 MHz.

## 3. Setup

| Item | Details |
|---|---|
| Equipment | Seeed XIAO ESP32S3 Sense at 240 MHz (8 MB PSRAM); 8 GB microSD card holding the test images; USB-C cable to a laptop for the serial log. The same laptop runs the TensorFlow Lite interpreter for the comparison runs |
| Software and parameters | Models v1 (float32, PlantVillage only), v2 (float32) and v3 (int8), all trained with seed 42; v3's 200 representative images also chosen with seed 42. Node firmware built with ESP-IDF 5.2 and esp-tflite-micro, tensor arena (310 KB) in PSRAM. Its test mode reads images from the SD card instead of the camera, so every run uses the same images. Dataset LeafWatch leaves v2, test split: 600 images from greenhouse row 4, 200 per class |
| Environment | Lab bench. Lighting does not matter, because images are replayed from the SD card |

*[Photo of the setup goes here: the XIAO board on the bench with the microSD card inserted, connected by USB to the laptop showing the serial log. Embed it with `![Setup](assets/EXP-2026-10-14-setup.jpg)`.]*

## 4. Procedure

1. Evaluate the float32 models v1 and v2 on the 600 test images on the laptop (`src/ml/evaluate.py --split test`).
2. Convert v2 to int8 with post-training quantisation, using 200 representative images from the training split. This gives v3.
3. Evaluate v3 on the laptop with the TensorFlow Lite interpreter.
4. Copy the 600 test images to the SD card, flash the test firmware and run every image on the device. Log the class, confidence and inference time of each image over serial.
5. Check, image by image, that the device predictions equal the laptop int8 predictions.
6. Time each inference with `esp_timer`, from the call to the interpreter until it returns.

## 5. Results

All results are on the same 600 test images (200 per class).

| Model | Run on | Accuracy | Early blight recall | Early blight precision | Inference time | Size |
|---|---|---|---|---|---|---|
| v1 float32, PlantVillage only | Laptop | 64.3% | 58.5% | 71.3% | — | 1.6 MB |
| v2 float32 | Laptop | 92.8% | 91.0% | 90.1% | — | 1.6 MB |
| v3 int8 | Laptop | 91.5% | 89.0% | 89.4% | — | 0.42 MB |
| v3 int8 | ESP32-S3 | 91.5% | 89.0% | 89.4% | 780 ms (σ 6 ms) | 0.42 MB |

Confusion matrix for v3 on the ESP32-S3 (rows: actual class; columns: predicted class):

| Actual ↓ / Predicted → | Healthy | Early blight | Other |
|---|---|---|---|
| Healthy | 189 | 6 | 5 |
| Early blight | 9 | 178 | 13 |
| Other | 3 | 15 | 182 |

*[Plot goes here: the confusion matrix above as a colour-scaled image. Embed it with `![Confusion matrix](assets/EXP-2026-10-14-confusion-matrix.png)`.]*

## 6. Analysis

- Quantisation cost 1.3 points of accuracy (92.8% → 91.5%) and 2.0 points of early blight recall (91.0% → 89.0%). This is in the 1–2 point range the hypothesis predicted.
- The device predictions matched the laptop int8 predictions for all 600 images. This shows that the firmware's preprocessing matches the preprocessing used in training.
- Recall of 89.0% is just below PR-01's 90% target but well above its 80% minimum. Precision of 89.4% passes PR-02's 75% minimum.
- Most errors are between early blight and other: 13 early blight images were called "other" and 15 "other" images were called early blight. Most of these are leaves with both problems, or leaf mould spots that look like early blight lesions.
- The PlantVillage-only model (v1) scored 64.3%. Training on our own greenhouse images was essential.
- At 780 ms, one inference costs roughly 0.02 mAh at the board's ~100 mA active current, so it adds little to the energy budget.
- **Uncertainty:** with 200 early blight test images, the 95% confidence interval on recall is roughly ±4 points (about 85–93%). We cannot yet say whether the true recall is above or below the 90% target.
- **Variation between runs:** inference is deterministic, and a second run of all 600 images on the device gave identical results. Retraining v2 with three other seeds gave 92.0–93.3% accuracy, so the training seed moves the result by about ±1 point.
- **Limitations:** one week of images, row 4 only, and daytime light only (08:00–16:00). Labels were checked on a sample only. Images were replayed from the SD card, so the camera's auto-exposure and the enclosure window were not part of this test.

## 7. Conclusion

The int8 model on the ESP32-S3 detects 89% of diseased test images with 89% precision in 0.78 s, losing only 1.3 points of accuracy to quantisation. That is good enough for on-node inference (TS-001 option B), and it meets the PR-01 minimum.

## 8. Next steps

- [x] Share with team for DDR-002 (accepted 2026-10-16)
- [ ] Repeat with images taken at 07:00 and 17:00 (#24)
- [ ] Collect more images of leaves with both early blight and other problems (#26)
- [ ] Include inference in the node energy measurement (EXP-2026-10-21)
