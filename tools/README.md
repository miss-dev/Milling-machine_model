# Tools

Small helper scripts for this repository. They need Python 3.8+ and nothing else. Run them from the repository root.

| Script | What it does |
|---|---|
| `new.py` | Creates a document from a template (progress log, meeting notes, experiment, decision, trade study, subsystem, dataset card, model card, phase review), with the ID, date and author filled in, and adds it to the right index. See [templates/README.md](../templates/README.md). |
| `check_docs.py` | Finds broken relative links and images in the docs. `--todo` lists files that still contain `TODO` or `EXAMPLE` placeholders; `--strict` makes those fail too. Runs automatically on GitHub for every push and pull request. |

```bash
python tools/new.py --help
python tools/check_docs.py --todo
```

On some systems the command is `python3` rather than `python`.
