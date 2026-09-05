# Lab 2 - Agile Backlog Creation & Sprint Simulation in Jira

Problem Statement #48: **Incident Escalation & On-Call Rotation Engine**
(Developer Tools & IT Operations)

The requirements identified in Lab 1 are converted here into an Agile backlog - Epics and User
Stories - which is prioritised, estimated with story points, and delivered across two sprints
on a Jira Scrum board.

## Contents

| File | What it is |
|---|---|
| [epics-and-user-stories.md](epics-and-user-stories.md) | 5 Epics and 18 User Stories in As-a / I-want / So-that form, with story points, priority and traceability to the Lab 1 requirements |
| [reflection.md](reflection.md) | Answers to the four reflection questions on estimation, prioritisation, sprint outcomes and burndown analysis |
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

| Sprint | Contents | Window | Committed |
|---|---|---|---|
| Sprint 1 | Epics 2 and 3 - 7 stories | Sat 5 Sep - Sun 6 Sep | 32 points |
| Sprint 2 | Sprint 1 carry-over and Epic 1 | Mon 7 Sep - Tue 8 Sep | Set from Sprint 1 velocity |

**Sprint 1 goal:** establish the rotation schedule and the acknowledgement path so escalation
has a correct foundation to build on.

**Sprint 2 goal:** deliver the alert ingestion and multi-tier escalation engine on top of
Sprint 1's scheduling and acknowledgement work.

Epics 4 and 5 remain in the backlog for subsequent sprints.

## Screenshots

| File | What it shows |
|---|---|
| `01-backlog-epics-and-story-points.png` | Backlog with the Epic panel open, showing Sprint 1 planned above the remaining backlog, with story points and priorities |
