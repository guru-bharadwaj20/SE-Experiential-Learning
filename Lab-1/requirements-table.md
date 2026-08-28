# Lab 1 - Requirements Table

**Problem Statement #48 - Incident Escalation & On-Call Rotation Engine**
Domain: Developer Tools & IT Operations

## Scenario Summary

A DevOps on-call management system that organises team shift rotations, routes inbound
monitoring alerts through multi-tiered phone/SMS escalation ladders, and tracks incident
post-mortems.

Primary stakeholders: On-Call Engineer, Incident Commander.
Supporting actors: Monitoring System, Notification Gateway.

## Functional Requirements

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall ingest incident alerts, identify the active on-call engineer from the rotation schedule, and escalate to the secondary engineer if the alert is unacknowledged within 5 minutes. | High | Pass: escalation step is triggered on timeout. Fail: an unacknowledged P1 incident drops without escalation. | Core escalation behaviour; an unrouted P1 alert is the failure mode the system exists to prevent. |
| FR-002 | Functional | The system shall allow an Incident Commander to create and edit a rotation schedule by assigning engineers to shifts with a defined start time, end time and time zone. | High | A shift saved for 09:00-17:00 IST is returned by the "who is on call" lookup for any timestamp inside that window and not for one outside it. | Escalation is only correct if the underlying schedule is correct. |
| FR-003 | Functional | The system shall allow an On-Call Engineer to acknowledge an incident either from the web console or by replying to the SMS notification, and shall stop further escalation for that incident on acknowledgement. | High | After an ACK reply is received, no further notification is dispatched for that incident and its state reads "Acknowledged". | Prevents alert storms and lets responders silence the ladder from a phone. |
| FR-004 | Functional | The system shall allow an Incident Commander to configure a per-team escalation ladder of up to five tiers, specifying the notification channel and timeout for each tier. | Medium | A three-tier ladder saved with timeouts 5/10/15 minutes is applied in that order to the next incident raised for that team. | Teams differ in size and severity policy; a hard-coded ladder does not fit all of them. |
| FR-005 | Functional | The system shall let an Incident Commander record a post-mortem for a resolved incident, capturing root cause, timeline and action items, and shall flag any incident with no post-mortem 72 hours after resolution. | Medium | A resolved incident with no post-mortem appears in the "Pending Post-Mortem" list once 72 hours have elapsed. | Closes the incident lifecycle and keeps follow-up work visible. |

## Non-Functional Requirements

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Nonfunctional (Performance & Security) | Alert dispatch via webhook, SMS and email shall initiate within 3 seconds of alert ingestion. | High | Benchmarking confirms 95th-percentile dispatch latency under 3 seconds at a simulated peak of 200 alerts per minute. | Every second of dispatch delay is added directly to incident downtime. |
| NFR-002 | Nonfunctional (Availability & Auditability) | The system shall remain available 99.9% of the time each calendar month, and shall write an immutable audit entry for every schedule change, notification attempt and acknowledgement. | High | Monthly uptime report shows downtime under 44 minutes, and the audit log for a sample incident reconstructs its full escalation path. | The tool must be more reliable than the services it watches, and escalation disputes are settled from the audit trail. |

## Peer Critique Notes

| Req ID | Comment received | Revision made |
|---|---|---|
| FR-002 | "Schedule needs a time zone, otherwise handover across regions is ambiguous." | Added explicit time zone to the shift definition and to the acceptance criteria. |
| FR-004 | "Up to how many tiers? Unbounded is not testable." | Capped the ladder at five tiers and made the timeout per tier explicit. |
| NFR-001 | "Under what load, and which percentile?" | Restated as 95th percentile at 200 alerts per minute. |
