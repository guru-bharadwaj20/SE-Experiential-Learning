# Lab 2 - Epics and User Stories

Problem Statement #48: **Incident Escalation & On-Call Rotation Engine**

The functional and non-functional requirements from Lab 1 are decomposed here into five Epics
and eighteen User Stories. Every story carries a story point estimate on the Fibonacci scale, a
priority, and a reference back to the Lab 1 requirement it implements.

## OCE-1 - Epic 1: Alert Ingestion & Escalation Engine

Ingest inbound monitoring alerts, resolve the active on-call engineer, and drive the multi-tier escalation ladder until the incident is acknowledged. Covers FR-001 and FR-004.

**Priority:** High | **Stories:** 5 | **Points:** 29

| Key | User Story | As a | I want | So that | Points | Priority | Traces to |
|---|---|---|---|---|---|---|---|
| OCE-6 | Story 1.1: Alert Ingestion Endpoint | As a monitoring system | I want to push incident alerts to the engine over an authenticated webhook | So that every detected fault is registered as a trackable incident | 5 | High | FR-001 |
| OCE-7 | Story 1.2: Resolve Active On-Call Engineer | As a system | I want to look up the engineer currently on call from the rotation schedule when an alert arrives | So that the alert reaches a named human instead of a shared inbox | 3 | High | FR-001 |
| OCE-8 | Story 1.3: Timeout-Based Escalation to Secondary | As an incident commander | I want the engine to escalate to the secondary engineer when an alert is unacknowledged for 5 minutes | So that no P1 incident is silently dropped | 8 | Highest | FR-001 |
| OCE-9 | Story 1.4: Configure Escalation Ladder | As an incident commander | I want to define a per-team escalation ladder of up to five tiers | So that each team's severity policy is respected rather than a hard-coded default | 8 | Medium | FR-004 |
| OCE-10 | Story 1.5: Per-Tier Channel and Timeout | As an incident commander | I want to set the notification channel and timeout individually for each ladder tier | So that escalation pacing matches how urgently that team must respond | 5 | Medium | FR-004 |

## OCE-2 - Epic 2: On-Call Rotation Scheduling

Let an Incident Commander build and maintain time-zone-aware shift rotations that the escalation engine reads from. Covers FR-002.

**Priority:** High | **Stories:** 4 | **Points:** 16

| Key | User Story | As a | I want | So that | Points | Priority | Traces to |
|---|---|---|---|---|---|---|---|
| OCE-11 | Story 2.1: Create Rotation Schedule | As an incident commander | I want to create a rotation schedule and assign engineers to shifts | So that the team has a single authoritative source for who is on duty | 5 | High | FR-002 |
| OCE-12 | Story 2.2: Time-Zone-Aware Shift Definition | As an incident commander | I want to define each shift with a start time, end time and explicit time zone | So that handover across regions is unambiguous | 3 | High | FR-002 |
| OCE-13 | Story 2.3: Who-Is-On-Call Lookup | As an on-call engineer | I want to query who is on call at any given timestamp | So that I can confirm coverage before I step away | 3 | High | FR-002 |
| OCE-14 | Story 2.4: Edit Shifts and Swaps | As an on-call engineer | I want to edit or swap an assigned shift | So that cover can be arranged without editing the whole rotation | 5 | Medium | FR-002 |

## OCE-3 - Epic 3: Incident Acknowledgement & Response

Allow an On-Call Engineer to acknowledge an incident from the web console or by SMS reply, and stop the escalation ladder on acknowledgement. Covers FR-003.

**Priority:** High | **Stories:** 3 | **Points:** 16

| Key | User Story | As a | I want | So that | Points | Priority | Traces to |
|---|---|---|---|---|---|---|---|
| OCE-15 | Story 3.1: Acknowledge from Web Console | As an on-call engineer | I want to acknowledge an incident from the web console | So that I can claim ownership while working at my desk | 3 | High | FR-003 |
| OCE-16 | Story 3.2: Acknowledge by SMS Reply | As an on-call engineer | I want to acknowledge an incident by replying to the SMS notification | So that I can silence the ladder from my phone away from a laptop | 5 | High | FR-003 |
| OCE-17 | Story 3.3: Halt Escalation on Acknowledgement | As an on-call engineer | I want all further notifications for an incident to stop once it is acknowledged | So that I am not buried in an alert storm for work I already own | 8 | Highest | FR-003 |

## OCE-4 - Epic 4: Post-Mortem & Incident Closure

Capture root cause, timeline and action items for resolved incidents and surface any incident left without a post-mortem after 72 hours. Covers FR-005.

**Priority:** Medium | **Stories:** 3 | **Points:** 10

| Key | User Story | As a | I want | So that | Points | Priority | Traces to |
|---|---|---|---|---|---|---|---|
| OCE-18 | Story 4.1: Record Post-Mortem | As an incident commander | I want to record root cause, timeline and action items against a resolved incident | So that the team learns from the outage rather than repeating it | 5 | Medium | FR-005 |
| OCE-19 | Story 4.2: Flag Missing Post-Mortems | As an incident commander | I want the system to flag any incident with no post-mortem 72 hours after resolution | So that follow-up work does not quietly lapse | 3 | Medium | FR-005 |
| OCE-20 | Story 4.3: Pending Post-Mortem List | As an incident commander | I want to view a Pending Post-Mortem list | So that I can chase outstanding write-ups in one place | 2 | Low | FR-005 |

## OCE-5 - Epic 5: Platform Reliability & Auditability

Meet the dispatch-latency, availability and immutable-audit obligations the platform is held to. Covers NFR-001 and NFR-002.

**Priority:** High | **Stories:** 3 | **Points:** 16

| Key | User Story | As a | I want | So that | Points | Priority | Traces to |
|---|---|---|---|---|---|---|---|
| OCE-21 | Story 5.1: Sub-3-Second Alert Dispatch | As an on-call engineer | I want notifications to be dispatched within 3 seconds of alert ingestion | So that dispatch delay is not added to incident downtime | 8 | High | NFR-001 |
| OCE-22 | Story 5.2: Immutable Audit Trail | As an incident commander | I want an immutable audit entry for every schedule change, notification and acknowledgement | So that escalation disputes can be settled from the record | 5 | High | NFR-002 |
| OCE-23 | Story 5.3: Availability Monitoring & Uptime Report | As an incident commander | I want platform health monitoring with a monthly uptime report | So that we can prove the 99.9% availability commitment | 3 | Medium | NFR-002 |

## Totals

| | |
|---|---|
| Epics | 5 |
| User stories | 18 |
| Story points | 87 |

Story points follow the Fibonacci scale (1, 2, 3, 5, 8), reflecting the increasing uncertainty
attached to larger pieces of work rather than a linear measure of hours.
