# Lab 1 - Requirements Engineering & UML Use-Case Modelling

Problem Statement #48: **Incident Escalation & On-Call Rotation Engine**
(Developer Tools & IT Operations)

A DevOps on-call management system that organises shift rotations, routes inbound monitoring
alerts through multi-tiered phone/SMS escalation ladders, and tracks incident post-mortems.

## Contents

| File | What it is |
|---|---|
| [requirements-table.md](requirements-table.md) | 5 functional + 2 non-functional requirements with priority, acceptance criteria and rationale, plus peer-critique notes |
| [use-case-diagram.pdf](use-case-diagram.pdf) | UML use-case diagram - 4 actors, 7 use cases, one «include» and one «extend» |
| [use-case-diagram.drawio](use-case-diagram.drawio) | Editable draw.io source for the diagram |
| [use-case-flow.md](use-case-flow.md) | Flow specification for UC-02 (Escalate Incident) with preconditions, postconditions, main success scenario and two alternate flows |

## Actors and Use Cases

**Actors:** Monitoring System, On-Call Engineer, Incident Commander, Notification Gateway

| ID | Use Case |
|---|---|
| UC-01 | Ingest & Triage Alert |
| UC-02 | Escalate Incident |
| UC-03 | Acknowledge Incident |
| UC-04 | Manage Rotation Schedule |
| UC-05 | Record Post-Mortem |
| UC-06 | Notify Responder (included by UC-02) |
| UC-07 | Broadcast Override Page (extends UC-02) |
