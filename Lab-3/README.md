# Lab 3 - Component Modelling & Architectural Pattern Selection

Problem Statement #48: **Incident Escalation & On-Call Rotation Engine**
(Developer Tools & IT Operations)

Evaluate the candidate architectural styles for the on-call engine, select one, and model the
system as a UML component diagram with explicit provided and required interfaces.

## Contents

| File | What it is |
|---|---|
| [component-diagram.pdf](component-diagram.pdf) | UML component diagram - 6 internal components, 2 external systems, 7 interfaces in ball-and-socket notation |
| [component-diagram.drawio](component-diagram.drawio) | Editable draw.io source for the diagram |
| [architecture-justification.pdf](architecture-justification.pdf) | One-page written justification: style analysis, architectural choice, two reasons, security advantage, performance benefit |

## Architecture Selected

**Microservices.** The system splits along boundaries that are already stable, and their load
profiles, failure tolerance and rates of change all differ. What settled it is that the paging
path (ingest → escalate → notify) has to stay available when the post-mortem and console
workflows are not, and NFR-002's 99.9% target leaves no room for a single shared process to
guarantee that.

## Components

| Component | Responsibility |
|---|---|
| Alert Ingestion Service | Receives monitoring webhooks, normalises and de-duplicates alerts (FR-001) |
| Escalation Engine | Runs the escalation ladder, timers and acknowledgement state (FR-001, FR-003, FR-004) |
| Rotation Scheduler Service | Owns shifts, time zones and overrides; answers "who is on call" (FR-002) |
| Notification Gateway Service | Fans out to SMS, voice and e-mail; holds the carrier credentials (FR-001) |
| Incident & Audit Store | Persists incidents and the immutable audit log (NFR-002) |
| Web Console & Post-Mortem Service | Schedule editing, console acknowledgement, post-mortem capture (FR-005) |

External actors modelled at the boundary: the **Monitoring System** and the **SMS / Voice Carrier**.

## Interfaces

| Interface | Provided by | Required by | Protocol |
|---|---|---|---|
| IAlertIntake | Alert Ingestion Service | Monitoring System | HTTPS webhook |
| IEscalationControl | Escalation Engine | Alert Ingestion Service | gRPC |
| IOnCallLookup | Rotation Scheduler Service | Escalation Engine | REST / JSON |
| INotificationDispatch | Notification Gateway Service | Escalation Engine | async queue |
| IAckCallback | Escalation Engine | Notification Gateway Service | inbound SMS |
| IIncidentRepository | Incident & Audit Store | Escalation Engine, Web Console | SQL + append-only audit |
| IChannelAdapter | SMS / Voice Carrier | Notification Gateway Service | SMPP / SIP |
| IIncidentCommand | Escalation Engine | Web Console & Post-Mortem Service | HTTPS |

`IAckCallback` lets an engineer stop the ladder by replying to the SMS instead of opening the
console (FR-003), so the dependency between the engine and the gateway runs in both
directions: each provides one interface to the other.
