# Lab 5 - Issues Found and Fixed

**Name:** Guru R Bharadwaj | **SRN:** PES1UG24CS177 | **Section:** 5 C
**File:** `gym_membership_system.py` (repo `SETAPESU26/L5_48_gym_membership_system`)

Line numbers refer to the original file. Reports are in [reports/before](reports/before) and [reports/after](reports/after).

| Before | After |
|---|---|
| Pylint 4.81/10 | Pylint 10.00/10 |
| Bandit: 2 High, 1 Medium, 3 Low | Bandit: no issues |
| Flake8: 9 findings | Flake8: none |

## Issue table (high and medium severity first)

| # | Issue | Tool / Code | Severity | Line(s) | Description | Fix Approach |
|---|-------|-------------|----------|---------|-------------|--------------|
| 1 | Shell injection | Bandit B605 | High | 58 | `os.system("echo ... " + filename)` sends the filename to a shell. A name like `x.txt & del *` would run a second command. | Replaced with a plain `print()`. No shell is needed to show a message. |
| 2 | Weak hash | Bandit B324 | High | 47 | `hashlib.md5` is broken for anything security related. | Switched to `hashlib.sha256`. |
| 3 | Use of `eval` | Bandit B307, Pylint W0123 | Medium | 40-43 | `calculateRenewalRate` ran `eval()` on a string, so a caller could run any Python code. It also made `base_fee` look unused. | The function now takes a numeric `discount` (0 to <1), checks the range and computes `fee * (1 - discount)`. The call changed from `"base_fee * 0.85"` to `0.15`, and the result is still 510.0. |
| 4 | Hardcoded secret, printed to console | Bandit B105 | Low (but serious in practice) | 70, 79 | The portal secret was in the source and then printed to stdout. | Read from the `GYM_API_SECRET` environment variable. The program only reports whether it is set and never prints the value. |
| 5 | Bare `except` with `pass` | Bandit B110, Pylint W0702, Flake8 E722 | Low | 24-27 | Every error was swallowed silently, including typos and `KeyboardInterrupt`. | Catch only `KeyError` and return `False`/`True` so the caller knows whether the cancel worked. |
| 6 | Insecure random for PIN | Bandit B311 | Low | 51 | `random` is predictable, which matters for a locker PIN. | Use `secrets.randbelow(9000) + 1000`. |
| 7 | Mutable default argument | Pylint W0102 | Medium (bug) | 15 | `member_log=[]` is created once and shared across every call, so log entries leaked between calls. | Default is `None`, and a new list is created inside the function. |
| 8 | File not closed on error, no encoding | Pylint R1732, W1514 | Medium | 55-57 | `open()`/`close()` leaks the handle if `write` raises, and the encoding depends on the OS. | `with open(filename, "w", encoding="utf-8")`. |
| 9 | Parameter shadows global | Pylint W0621 | Medium | 61 | `get_active_summary(members)` hides the module-level `members`. | Renamed the parameter to `roster`. |
| 10 | Unused import / variables | Flake8 F401, F841; Pylint W0611, W0612 | Low | 6, 31, 41, 63 | `math`, `locker_deposit`, `base_fee` and loop variable `m` were never used. | Removed them. The loop now iterates over `.values()`. |
| 11 | `== None` comparison | Flake8 E711, Pylint C0121 | Low | 32 | Should be an identity check. | `is None`. |
| 12 | Lines too long, no final newline | Flake8 E501, W292; Pylint C0304 | Low | 10, 11, 18, 82 | Style violations. | Wrapped the lines and added the newline. |
| 13 | Naming and docstrings | Pylint C0103, C0116 | Low | 15-69 | camelCase function names, and no function had a docstring. | Renamed to snake_case (`register_member` and so on) and added a docstring to each function. |
| 14 | Redundant code | Pylint R1703, R1705, C0209 | Low | 19, 34-37 | An if/else returned True/False, and `%` formatting was used. | `return member["months_left"] > 0` and f-strings. |
| 15 | Code runs on import | Not flagged | Low | 82 | `main()` was called at module level, so importing the file would run the demo and write a file. | Wrapped in `if __name__ == "__main__":`. |

## Problems the tools did not flag

- Bandit flagged the hardcoded secret string but not the `print` that showed it on screen. I only noticed that by reading the program output.
- In the original output, "Roster exported to" appeared at the top, ahead of lines that were printed earlier. `os.system` writes straight to the console while Python's own `print` output is still buffered. Removing `os.system` fixed the order.
- `cancelMembership` gave no sign of failure for an unknown ID. It now returns `False`.

## Commits

1. `Fixed Bandit issues in Lab 5` (security fixes, plus the before reports)
2. `Fixed Flake8 issues in Lab 5` (style fixes)
3. `Fixed Pylint issues and added Lab 5 write-up` (Pylint fixes, after reports, this table and the reflection)
