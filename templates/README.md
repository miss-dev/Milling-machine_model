# Templates

Blank templates for the documents you create repeatedly. **Don't copy these by hand.** Use the helper script, which fills in the ID, date and author, puts the file in the right place and adds it to the right index:

| Document | Command | Created at |
|---|---|---|
| Progress log | `python tools/new.py log "Your Name"` | `docs/06-reports/progress-logs/<your-name>/LOG-NN.md` |
| Meeting notes | `python tools/new.py meeting mentor` (or `team`, `standup`, `other`) | `docs/07-meetings/YYYY-MM-DD-<type>.md` |
| Experiment | `python tools/new.py experiment "Sleep current"` | `docs/04-testing/experiments/EXP-YYYY-MM-DD-<slug>.md` and `data/EXP-…/README.md` |
| Design decision | `python tools/new.py decision "Use MQTT for telemetry"` | `docs/02-design/decisions/DDR-NNN-<slug>.md` |
| Trade study | `python tools/new.py trade-study "Which microcontroller?"` | `docs/02-design/trade-studies/TS-NNN-<slug>.md` |
| Subsystem | `python tools/new.py subsystem "Sensing"` | `docs/03-subsystems/<slug>/README.md` |
| Dataset card | `python tools/new.py dataset "Field images"` | `data/<slug>/README.md` |
| Model card | `python tools/new.py model "Fault classifier"` | `docs/02-design/ml-models/<slug>.md` |
| Phase review | `python tools/new.py review 2` | `docs/06-reports/phase-reviews/phase-N-<name>.md` |

Run `python tools/new.py --help` for all options. The script needs Python 3.8 or newer and no extra packages. The author name defaults to your `git config user.name`. Override it with `--author "Name"`.

Single documents that exist only once (requirements, architecture, test plan, risk register and so on) are not here. They are already in `docs/`, ready to fill in.

## Worked examples

[examples/](examples/README.md) has a filled-in example of each document type for an imaginary AIoT project, *LeafWatch*. Read them to see the expected level of detail.
