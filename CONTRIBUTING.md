# Contributing

This file is the rulebook for this repository. It applies whether you work solo or in a team.

## Golden rules

1. **If it isn't written down, it didn't happen.** Tests, decisions, meetings and progress all get recorded.
2. **One place for each thing.** Use the table below. Do not keep project information in private notes, chats or personal drives.
3. **Link by ID.** Requirements, tests, risks and decisions have IDs. Refer to them by ID and link to them.
4. **`main` always works.** Do not merge code that breaks the build or the working system.
5. **A task is not done until its docs are updated** (see [Definition of done](#definition-of-done)).

## Where does this go?

| I have… | It goes in | Start it with |
|---|---|---|
| A paper, product or tutorial we are learning from | [docs/00-project/background.md](docs/00-project/background.md) | edit the file |
| A term others may not know | [docs/00-project/glossary.md](docs/00-project/glossary.md) | edit the file |
| A new requirement, or a change to one | [docs/01-requirements/requirements.md](docs/01-requirements/requirements.md) | edit the file and add to its change log |
| An idea, sketch or concept | [docs/02-design/concepts.md](docs/02-design/concepts.md), images in `docs/02-design/assets/` | edit the file |
| A comparison of options (sensor, board, network, algorithm, model…) | [docs/02-design/trade-studies/](docs/02-design/trade-studies/README.md) | `python tools/new.py trade-study "<question>"` |
| A decision we made, and why | [docs/02-design/decisions/](docs/02-design/decisions/README.md) | `python tools/new.py decision "<title>"` |
| How a subsystem works | `docs/03-subsystems/<subsystem>/README.md` | `python tools/new.py subsystem "<name>"` |
| A test of a component or an idea | [docs/04-testing/experiments/](docs/04-testing/experiments/README.md) | `python tools/new.py experiment "<title>"` |
| Raw data from that test | `data/<EXP-ID>/` | see [data/README.md](data/README.md) |
| A dataset we collect, label or download | `data/<dataset>/README.md` (the files follow the [large-file policy](#large-files)) | `python tools/new.py dataset "<name>"` |
| A trained model: what it is, its data, its results | [docs/02-design/ml-models/](docs/02-design/ml-models/README.md) | `python tools/new.py model "<name>"` |
| The result of a formal test from the test plan | [docs/04-testing/results.md](docs/04-testing/results.md) | edit the file |
| A new risk, or a change to an existing one | [docs/05-management/risk-register.md](docs/05-management/risk-register.md) | edit the file |
| A task, bug or problem to track | GitHub Issue | **Issues → New issue** |
| Notes from a meeting | [docs/07-meetings/](docs/07-meetings/README.md) | `python tools/new.py meeting <team\|mentor>` |
| What I did this period | `docs/06-reports/progress-logs/<my-name>/` | `python tools/new.py log "<my name>"` |
| The report for a phase gate | [docs/06-reports/phase-reviews/](docs/06-reports/phase-reviews/README.md) | `python tools/new.py review <1-5>` |
| CAD files and drawings | [hardware/cad/](hardware/cad/README.md) | |
| Schematics, PCB, wiring diagrams | [hardware/electrical/](hardware/electrical/README.md) | |
| A datasheet | [hardware/datasheets/](hardware/datasheets/README.md) | |
| A part we need or have bought | [hardware/bom.csv](hardware/bom.csv) | |
| Code | [src/](src/README.md) | |
| Photos, videos, poster | [media/](media/README.md) | |
| Something we learned the hard way | [docs/08-retrospective/lessons-learned.md](docs/08-retrospective/lessons-learned.md) | edit the file |

## IDs

IDs let documents point at each other. That is how you can show which test proves which requirement.

| Prefix | Meaning | Format | Lives in |
|---|---|---|---|
| `FR` | Functional requirement | `FR-01` | [requirements.md](docs/01-requirements/requirements.md) |
| `PR` | Performance requirement | `PR-01` | [requirements.md](docs/01-requirements/requirements.md) |
| `NFR` | Non-functional requirement | `NFR-01` | [requirements.md](docs/01-requirements/requirements.md) |
| `TS` | Trade study | `TS-001` | `docs/02-design/trade-studies/TS-001-<slug>.md` |
| `DDR` | Design decision record | `DDR-001` | `docs/02-design/decisions/DDR-001-<slug>.md` |
| `T` | Test in the test plan | `T-01` | [test-plan.md](docs/04-testing/test-plan.md) |
| `EXP` | Experiment | `EXP-2026-10-03-<slug>` | `docs/04-testing/experiments/` |
| `R` | Risk | `R-01` | [risk-register.md](docs/05-management/risk-register.md) |
| `LOG` | Progress log, numbered per person | `LOG-01` | `docs/06-reports/progress-logs/<name>/` |
| `#` | GitHub issue or pull request | `#12` | GitHub |

**Never reuse or renumber an ID.** Other documents point to it. If something is dropped, set its status to *Removed* and leave it in place.

## Writing documentation

- **Format:** GitHub-flavoured Markdown. Preview it on GitHub or in your editor before committing.
- **Placeholders:** text you must replace is marked `TODO`. Example rows in tables are marked `EXAMPLE`. Replace or delete them. `python tools/check_docs.py --todo` lists any that remain.
- **Guidance:** templates contain `<!-- guidance comments -->`. They are hidden when rendered and you can delete them once you no longer need them.
- **File names:** `lowercase-with-hyphens.md`, no spaces. Dates are always `YYYY-MM-DD`.
- **Images:** put them in an `assets/` folder next to the document that uses them, and name them descriptively (`2026-10-14-enclosure-v2-side.jpg`, not `IMG_4032.jpg`). Every figure gets a caption that says what it shows.
- **Diagrams:** prefer [Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams). GitHub renders it, and because it is text you can see what changed between versions. For diagrams Mermaid cannot do, commit the source file (draw.io, Figma export, etc.) alongside the PNG/SVG.
- **Tables over paragraphs** for anything you will compare or update (requirements, risks, results).
- **Numbers need units and conditions.** Write "0.42 m/s on carpet, 5 trials, σ = 0.03" or "87% recall on the 600-image test set", not "pretty fast" or "works well".
- **Link evidence.** When you say something works, link the experiment, data, video, commit or pull request that shows it.

## Git workflow

### Branches

- `main` always builds and runs.
- Do work on a branch named `<type>/<short-description>`, e.g. `feat/mqtt-telemetry`, `fix/sensor-i2c-address`, `docs/test-plan`.

### Commits

Write small commits that do one thing. The message format is `<type>: <what changed>`, with the issue number if there is one:

```
feat: add MQTT telemetry publisher (#14)
fix: correct I2C address of the humidity sensor
docs: add EXP-2026-10-03-sleep-current
hw: enclosure v2 STEP export and drawing
data: add labelled batch 3 (420 images) to dataset v2
test: add unit tests for the data loader
```

Types: `feat`, `fix`, `docs`, `test`, `hw`, `data`, `refactor`, `chore`.

### Pull requests

- One topic per pull request. Link the issue with `Closes #N`.
- Fill in the pull request template, including the documentation checklist.
- **Team:** at least one teammate reviews and approves before merging. Tag your mentor on major design changes.
- **Solo:** pull requests are optional but recommended. They give you, your mentor and your examiners a clean record of what changed and why.

## Issues

- Every task that takes more than about an hour, and every bug, gets an issue. Use the issue templates.
- Assign an owner, a phase milestone and labels.
- When you close an issue, leave a comment linking the evidence: the pull request, experiment or photo.
- GitHub Issues **is** the project's issue log. Do not keep a separate one.

## Definition of done

A task is done when all of the following that apply are true:

- [ ] Code is merged to `main` (through a reviewed pull request in a team) and runs
- [ ] The subsystem document is updated: status, how to run it, interfaces if they changed
- [ ] If you tested something, there is an experiment record or an updated [results.md](docs/04-testing/results.md), with data in `data/`
- [ ] If you made a design choice, there is a design decision record (DDR)
- [ ] If you changed a dataset or trained a new model version, its dataset card or model card is updated
- [ ] If a requirement's status changed, [requirements.md](docs/01-requirements/requirements.md) and [traceability.md](docs/01-requirements/traceability.md) are updated
- [ ] If you bought something, it is in [hardware/bom.csv](hardware/bom.csv)
- [ ] The issue is closed with a comment linking the evidence
- [ ] It appears in your next progress log

## Large files

GitHub warns about files over 50 MB and rejects files over 100 MB. Large binary files (videos, CAD assemblies, datasets, model weights) make the repository slow to clone for everyone. Your team decides how to handle them. Options include Git LFS, DVC (popular for datasets and models), a shared cloud folder or university storage. The `.gitignore` already keeps common model-weight files (`*.pt`, `*.pth`, `*.ckpt`, `*.safetensors`) out of git; edit it if your policy is different. Write your decision here and stick to it. Wherever large files end up, link them from the document that uses them.

> **Our large-file policy:** TODO

## Secrets

Never commit passwords, Wi-Fi credentials, API keys, tokens, or device keys and certificates for cloud or IoT services. Put them in a file that git ignores (`.env`, `secrets.h`, `*.key`, `*.pem`) and commit an example version with dummy values instead (`.env.example`, `secrets.example.h`). If you commit a secret by accident, tell your mentor and change the password or key straight away. Deleting the file does not remove it from git history.
