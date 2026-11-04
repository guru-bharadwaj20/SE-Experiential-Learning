"""Lab 6 - tests written to reach at least 90% line (statement) coverage
of daycare_fees.py. Each test targets lines the starter tests never ran."""
import pytest
from daycare_fees import extra_hours_fee, enrolment_allowed, pickup_status


# extra_hours_fee

def test_within_included_hours():
    assert extra_hours_fee("toddler", 20, False) == 0


def test_unknown_age_group_raises():
    with pytest.raises(ValueError, match="unknown age group"):
        extra_hours_fee("teen", 10, False)


def test_negative_hours_raises():
    with pytest.raises(ValueError, match="invalid hours"):
        extra_hours_fee("toddler", -1, False)


def test_sibling_discount_adds_five_included_hours():
    # toddler: 25 + 5 included, so 32 hours is 2 extra at 9/hr
    assert extra_hours_fee("toddler", 32, True) == 18


def test_infant_normal_rate():
    # infant: 20 included, 25 hours is 5 extra at 14/hr
    assert extra_hours_fee("infant", 25, False) == 70


def test_infant_long_hours_surcharge():
    # 45 hours is 25 extra, rate 14 + 5 + 3 = 22
    assert extra_hours_fee("infant", 45, False) == 550


# enrolment_allowed

def test_enrolment_allowed():
    assert enrolment_allowed(24, 2, False) is True


def test_immunisation_pending_old_enough():
    assert enrolment_allowed(12, 0, True) is True


def test_too_young_to_enrol():
    assert enrolment_allowed(5, 3, False) is False


# pickup_status

def test_aftercare_friday_on_time():
    # cutoff 20 + 10 = 30
    assert pickup_status(30, True, True) == "on_time"


def test_regular_late():
    # cutoff 10, late window is -5 to 9
    assert pickup_status(0, False, False) == "late"


def test_regular_overdue():
    assert pickup_status(-6, False, False) == "overdue"
