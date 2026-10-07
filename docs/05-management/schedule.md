# Schedule

<!-- GUIDE: Create in Phase 1 and update at every gate and whenever a date slips.
     Keep the original planned dates and add actual dates beside them. Comparing plan with
     reality is part of what you are assessed on. -->

## Phases and gates

| Phase | Planned start | Planned gate | Actual gate | Status |
|---|---|---|---|---|
| 1. Define | TODO | TODO | | Not started |
| 2. Design | TODO | TODO | | Not started |
| 3. Build and Integrate | TODO | TODO | | Not started |
| 4. Test and Validate | TODO | TODO | | Not started |
| 5. Deliver | TODO | TODO | | Not started |

**Status values:** Not started, On track, At risk, Late, Done

## Key events

<!-- GUIDE: Presentations, demos, submission deadlines, holidays, exam periods and lab
     closures. Anything that constrains your time. -->

| Event | Date | Presenter(s) | Deliverable |
|---|---|---|---|
| TODO: e.g. Concept Review | TODO | TODO | Phase 1 review and slides |
| TODO: e.g. Final presentation | TODO | TODO | Final slides, demo |

## Gantt chart

<!-- GUIDE: Replace the example tasks and dates with your own. Keep tasks at the level of
     about one to two weeks of work. Day-to-day tasks belong in GitHub issues.
     Syntax: https://mermaid.js.org/syntax/gantt.html -->

```mermaid
gantt
    title Example schedule - replace with your own tasks and dates
    dateFormat YYYY-MM-DD
    axisFormat %d %b

    section 1 Define
    Problem and research          :d1, 2026-09-07, 7d
    Requirements v1 and risks     :d2, after d1, 7d
    Concept Review                :milestone, g1, after d2, 0d

    section 2 Design
    Concepts and trade studies    :s1, after d2, 10d
    Architecture and subsystems   :s2, after s1, 7d
    BOM and ordering              :s3, after s1, 7d
    Test plan v1                  :s4, after s2, 4d
    Design Review                 :milestone, g2, after s4, 0d

    section 3 Build and Integrate
    Subsystem build and tests     :b1, after s4, 25d
    Integration                   :b2, after b1, 10d
    Integration Review            :milestone, g3, after b2, 0d

    section 4 Test and Validate
    Execute test plan             :t1, after b2, 10d
    Validation Demo               :milestone, g4, after t1, 0d

    section 5 Deliver
    Final report and slides       :f1, after t1, 10d
    Final Submission              :milestone, g5, after f1, 0d
```

## Schedule changes

<!-- GUIDE: Each time a planned date moves, record it. -->

| Date | What moved | From → To | Reason | Impact / recovery plan |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |
