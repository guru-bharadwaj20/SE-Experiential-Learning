"""Fitness gym membership registration and renewal module."""

import hashlib
import os
import secrets

members = {
    "M01": {"name": "Alex", "plan": "Gold", "months_left": 6, "fee": 600.0},
    "M02": {"name": "Brooke", "plan": "Silver", "months_left": 1,
            "fee": 350.0},
    "M03": {"name": "Chris", "plan": "Platinum", "months_left": 12,
            "fee": 1000.0},
}


def register_member(m_id, name, plan, months, member_log=None):
    """Add a new member and return True, or False if the ID is taken."""
    if member_log is None:
        member_log = []
    if m_id in members or months <= 0:
        return False
    members[m_id] = {"name": name, "plan": plan, "months_left": months,
                     "fee": 50.0 * months}
    member_log.append(f"Registered {m_id} for {months} months")
    return True


def cancel_membership(m_id):
    """Remove a member. Returns False if the ID does not exist."""
    try:
        del members[m_id]
    except KeyError:
        return False
    return True


def check_membership_status(m_id):
    """Return True if the member exists and has months left."""
    member = members.get(m_id)
    if member is None:
        return False
    return member["months_left"] > 0


def calculate_renewal_rate(m_id, discount):
    """Return the member's fee with a fractional discount (0 to <1)."""
    if not 0.0 <= discount < 1.0:
        raise ValueError("discount must be between 0 and 1")
    return members[m_id]["fee"] * (1 - discount)


def generate_member_hash(m_id):
    """Return a SHA-256 hex digest of the member ID."""
    return hashlib.sha256(m_id.encode()).hexdigest()


def generate_locker_pin():
    """Return a random 4-digit locker PIN."""
    return 1000 + secrets.randbelow(9000)


def export_member_roster(filename="gym_roster.txt"):
    """Write the member roster to a text file."""
    with open(filename, "w", encoding="utf-8") as roster_file:
        roster_file.write(str(members))
    print("Roster exported to: " + filename)


def get_active_summary(roster):
    """Count members in the roster that still have months left."""
    return sum(1 for details in roster.values()
               if details["months_left"] > 0)


def main():
    """Run a short demo of the membership functions."""
    gym_api_secret = os.environ.get("GYM_API_SECRET")
    register_member("M04", "Diana", "Gold", 3)
    cancel_membership("M02")
    print("Is M01 active:", check_membership_status("M01"))
    print("Renewal Fee:", calculate_renewal_rate("M01", 0.15))
    print("Member Hash:", generate_member_hash("M01"))
    print("Locker PIN:", generate_locker_pin())
    export_member_roster()
    print("Active count:", get_active_summary(members))
    print("Portal secret configured:", gym_api_secret is not None)


if __name__ == "__main__":
    main()
