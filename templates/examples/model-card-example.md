# Model: Leaf classifier

> Worked example. See [examples/README.md](README.md).

- **Current version:** v3
- **Owner:** Mei Lin
- **Subsystem:** Detection
- **Code:** `src/ml/`
- **Weights:** every version on the team's university OneDrive folder, `LeafWatch/models/` (large-file policy in CONTRIBUTING.md). v3 is also compiled into the firmware as `src/firmware/components/detection/model_data.cc`
- **Last updated:** 2026-11-06

## 1. Intended use

The model runs on the ESP32-S3 microcontroller in each LeafWatch node. Three times a day it classifies a photo of tomato leaves as healthy, early blight or other. After the Detection subsystem's 2-of-3 vote, an early blight result triggers an email to the greenhouse manager, Ruth Amadi, who then inspects the plants. It is a screening tool that prompts a person to look.

It must **not** be used:

- to decide on its own whether to spray;
- on other crops, or to detect other diseases;
- on images that were not taken by a node camera about 40 cm above the canopy.

## 2. Requirements addressed

| Requirement | Metric and target |
|---|---|
| PR-01 | Early blight recall ≥ 90% (target), ≥ 80% (minimum) on the greenhouse test set |
| PR-02 | Early blight precision ≥ 90% (target), ≥ 75% (minimum) on the same test set |

## 3. Model

| Item | Details |
|---|---|
| Architecture | MobileNetV2, width multiplier α = 0.35, with a new 3-class output layer (DDR-006) |
| Inputs | 96 × 96 RGB image. Preprocessing: centre crop of the camera frame, bilinear resize to 96 × 96, then scaling to the int8 input range. Training (`src/ml/preprocess.py`) and the node (`preprocess.c`) must do exactly the same; EXP-2026-10-14 confirmed identical predictions on all 600 test images |
| Outputs | Softmax scores for healthy, early blight and other. After its 2-of-3 vote, Detection sends one class and a confidence of 0–255 in the uplink |
| Starting point | ImageNet-pretrained weights from Keras Applications (Apache License 2.0), fine-tuned on our data |
| Size and speed | About 0.41 M parameters. 0.42 MB as int8 (1.6 MB as float32). On the ESP32-S3 at 240 MHz: 780 ms per inference (σ 6 ms), with the 310 KB tensor arena in PSRAM. It took 610 ms with the arena in internal RAM, but that is not possible while the camera is running (#15) |

## 4. Training

| Item | Details |
|---|---|
| Dataset | LeafWatch leaves v2 ([dataset card](dataset-example.md)): 3,120 training images; the 180 validation images choose the best epoch |
| Code version | `5be81d7` (v2 training); `a3f9c21` (v3 conversion and export) |
| Settings | `src/ml/configs/mobilenetv2_96.yaml`, seed 42. Two stages: 10 epochs training only the new output layer (Adam, learning rate 1e-3), then 20 epochs fine-tuning all layers (learning rate 1e-4); batch size 32. Augmentation: flips, rotation up to ±20°, brightness and colour changes. v3 is v2 after post-training int8 quantisation with 200 representative training images, exported by `src/ml/scripts/export_tflm.py` |
| Compute | Google Colab T4 GPU, about 18 min |

## 5. Evaluation

All results are on the LeafWatch leaves v2 test split: 600 images from greenhouse row 4, 200 per class.

| Version | Test set | Result | Baseline | Evidence |
|---|---|---|---|---|
| v1 (float32, laptop) | Leaves v2, test split | 64.3% accuracy; early blight recall 58.5%, precision 71.3% | Always "healthy": 33.3% accuracy, 0% recall. Colour rule: 61.0% accuracy, 55.0% recall | EXP-2026-10-14 |
| v2 (float32, laptop) | Leaves v2, test split | 92.8% accuracy; recall 91.0%, precision 90.1% | As v1 | EXP-2026-10-14 |
| v3 (int8, on the ESP32-S3) | Leaves v2, test split | 91.5% accuracy; recall 89.0%, precision 89.4%; 780 ms per inference | As v1 | EXP-2026-10-14 |

The colour rule calls early blight when brown spots cover more than a set share of the leaf, "other" when yellow areas do, and healthy otherwise. Its thresholds were tuned on the training split (`src/ml/baselines.py`). v3 beats it by about 30 points of accuracy and 34 points of early blight recall, so the model earns its place. v1, trained on PlantVillage only, is barely better than the colour rule.

## 6. Limitations and risks

- **Low light:** early blight recall falls to 74% on images taken at 07:00 (EXP-2026-10-28-lighting). The dataset has no images before 08:00, so the first daily check was moved to 08:30 (#27).
- **Condensation:** in the early morning, condensation on the camera window blurs images, which gives false "other" results. The window has an anti-fog coating, and the check is skipped and retried after 30 minutes when humidity is above 95% (#29).
- **Leaves with more than one problem:** most errors are between early blight and other (28 of the 51 errors on the test set). More examples are being collected (#26).
- **Narrow training data:** one week in October, one greenhouse, one tomato variety and two camera boards. Expect accuracy to drop as the plants grow and the winter light changes. A disease the model has never seen is forced into one of the three classes; late blight, for example, may well be called early blight.

**When the model is wrong:** a single result never triggers an alert. Early blight must be reported with confidence ≥ 0.70 in 2 of the last 3 checks. The alert email asks Ruth Amadi to inspect the plants, not to spray. The node keeps the last 50 images and results on its SD card (FR-D1), so a wrong result can be checked afterwards.

## 7. Version history

| Version | Date | What changed | Why | By |
|---|---|---|---|---|
| v1 | 2026-10-08 | First trained version: float32, PlantVillage images only | A starting point while the greenhouse images were being collected | Mei Lin |
| v2 | 2026-10-12 | Retrained on LeafWatch leaves v2, adding 720 greenhouse images from rows 1–3 | PlantVillage photos are single leaves on plain backgrounds, not what the node sees (v1 later scored 64.3% on the greenhouse test set) | Mei Lin |
| v3 | 2026-10-14 | v2 quantised to int8 (post-training, 200 representative images) | To fit in memory and run in under 1 s on the ESP32-S3 (TS-001 option B; tested in EXP-2026-10-14) | Mei Lin |
