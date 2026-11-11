import math

MAX_WEEKLY_HOURS = 168


def _to_number(value):
    if not isinstance(value, str):
        return None
    value = value.strip()
    if not value:
        return None
    try:
        number = float(value)
    except ValueError:
        return None
    if not math.isfinite(number) or number < 0:
        return None
    return number


def parse_enrolment(text):
    if not isinstance(text, str) or text.count(':') != 1:
        return None
    age_group, hours = text.split(':')
    age_group = age_group.strip()
    if not age_group:
        return None
    hours = _to_number(hours)
    if hours is None or hours > MAX_WEEKLY_HOURS:
        return None
    return age_group.title(), hours


def hours_average(hours_csv):
    if not isinstance(hours_csv, str):
        return None
    values = []
    for part in hours_csv.split(','):
        number = _to_number(part)
        if number is None or number > MAX_WEEKLY_HOURS:
            return None
        values.append(number)
    return round(sum(values) / len(values), 2)


def payable_fee(text):
    if not isinstance(text, str) or text.count('|') != 1:
        return None
    fee, discount = text.split('|')
    fee = _to_number(fee)
    discount = _to_number(discount)
    if fee is None or discount is None:
        return None
    total = fee * 1.18 - discount
    if not math.isfinite(total):
        return None
    return round(max(total, 0), 2)


def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    result = parse_enrolment(user_input)
    if result is None:
        print("Invalid input, expected something like toddler:25")
    else:
        print("Age Group and Hours:", result)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    result = hours_average(user_input)
    if result is None:
        print("Invalid input, expected numbers between 0 and 168 separated by commas")
    else:
        print("Average Hours:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    result = payable_fee(user_input)
    if result is None:
        print("Invalid input, expected two non-negative numbers like 3000|250")
    else:
        print("Payable Fee:", result)


if __name__ == "__main__":
    main()
