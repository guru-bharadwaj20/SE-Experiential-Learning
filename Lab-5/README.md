# Lab 5 - Static Code Analysis

Assigned repository: `SETAPESU26/L5_48_gym_membership_system`
Guru R Bharadwaj, PES1UG24CS177, Section 5 C

The script was checked with Pylint, Bandit and Flake8, and fixed in three commits, one per tool.

| | Before | After |
|---|---|---|
| Pylint | 4.81/10 | 10.00/10 |
| Bandit | 2 High, 1 Medium, 3 Low | No issues |
| Flake8 | 9 findings | 0 |

## Contents

| File | What it is |
|---|---|
| [gym_membership_system.py](gym_membership_system.py) | Cleaned script |
| [issues.md](issues.md) | Issue table: what each tool found and how it was fixed |
| [reflection.md](reflection.md) | Answers to the reflection questions |
| [reports/before](reports/before) | `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` for the original file |
| [reports/after](reports/after) | The same three reports for the cleaned file |

## Running

```bash
pip install pylint bandit flake8
python gym_membership_system.py
pylint gym_membership_system.py
bandit -r gym_membership_system.py
flake8 gym_membership_system.py
```

The script reads an optional `GYM_API_SECRET` environment variable. It never prints the value, only whether the variable is set.
