# Subsystems

<!-- GUIDE: Define your subsystems in Phase 2, based on the architecture. A good subsystem
     has one clear owner, a clear purpose and well-defined interfaces. Typical subsystems:
     - Robotics: mechanical structure and drive, power, perception, localization, navigation,
       manipulation, user interface
     - Embedded and IoT: sensing, firmware, power, enclosure, connectivity, gateway, back end,
       dashboard or app
     - AI / ML: data pipeline, model training and evaluation, inference (on a device or a
       server), user interface
     Match code folders in src/ to these names. -->

Each subsystem has its own folder with a `README.md` that describes its purpose, interfaces, hardware, software, tests and current status. Create one with:

```bash
python tools/new.py subsystem "Sensing"
```

The script adds a row to the table below. Keep the **Status** column up to date. Your mentor reads it to see where the project stands. See the [worked example](../../templates/examples/subsystem-example.md).

**Status scale:** Not started → Designing → Building → Testing → Integrated → Verified

## Index

| Subsystem | Owner | Status | Code | Notes |
|---|---|---|---|---|
<!-- index: new rows are added above this line -->
