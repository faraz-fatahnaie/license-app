from datetime import datetime


def compare_dates(c_date, e_date):
    # Parse the datetime strings into datetime objects
    datetime_current = datetime.fromisoformat(c_date)
    datetime_expiry = datetime.fromisoformat(e_date)

    # Remove the time part by extracting the date
    date_current = datetime_current.date()
    date_expiry = datetime_expiry.date()

    print(date_current)
    print(date_expiry)

    # Compare the dates
    if date_expiry <= date_current:
        print(f"License is expired")
        return False, 0
    else:
        remaining_days = (date_expiry - date_current).days
        print(f"License is still valid, {remaining_days} days remaining")
        return True, remaining_days
