"""Lab 6 - tests written to reach full branch coverage of daycare_fees.py.
Starts from the line coverage suite and adds the decision outcomes it
never took, plus boundary values for every comparison."""
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


# Branches the line coverage suite missed or only took one way

def test_toddler_long_hours_no_infant_surcharge():
    # extra > 20 but not infant: inner "if infant" goes False (21->23)
    # 50 hours is 25 extra, rate 9 + 5 = 14
    assert extra_hours_fee("toddler", 50, False) == 350


def test_infant_sibling_gets_no_discount():
    # has_sibling True but age_group is infant, so the bonus is skipped
    assert extra_hours_fee("infant", 25, True) == 70


def test_preschool_sibling_at_included_limit():
    # 30 + 5 included, exactly 35 hours gives extra == 0
    assert extra_hours_fee("preschool", 35, True) == 0


def test_zero_hours_is_valid():
    assert extra_hours_fee("infant", 0, False) == 0


def test_exactly_twenty_extra_hours_has_no_surcharge():
    # extra == 20 is not > 20, so the base rate applies
    assert extra_hours_fee("preschool", 50, False) == 180


def test_immunisation_pending_too_young():
    assert enrolment_allowed(11, 5, True) is False


def test_no_vacancies():
    assert enrolment_allowed(24, 0, False) is False


def test_six_months_is_old_enough():
    assert enrolment_allowed(6, 1, False) is True


def test_regular_weekday_on_time():
    assert pickup_status(10, False, False) == "on_time"


def test_aftercare_weekday_late():
    # cutoff 20, late window is 5 to 19
    assert pickup_status(5, True, False) == "late"


def test_regular_friday_overdue():
    # cutoff 20, below 5 is overdue
    assert pickup_status(4, False, True) == "overdue"
