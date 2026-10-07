# Dataset: LeafWatch leaves

> Worked example. See [examples/README.md](README.md).

- **Version:** v2
- **Owner:** Mei Lin
- **Created:** 2026-10-09
- **Where the files are:** the team's university OneDrive folder, `LeafWatch/datasets/v2/` (large-file policy in CONTRIBUTING.md)
- **Used by:** Leaf classifier v2 and v3 ([model card](model-card-example.md)), EXP-2026-10-14-int8-model-accuracy, T-01

## 1. Purpose

Training, validating and testing the leaf classifier that runs on each LeafWatch node (Detection subsystem). The test split is also the test set for PR-01 and PR-02, so T-01 uses it.

## 2. Source and licence

| Part | Source | Licence / permission | Personal data? |
|---|---|---|---|
| Public images: PlantVillage tomato subset, 2,400 images | PlantVillage dataset [1], downloaded 2026-10-02 | Licence terms saved with the download date in `licences/plantvillage.txt` | No: single leaves on plain backgrounds |
| Greenhouse images, 1,500 images | Research farm greenhouse, rows 1–4, 2026-10-05 to 2026-10-09, two XIAO ESP32S3 Sense boards | Permission from Ruth Amadi, greenhouse manager, 2026-10-02 | No: the cameras point down at the canopy only (NFR-05). Every image was checked for people while labelling; none were found |

[1] D. P. Hughes and M. Salathé, "An open access repository of images on plant health to enable the development of mobile disease diagnostics," arXiv:1511.08060, 2015.

## 3. Collection

**Greenhouse images.** Two Seeed XIAO ESP32S3 Sense development boards, with the same OV2640 camera module as the final node, on tripods 40 cm above the canopy, looking down at 30°. Camera on default auto-exposure and white balance, saving 320 × 240 JPEGs to the SD card. We captured at 08:00, 12:00 and 16:00 each day from Monday 2026-10-05 to Friday 2026-10-09, in rows 1–4 of the greenhouse: 15 sessions of about 100 images (50 per board). In each session, each board photographed about 10 plants, 5 images per plant, moving the tripod slightly between images. So the same plant appears many times in the data, which matters for the split (section 5).

The greenhouse is running a fungicide trial in which some plants are deliberately infected with early blight. We used the trial's records to choose plants, so that each row had similar numbers of healthy, early blight and other-problem plants. Deliberately varied: time of day, row, plant, and which side of the plant faced the camera. The week was mostly sunny.

**PlantVillage images.** 800 images per class, chosen at random (seed 42) from the tomato folders of the public dataset.

## 4. Contents and labels

| Class / label | Count | Notes |
|---|---|---|
| Healthy | 1,300 | 800 PlantVillage, 500 greenhouse |
| Early blight | 1,300 | 800 PlantVillage, 500 greenhouse |
| Other | 1,300 | 800 PlantVillage (leaf mould, septoria leaf spot and spider mite damage, about 267 of each); 500 greenhouse (leaf mould, nutrient deficiency and insect damage) |
| **Total** | 3,900 | 2,400 PlantVillage, 1,500 greenhouse |

- **Format:** JPEG. Greenhouse images are 320 × 240, as captured by the OV2640. PlantVillage images are 256 × 256. `labels.csv` lists each file with its class, source, row, plant ID, board, date and time.
- **Labelling:** Mei Lin labelled all greenhouse images in Label Studio, following a one-page rule sheet with example photos of each class (`src/ml/labelling-rules.md`). The main rule: if any early blight lesion is visible, the label is early blight, even if other problems are also visible. Ruth Amadi relabelled a random sample of 100 greenhouse images without seeing Mei's labels: 97% agreement. All 3 disagreements were leaves with more than one problem. PlantVillage labels were used as published, with leaf mould, septoria leaf spot and spider mite damage merged into "other".

## 5. Split

| Split | Count | How chosen |
|---|---|---|
| Train | 3,120 | All 2,400 PlantVillage images, plus 720 greenhouse images from rows 1–3 |
| Validation | 180 | Greenhouse images of 20% of the plants in rows 1–3, chosen at random by plant ID (seed 42). Used to choose the best training epoch |
| Test | 600 | Everything from row 4 (200 per class); never used for training or tuning |

The greenhouse images are split by row, not by image, because each plant was photographed many times. Row 4 is twice as long as each of rows 1–3, so on its own it gives the 200 images per class that PR-01 needs. PlantVillage images are used for training only, because they do not look like what the node sees.

**Split file or script:** `src/ml/splits/v2.csv`, made by `src/ml/scripts/make_split.py --by row --test-rows 4 --val-fraction 0.2 --seed 42`

## 6. Known limitations and biases

- **Season:** one week in October. The plants were at one growth stage.
- **Light:** daytime only, between 08:00 and 16:00, in a mostly sunny week. Nothing at dawn, at dusk or under heavy cloud (risk R-08).
- **Place and plants:** one greenhouse and one tomato variety.
- **Devices:** two boards. Camera modules vary, so a new node's colours may differ slightly.
- **Classes:** "other" mixes several problems, with few examples of each. Leaves with both early blight and another problem cause most of the model's errors; more are being collected (#26).
- **Labels:** labelled by one person who is not a plant pathologist, and checked on a 100-image sample only.

## 7. Version history

| Version | Date | Change | By |
|---|---|---|---|
| v1 | 2026-10-09 | Created. Random per-image split | Mei Lin |
| v2 | 2026-10-12 | Re-split by greenhouse row after review of PR #12 found the same plant in the training and test sets. Added a validation split by plant | Mei Lin |
