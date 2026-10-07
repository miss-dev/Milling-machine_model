# Hardware

Physical design files: the things you would need to build the device again.

> **Software-only project?** Delete `cad/`, `electrical/` and `datasheets/`. Keep `bom.csv` if you pay for compute, cloud services, data plans or datasets, and delete the whole folder otherwise.

| Folder / file | Contents |
|---|---|
| [bom.csv](bom.csv) | Bill of materials: every part, bought or provided, with cost and status |
| [cad/](cad/README.md) | Mechanical CAD (structures, enclosures, mounts): source files, exports (STEP, STL) and drawings |
| [electrical/](electrical/README.md) | Schematics, PCB designs, wiring diagram, power budget |
| [datasheets/](datasheets/README.md) | Datasheets for every electronic part you depend on |

How each subsystem uses this hardware is described in its [subsystem document](../docs/03-subsystems/README.md).

## Bill of materials

[bom.csv](bom.csv) opens in Excel, Google Sheets or LibreOffice, and GitHub shows it as a table. Keep one row per part type.

| Column | Meaning |
|---|---|
| `id` | Short reference, e.g. `E01` (electronics), `M01` (mechanical), `P01` (power), `C01` (compute, cloud and data) |
| `item` | What it is |
| `part_number` | Manufacturer or supplier part number |
| `subsystem` | Which subsystem uses it |
| `qty` | Quantity |
| `unit_cost`, `total_cost` | Cost in the currency named in the `currency` column |
| `supplier`, `link` | Where it comes from |
| `status` | `planned`, `ordered`, `received`, `provided` (lent by lab or mentor), `returned` |
| `ordered_by`, `date_ordered` | Who ordered it and when |
| `datasheet` | Path in `datasheets/`, or a link |
| `notes` | Anything else, e.g. "spare", "replaced E03 after burnout" |

The first row is an example. Delete it once you have added your own parts.

## Rules

- **If it isn't in the BOM, don't buy it.** Add the row first with status `planned`.
- **Match the build.** By the Phase 3 gate, the CAD, schematics and wiring diagram match what is actually built. Photograph the wiring before closing the enclosure or chassis.
- **Export viewable formats.** Not everyone has your CAD tool. Always commit a STEP and a PDF or PNG drawing alongside the source file.
