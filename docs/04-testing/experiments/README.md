# Experiments

An experiment answers one specific question about a component, an idea or a subsystem. For example: *How much current does the board draw in deep sleep? How many LoRa messages are lost at 300 m? Does the PID controller hold a heading on carpet? How much accuracy does the model lose when it is quantised to int8?*

Run experiments early and often. They catch problems while there is still time to fix them. Create one with:

```bash
python tools/new.py experiment "Sleep current"
```

Put the raw data in `data/<EXP-ID>/` (see [data/README.md](../../../data/README.md)). The script adds a row to the index below. Fill in the *Outcome* column when the experiment is finished. See the [worked example](../../../templates/examples/EXP-2026-10-14-example.md).

## Index

| ID | Question | Subsystem | Related requirement(s) | Outcome | Author |
|---|---|---|---|---|---|
<!-- index: new rows are added above this line -->
