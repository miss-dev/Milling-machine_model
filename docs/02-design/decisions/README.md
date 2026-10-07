# Design Decision Records

A design decision record (DDR) is a short note that captures **one** significant decision: the context, the options, what you chose and why. Six weeks from now nobody will remember why the sensor was changed or why you switched from Wi-Fi to LoRaWAN. A DDR records it.

Write a DDR when a decision:

- is hard or expensive to reverse (hardware purchases, platform, architecture, cloud service, model type), or
- affects more than one subsystem or person, or
- was debated, or went against the obvious choice.

Create one with:

```bash
python tools/new.py decision "Use MQTT for telemetry"
```

Never delete or rewrite an old DDR. If a decision changes, write a new DDR and set the old one's status to *Superseded by DDR-xxx*. See the [worked example](../../../templates/examples/DDR-002-example.md).

## Index

| ID | Decision | Status | Date |
|---|---|---|---|
<!-- index: new rows are added above this line -->
