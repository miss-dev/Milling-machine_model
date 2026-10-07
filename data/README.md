# Data

Raw and processed data from experiments and tests (logs, measurements, CSV files, short recordings, rosbags, audio clips, image samples), and the documentation for every dataset the project uses.

## Experiment and test data

One folder per experiment or test run, named after its ID:

```
data/
├── EXP-2026-10-21-sleep-current/
│   ├── README.md
│   ├── run-01.csv
│   └── plot.png
└── T-01-2026-11-20/
    ├── README.md
    └── ...
```

`python tools/new.py experiment "<title>"` creates the folder and its README for you. Keep the README short:

- **What:** what was measured, and which experiment or test it belongs to (with link)
- **How:** how it was collected (script, sensor, rate) and the code version (commit hash)
- **Format:** file formats, column names, units, coordinate frames
- **Notes:** anything odd, e.g. "run 3 aborted at t = 12 s, battery disconnected"

## Datasets

<!-- GUIDE: Projects that train or evaluate a model, or that analyse a large collection of
     recordings. No datasets in your project? Delete this section. -->

A dataset (data you collect, label or download to train or evaluate a model) gets its own folder with a **dataset card**: where the data came from, its licence, how it was labelled, how it is split into training, validation and test sets, and what it does not cover. Write the card even when the files themselves live elsewhere. Create one with:

```bash
python tools/new.py dataset "Field images"
```

See the [worked example](../templates/examples/dataset-example.md).

| Dataset | Version | Used by | Owner |
|---|---|---|---|
<!-- index: new rows are added above this line -->

## Size

Keep files here small. Anything large (long recordings and rosbags, image or audio datasets, videos, model weights) follows the team's large-file policy in [CONTRIBUTING.md](../CONTRIBUTING.md#large-files). Link to where it lives from the folder's README.
