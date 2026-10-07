# Machine Learning Models

<!-- GUIDE: Only for projects that train, fine-tune or adapt a model (on a microcontroller,
     single-board computer, server or phone). No learned model in your project? Delete this
     folder. -->

A model card is a short living document for one model: what it is for, what data it was trained on, how well it works on the test set, where it fails, and where each version is stored. Update it every time you train a new version, so anyone can tell which model is running and why it can be trusted. Create one with:

```bash
python tools/new.py model "Fault classifier"
```

Each model's training data has its own [dataset card](../../../data/README.md#datasets). Results that matter for a requirement are measured in an [experiment](../../04-testing/experiments/README.md) or a test, and linked from the card. See the [worked example](../../../templates/examples/model-card-example.md).

## Index

| Model | Current version | Subsystem | Key result | Owner |
|---|---|---|---|---|
<!-- index: new rows are added above this line -->
