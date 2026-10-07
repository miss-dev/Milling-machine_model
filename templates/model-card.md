# Model: {{TITLE}}

- **Current version:** v1
- **Owner:** {{AUTHOR}}
- **Subsystem:** TODO
- **Code:** TODO: e.g. `src/ml/`
- **Weights:** TODO: where each version is stored (follow the large-file policy in CONTRIBUTING.md)
- **Last updated:** {{DATE}}

<!-- GUIDE: One card per model you train, fine-tune or adapt. It is a living document: update it
     with every new version. It says what the model is for, what it was trained on, how well it
     works and where it fails. Report results on the test set only, and link the experiment or
     test that measured them. -->

## 1. Intended use

TODO: What the model does, where it runs (microcontroller, single-board computer, server, phone) and who relies on its output. Also say what it must **not** be used for.

## 2. Requirements addressed

| Requirement | Metric and target |
|---|---|
| TODO: e.g. PR-01 | TODO: e.g. recall ≥ 80% on the test set |

## 3. Model

| Item | Details |
|---|---|
| Architecture | TODO: e.g. MobileNetV2, random forest, LSTM, fine-tuned language model |
| Inputs | TODO: shape, units and preprocessing (must be identical in training and in use) |
| Outputs | TODO: classes or values, and how confidence is reported |
| Starting point | TODO: trained from scratch, or pretrained weights (name, source, licence) |
| Size and speed | TODO: parameters, file size, latency and memory on the target hardware |

## 4. Training

| Item | Details |
|---|---|
| Dataset | TODO: link to the dataset card, and the version used |
| Code version | TODO: commit hash |
| Settings | TODO: config file, or the key hyperparameters and the random seed |
| Compute | TODO: e.g. Google Colab T4 GPU, 25 min |

## 5. Evaluation

<!-- GUIDE: Always compare with a simple baseline (e.g. always predict the most common class,
     or a threshold rule), so the reader can see what the model actually adds. -->

| Version | Test set | Result | Baseline | Evidence |
|---|---|---|---|---|
| v1 | TODO: dataset and version | TODO | TODO | TODO: EXP-… or T-… |

## 6. Limitations and risks

TODO: Conditions in which the model is known or expected to be wrong, any biases, and what the system does when the model is wrong.

## 7. Version history

| Version | Date | What changed | Why | By |
|---|---|---|---|---|
| v1 | {{DATE}} | First trained version | — | {{AUTHOR}} |
