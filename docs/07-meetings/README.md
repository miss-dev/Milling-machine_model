# Meeting Notes

Take notes at every mentor meeting and every team meeting where something is decided. One person takes notes and commits them the same day. In a team, rotate the role.

Create notes with:

```bash
python tools/new.py meeting mentor     # or: team, standup, other
```

Files are named `YYYY-MM-DD-<type>.md`, so they sort by date automatically.

## Rules

- **Decisions** are written down explicitly. If a decision is significant, it also gets a [DDR](../02-design/decisions/README.md).
- **Action items** always have an owner and a due date. Turn them into GitHub issues if they take more than about an hour.
- **Review the previous meeting's open actions** at the start of each meeting.

See the [worked example](../../templates/examples/meeting-example.md).
