import math

from hypothesis import given, settings, strategies as st
from daycare_fees import parse_enrolment, hours_average, payable_fee


@settings(max_examples=300)
@given(st.text() | st.none())
def test_parse_enrolment_no_crash(s):
    try:
        result = parse_enrolment(s)
    except Exception as e:
        assert False, f"parse_enrolment crashed with: {e!r}"
    if result is not None:
        age_group, hours = result
        assert age_group
        assert math.isfinite(hours) and hours >= 0


@settings(max_examples=300)
@given(st.text() | st.none())
def test_hours_average_no_crash(s):
    try:
        result = hours_average(s)
    except Exception as e:
        assert False, f"hours_average crashed with: {e!r}"
    if result is not None:
        assert math.isfinite(result) and result >= 0


@settings(max_examples=300)
@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    try:
        result = payable_fee(s)
    except Exception as e:
        assert False, f"payable_fee crashed with: {e!r}"
    if result is not None:
        assert math.isfinite(result) and result >= 0


@given(st.lists(st.integers(min_value=0, max_value=168), min_size=1))
def test_hours_average_matches_mean(values):
    csv = ",".join(str(v) for v in values)
    assert hours_average(csv) == round(sum(values) / len(values), 2)


@given(
    st.sampled_from(["infant", "toddler", "preschool"]),
    st.integers(min_value=0, max_value=60),
)
def test_parse_enrolment_valid_input(group, hours):
    assert parse_enrolment(f"{group}:{hours}") == (group.title(), float(hours))


@given(
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=0, max_value=100000),
)
def test_payable_fee_valid_input(fee, discount):
    expected = round(max(fee * 1.18 - discount, 0), 2)
    assert payable_fee(f"{fee}|{discount}") == expected
