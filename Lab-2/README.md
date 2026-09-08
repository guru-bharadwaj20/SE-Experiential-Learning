# Lab 2 - Agile Backlog Creation & Sprint Simulation in Jira

Guru R Bharadwaj | SRN: PES1UG24CS177 | Section: 5-C

Problem Statement #48: **Incident Escalation & On-Call Rotation Engine**
(Developer Tools & IT Operations)

The requirements identified in Lab 1 are converted here into an Agile backlog - Epics and User
Stories - which is prioritised, estimated with story points, and delivered across two sprints
on a Jira Scrum board.

## Contents

| File | What it is |
|---|---|
| [epics-and-user-stories.pdf](epics-and-user-stories.pdf) | 5 Epics and 18 User Stories in As-a / I-want / So-that form, with story points, priority and traceability to the Lab 1 requirements |
| [reflection.pdf](reflection.pdf) | Answers to the four reflection questions on estimation, prioritisation, sprint outcomes and burndown analysis |
| [screenshots/](screenshots/) | Jira evidence - backlog, sprint boards, epic progress and burndown charts |

## Jira workspace

| | |
|---|---|
| Site | https://gururb.atlassian.net |
| Project | On-Call Rotation Engine (`OCE`) |
| Type | Company-managed Scrum |
| Board | OCE board |

## Epics

Each Epic groups the User Stories that implement one functional theme from the Lab 1
requirements table.

| Key | Epic | Traces to | Stories | Points |
|---|---|---|---|---|
| OCE-1 | Alert Ingestion & Escalation Engine | FR-001, FR-004 | 5 | 29 |
| OCE-2 | On-Call Rotation Scheduling | FR-002 | 4 | 16 |
| OCE-3 | Incident Acknowledgement & Response | FR-003 | 3 | 16 |
| OCE-4 | Post-Mortem & Incident Closure | FR-005 | 3 | 10 |
| OCE-5 | Platform Reliability & Auditability | NFR-001, NFR-002 | 3 | 16 |

18 User Stories, 87 story points. Estimates use the Fibonacci scale (1, 2, 3, 5, 8), whose
non-linearity reflects the growing uncertainty attached to larger items.

## Sprints

Epic 1 is the headline feature but was deliberately scheduled second: the escalation engine
cannot resolve who to page until the rotation schedule it reads from exists. Sprints 1 and 2
therefore build the foundation first and the engine on top of it.

| Sprint | Contents | Window | Committed | Completed |
|---|---|---|---|---|
| Sprint 1 | Epics 2 and 3 - 7 stories | Sat 5 Sep - Sun 6 Sep | 32 points | 24 points (Story 3.3 carried to Sprint 2) |
| Sprint 2 | Sprint 1 carry-over + 3 stories from Epic 1 - 4 stories | Sun 6 Sep - Tue 8 Sep | 24 points | 24 points (no carry-over) |

**Sprint 1 goal:** establish the rotation schedule and the acknowledgement path so escalation
has a correct foundation to build on.

**Sprint 2 goal:** deliver the alert ingestion engine and close out the acknowledgement-halt
story carried over from Sprint 1.

Sprint 1's burndown runs 32 - 24 - 21 - 8, ending above zero - the carry-over. Sprint 2's
commitment was set directly from Sprint 1's measured velocity (24 points) rather than repeating
the original 32-point assumption, and its burndown runs 24 - 16 - 8 - 0, a clean finish.

Epics 4 and 5 (26 points) remain in the backlog for subsequent sprints.

## Screenshots

| File | What it shows |
|---|---|
| `01-backlog-epics-and-story-points.png` | Backlog with the Epic panel open, Sprint 1 planned above the remaining backlog, story points and priorities visible |
| `02-active-sprint-board-day1.png` | Sprint 1 board, day 1 - To Do / In Progress / Done populated |
| `03-active-sprint-board-day2.png` | Sprint 1 board, day 2 - nearing completion, one story (the eventual carry-over) still open |
| `04-burndown-sprint1.png` | Sprint 1 burndown - 32 to 24 to 21 to 8, spanning the full Sat-Sun window with non-working days shown |
| `05-active-sprint2-board.png` | Sprint 2 board mid-flight |
| `06-epic-progress-overview.png` | All 5 epics' progress bars at a glance - Epics 2 and 3 complete, Epic 1 in flight, Epics 4 and 5 untouched |
| `07-burndown-sprint2.png` | Sprint 2 burndown - 24 to 16 to 8 to 0, ending exactly at zero |
