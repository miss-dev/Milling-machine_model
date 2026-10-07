# Getting Started

This template is for engineering projects that build a working system and need to show, with evidence, that it meets its requirements: robots, embedded devices, IoT and AIoT systems, and AI / machine learning projects. The phases, requirements, design decisions, experiments, tests and reports work the same way for all of them. Section 3 below shows which parts to emphasise for your kind of project.

Do this in your first session, before writing any code. It takes about an hour and sets up the structure you will use for the rest of the project.

## 1. Create your repository from the template

1. On GitHub, open the template repository and click **Use this template → Create a new repository**. Name it after your project.
2. Clone **your new repository** (not the template):

   ```bash
   git clone https://github.com/<your-account>/<your-project>.git
   cd <your-project>
   ```

3. Team project: add every teammate and your mentor as collaborators (**Settings → Collaborators**).
4. Team project: protect `main` so changes arrive through reviewed pull requests (**Settings → Branches → Add rule**, require a pull request before merging).

## 2. Solo or team?

Everything in this repository works both ways. The differences are:

| | Solo | Team |
|---|---|---|
| [team.md](docs/00-project/team.md) | You and your mentor; you own every subsystem | Every member, their role and the subsystems they own |
| Progress logs | One folder: `progress-logs/<your-name>/` | One folder per member; each person writes their own |
| Meetings | Mentor meetings | Team meetings and mentor meetings |
| Pull requests | Optional but recommended, because they give a reviewable record of your work | Required: a teammate reviews before anything merges to `main` |
| Final report | No contribution statement | Individual contribution statements in the appendix |

## 3. What kind of project?

Use the row that fits best. Most projects mix two or more, e.g. an AIoT project is IoT plus ML.

| Project type | Typical subsystems | `hardware/` folder | Pay extra attention to |
|---|---|---|---|
| Robotics | Mechanical structure and drive, power, perception, localization, navigation, manipulation, user interface | All of it: CAD, electrical, datasheets, BOM | Safety and emergency stop, power budget, integration time, testing in the real environment |
| Embedded systems | Firmware, sensors, actuators, power, PCB, communication, enclosure | Electrical, datasheets and BOM; CAD for enclosures and mounts | Pin assignments, timing and memory budgets, power budget, testing on the real board |
| IoT | Device or node, connectivity, gateway, back end or cloud, dashboard or app | Electrical, datasheets, BOM and enclosure CAD | Message formats and interfaces, battery life, behaviour when the network drops, device credentials and firmware updates |
| AIoT / edge AI | IoT subsystems plus the dataset, the model and on-device inference | As IoT | Everything from IoT and ML, plus model size, latency and energy on the target hardware |
| AI / machine learning (software only) | Data pipeline, model, training and evaluation, inference service, user interface | Delete it, or keep only `bom.csv` to track paid compute, cloud services and data | [Dataset cards](data/README.md#datasets) and [model cards](docs/02-design/ml-models/README.md), a test set that is never used for training, baselines, reproducibility, privacy and ethics |

Folders you don't need can simply be deleted, e.g. `hardware/` in a software-only project, or `docs/02-design/ml-models/` if nothing is trained. But when a section of a project document does not apply (for example, the power budget in a software-only project), don't delete it silently. Write "Not applicable" and one line saying why, so your mentor can see you considered it.

## 4. Fill in the basics (Phase 1 starts now)

- [ ] [README.md](README.md): project name, one-liner, team, mentor, timeline, reporting cadence, tech stack
- [ ] [docs/00-project/team.md](docs/00-project/team.md): who does what and how you will work together
- [ ] [docs/05-management/schedule.md](docs/05-management/schedule.md): real dates for the five phases
- [ ] Agree the reporting cadence with your mentor (how often progress logs and meetings happen) and write it in the README

## 5. Set up GitHub Issues and Milestones

GitHub **Issues** are your task list and issue log. GitHub **Milestones** are your phases.

**Milestones** (**Issues → Milestones → New milestone**). Create one per phase, with the due date set to the gate date:

`Phase 1 — Define`, `Phase 2 — Design`, `Phase 3 — Build & Integrate`, `Phase 4 — Test & Validate`, `Phase 5 — Deliver`

**Labels** (**Issues → Labels**):

| Label | Use for |
|---|---|
| `type: task` | A piece of work to do |
| `type: bug` | Something that is broken (hardware or software) |
| `type: hardware` | Electronics, mechanical or enclosure work, purchasing |
| `type: docs` | Documentation work |
| `type: data` | Collecting, labelling or cleaning data; training and evaluating models (delete if you have no ML) |
| `subsystem: <name>` | One label per subsystem, created in Phase 2 when subsystems are defined |
| `priority: high` | Blocks other work or a gate |
| `blocked` | Cannot progress; say why in a comment |

If you have the [GitHub CLI](https://cli.github.com/) installed, you can create the labels in one go:

```bash
gh label create "type: task"     --color 0E8A16
gh label create "type: bug"      --color D73A4A
gh label create "type: hardware" --color FBCA04
gh label create "type: docs"     --color 0075CA
gh label create "type: data"     --color 5319E7
gh label create "priority: high" --color B60205
gh label create "blocked"        --color 000000
```

Optional: create a Project board (**Projects → New project → Board**) with columns *Todo, In progress, Review, Done*.

## 6. Learn the three habits

1. **Write it down where it belongs.** [CONTRIBUTING.md](CONTRIBUTING.md) has a "where does this go?" table. When in doubt, check it.
2. **Start documents with the helper script**, so the ID, date and structure are always right:

   ```bash
   python tools/new.py log "Ada Lovelace"          # your progress log
   python tools/new.py meeting mentor              # meeting notes
   python tools/new.py experiment "Sleep current"
   python tools/new.py decision "Use MQTT for telemetry"
   ```

   Run `python tools/new.py --help` for everything it can create. It needs Python 3.8+ and nothing else.
3. **A task is not done until its documentation is updated.** See the *Definition of done* in [CONTRIBUTING.md](CONTRIBUTING.md#definition-of-done).

## 7. Read the examples once

[templates/examples/](templates/examples/README.md) has a filled-in example of every document type, written for an imaginary AIoT project called *LeafWatch*: solar-powered camera nodes that detect plant disease on the device and send alerts over LoRaWAN. Read them once. They show the level of detail expected, whatever kind of system you are building.

## 8. Before every phase gate

1. Open [docs/05-management/phases.md](docs/05-management/phases.md) and work through the checklist for the phase.
2. Run `python tools/check_docs.py --todo` to find broken links and unfilled placeholders.
3. Write the phase review: `python tools/new.py review <phase-number>`.
