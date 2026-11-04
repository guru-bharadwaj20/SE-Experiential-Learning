# Lab 6 - Code and Branch Coverage

Assigned repository: `SETAPESU26/L6_L7_48_daycare_fees`
Guru R Bharadwaj, PES1UG24CS177, Section 5 C

`daycare_fees.py` works out extra-hours fees, checks whether a child can be enrolled and reports pickup status. The starter tests were extended in two commits, the first for line coverage and the second for branch coverage.

| | Tests | Line coverage | Branch coverage |
|---|---|---|---|
| Starter | 2 | 38% | 32% |
| Code coverage tests | 12 | 100% | 98% |
| Branch coverage tests | 23 | 100% | 100% |

The code coverage tests ran every line but missed one branch (`21->23`): the nested infant check inside the long-hours surcharge had only come out True. The branch coverage tests add a toddler on long hours for that case, plus boundary values for every comparison.

## Contents

| File | What it is |
|---|---|
| [daycare_fees/daycare_fees.py](daycare_fees/daycare_fees.py) | Module under test, unchanged |
| [daycare_fees/test_daycare_fees.py](daycare_fees/test_daycare_fees.py) | Starter tests |
| [daycare_fees/CodeCoverageTest_daycare_fees.py](daycare_fees/CodeCoverageTest_daycare_fees.py) | Test cases for line coverage |
| [daycare_fees/BranchCoverageTest_daycare_fees.py](daycare_fees/BranchCoverageTest_daycare_fees.py) | Test cases for branch coverage |
| [daycare_fees/screenshots](daycare_fees/screenshots) | `code-coverage.png` and `branch-coverage.png`, terminal output for each run |

## Running

```bash
cd daycare_fees
pip install coverage pytest
coverage run -m pytest CodeCoverageTest_daycare_fees.py
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_daycare_fees.py
coverage report -m
```
