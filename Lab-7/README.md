# Lab 7 - Fuzz Testing with Hypothesis

Assigned repository: `SETAPESU26/L6_L7_48_daycare_fees`
Guru R Bharadwaj, PES1UG24CS177, Section 5 C

`daycare_fees.py` is this repo's version of `processor.py` from the handout, and `test_daycare_fees.py` is the `test_processor.py`. The script parses an enrolment like `toddler:25`, averages weekly hours given as CSV, and works out the fee after GST and a discount.

Against the original code, five of the six Hypothesis tests failed. The script crashed on `None`, on input with a missing `:` or `|`, and on empty values. The average was also wrong because of floor division (`0,1` gave 0), and the fee had float noise (`1|1` gave 0.17999999999999994). After the fix all six pass.

## Contents

| File | What it is |
|---|---|
| [daycare_fees/daycare_fees.py](daycare_fees/daycare_fees.py) | Fixed script |
| [daycare_fees/test_daycare_fees.py](daycare_fees/test_daycare_fees.py) | Hypothesis tests |
| [daycare_fees/screenshots](daycare_fees/screenshots) | Terminal output for each step |
| [Lab7_FuzzTesting_PES1UG24CS177.pdf](Lab7_FuzzTesting_PES1UG24CS177.pdf) | Report with screenshots |

## Running

```bash
cd daycare_fees
pip install hypothesis pytest
python daycare_fees.py
python -m pytest -v test_daycare_fees.py
```
