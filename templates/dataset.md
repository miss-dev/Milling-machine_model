# Dataset: {{TITLE}}

- **Version:** v1 <!-- Bump the version whenever samples, labels or the split change, and add a row to the version history. -->
- **Owner:** {{AUTHOR}}
- **Created:** {{DATE}}
- **Where the files are:** TODO: this folder, or a link that follows the large-file policy in CONTRIBUTING.md
- **Used by:** TODO: models, experiments and tests, e.g. T-01

<!-- GUIDE: One card for every dataset you collect, label or download, including public ones.
     From this page alone, a reader should be able to tell where the data came from, whether
     you are allowed to use it, and whether results measured on it can be trusted. -->

## 1. Purpose

TODO: What this dataset is for, e.g. training and testing the fault classifier.

## 2. Source and licence

| Part | Source | Licence / permission | Personal data? |
|---|---|---|---|
| TODO: e.g. public images | TODO: name and link | TODO: e.g. CC BY 4.0 | TODO: e.g. No |
| TODO: e.g. data we collected | TODO: where, when, which device | TODO: e.g. permission from the site owner, 2026-10-01 | TODO |

<!-- GUIDE: If the data shows or describes people (faces, voices, locations, health, behaviour),
     talk to your mentor before collecting it. You may need consent or ethics approval. -->

## 3. Collection

TODO: Device or sensor and its settings, places, dates and times, conditions (lighting, weather, users), and anything you deliberately varied.

## 4. Contents and labels

| Class / label | Count | Notes |
|---|---|---|
| TODO | TODO | TODO |
| **Total** | TODO | |

- **Format:** TODO: file types, resolution or sample rate, units
- **Labelling:** TODO: who labelled, with which tool, following which written rules, and how the labels were checked (e.g. a second person relabelled a 10% sample: 96% agreement)

## 5. Split

<!-- GUIDE: Split by whatever makes samples similar to each other (person, plant, machine,
     recording session, site, day), not by individual sample. Otherwise near-identical samples
     end up in both the training and test sets, and your test results are too optimistic.
     Never tune anything on the test set. -->

| Split | Count | How chosen |
|---|---|---|
| Train | TODO | TODO |
| Validation | TODO | TODO |
| Test | TODO | TODO: e.g. everything from site 4; never used for training or tuning |

**Split file or script:** TODO: e.g. `src/ml/splits/v1.csv`, made by `make_split.py --seed 42`

## 6. Known limitations and biases

TODO: What the data does not cover, e.g. only daytime images, one device, one season, few examples of one class.

## 7. Version history

| Version | Date | Change | By |
|---|---|---|---|
| v1 | {{DATE}} | Created | {{AUTHOR}} |
