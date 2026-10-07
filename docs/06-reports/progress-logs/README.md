# Progress Logs

Each person writes their **own** progress log on the cadence agreed with the mentor (see the [README](../../../README.md)). Solo projects have one folder. Teams have one folder per member.

```
progress-logs/
├── ada-lovelace/
│   ├── LOG-01.md
│   └── LOG-02.md
└── alan-turing/
    └── LOG-01.md
```

Create your next log with:

```bash
python tools/new.py log "Ada Lovelace"
```

The script creates your folder the first time and numbers the logs for you.

## What makes a good progress log

- **Evidence over claims.** "Added deep sleep between readings (#23, PR #31); sleep current down from 18.5 mA to 0.09 mA, see EXP-2026-10-21-sleep-current" beats "worked on power saving".
- **Honest about plans.** Each log starts by checking the plan from your previous log. Missing a plan is normal; not explaining why is not.
- **Specific next steps.** "Finish the I2C driver for the humidity sensor and compare its readings with the reference meter" rather than "continue with the sensors".
- **Ask for help early.** The *Help needed* section is read by your mentor.

See the [worked example](../../../templates/examples/LOG-03-example.md).
