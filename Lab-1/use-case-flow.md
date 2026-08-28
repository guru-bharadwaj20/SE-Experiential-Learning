# Lab 1 - Use-Case Flow Specification

**Problem Statement #48 - Incident Escalation & On-Call Rotation Engine**

## UC-02: Escalate Incident

| Field | Value |
|---|---|
| Use Case ID | UC-02 |
| Primary Actor | Monitoring System |
| Secondary Actors | On-Call Engineer, Notification Gateway, Incident Commander |
| Trigger | A monitoring alert is received on the ingestion endpoint. |
| Related Requirements | FR-001, FR-003, FR-004, NFR-001 |

### Preconditions

1. A rotation schedule exists for the team that owns the alerting service.
2. An escalation ladder with at least two tiers is configured for that team.
3. The Notification Gateway is reachable and the responders' contact details are valid.

### Postconditions

- **Success:** The incident is in state `Acknowledged`, an owning engineer is recorded against it,
  and no further escalation tiers are fired.
- **Failure:** The incident is in state `Escalation Exhausted`, the Incident Commander has been
  notified, and every notification attempt is present in the audit log.

### Main Success Scenario

1. The Monitoring System posts an alert payload to the ingestion endpoint.
2. The system validates the payload and creates an incident record with severity and owning team.
3. The system queries the rotation schedule for the engineer on call at the current timestamp.
4. The system selects tier 1 of the team's escalation ladder and dispatches a notification through
   the Notification Gateway (SMS and push) within 3 seconds of ingestion.
5. The system starts the tier-1 acknowledgement timer, set to the configured timeout.
6. The On-Call Engineer receives the notification and acknowledges the incident from the web
   console or by SMS reply.
7. The system cancels the pending timer, sets the incident state to `Acknowledged` and records the
   acknowledging engineer and the elapsed response time.
8. The system writes the notification and acknowledgement events to the audit log.
9. The use case ends successfully.

### Alternate Flow - 6a. Tier-1 Engineer Does Not Acknowledge

- **6a1.** The tier-1 acknowledgement timer expires with no acknowledgement received.
- **6a2.** The system marks the tier-1 attempt as `Timed Out` and moves to the next tier of the ladder.
- **6a3.** The system resolves the secondary engineer for that tier and dispatches the notification,
  then starts that tier's timer.
- **6a4.** If an engineer acknowledges, the flow rejoins the main scenario at step 7.
- **6a5.** If every tier is exhausted with no acknowledgement, the system sets the incident to
  `Escalation Exhausted`, pages the Incident Commander on the override channel, and ends the use case
  unsuccessfully.

### Alternate Flow - 4a. Notification Gateway Unavailable

- **4a1.** The Notification Gateway returns an error or does not respond within the dispatch timeout.
- **4a2.** The system retries the dispatch on the next available channel for the same tier.
- **4a3.** If all channels for the tier fail, the system logs a `Dispatch Failed` event and advances
  immediately to the next tier rather than waiting for the timer to expire.
