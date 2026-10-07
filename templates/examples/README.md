# Worked Examples: LeafWatch

These examples show what good documentation looks like in practice. They are written for an imaginary project, so the names, numbers and most references are invented. Two references are real: the PlantVillage paper and the LoRaWAN Regional Parameters. Use the examples for **structure and level of detail**. Don't copy their content.

## The example project

**LeafWatch** is a set of solar-powered camera nodes that watch tomato plants in a university research greenhouse. Each node detects early blight on the leaves with an on-device ML model, and the system alerts the greenhouse manager, Ruth Amadi, over LoRaWAN. A three-person undergraduate team builds it over one semester.

The examples use one AIoT project because it touches hardware, firmware, connectivity and machine learning at once. The same structure works for a robot, a pure embedded device or a software-only ML project.

| | |
|---|---|
| Team | Amara Okafor (project manager; server, dashboard and alerts), Kofi Mensah (hardware lead; node electronics, power, enclosure and LoRaWAN), Mei Lin (ML and test lead; dataset and model) |
| Mentor | Dr. Sam Taylor |
| Node | Seeed XIAO ESP32S3 Sense (ESP32-S3, OV2640 camera, 8 MB PSRAM), SX1262 LoRa module, SHT31 temperature and humidity sensor, 2000 mAh Li-ion cell with a 1 W solar panel, 3D-printed PETG enclosure; firmware on ESP-IDF 5.2 |
| Model | MobileNetV2 (α 0.35, 96 × 96 input) quantised to int8, running on the node with TensorFlow Lite Micro; classes healthy, early blight and other |
| Connectivity | LoRaWAN (class A, OTAA) through the farm's existing gateway and The Things Stack; one 12-byte uplink per check |
| Server | MQTT → Python ingest service → InfluxDB → Grafana dashboard on a university VM; email alerts |

## Examples

| Example | Shows how to write… | Template |
|---|---|---|
| [requirements-example.md](requirements-example.md) | Functional, performance and non-functional requirements | `docs/01-requirements/requirements.md` |
| [TS-001-example.md](TS-001-example.md) | A trade study with must-meet criteria, weights and a sensitivity check | [trade-study.md](../trade-study.md) |
| [DDR-002-example.md](DDR-002-example.md) | A design decision record | [design-decision.md](../design-decision.md) |
| [EXP-2026-10-14-example.md](EXP-2026-10-14-example.md) | An experiment with a hypothesis, procedure, results and analysis | [experiment.md](../experiment.md) |
| [LOG-03-example.md](LOG-03-example.md) | An individual progress log | [progress-log.md](../progress-log.md) |
| [meeting-example.md](meeting-example.md) | Mentor meeting notes | [meeting-notes.md](../meeting-notes.md) |
| [subsystem-example.md](subsystem-example.md) | A subsystem document | [subsystem.md](../subsystem.md) |
| [dataset-example.md](dataset-example.md) | A dataset card: source, licence, labelling and a split that avoids leakage | [dataset.md](../dataset.md) |
| [model-card-example.md](model-card-example.md) | A model card: intended use, results against baselines, limitations | [model-card.md](../model-card.md) |
| [phase-2-review-example.md](phase-2-review-example.md) | A phase review, including the mentor's assessment | [phase-review.md](../phase-review.md) |

Most cross-references in the examples (FR-01, DDR-002, #15, etc.) are written as plain text, because the documents they refer to don't exist in this template. In your project, make them links.
