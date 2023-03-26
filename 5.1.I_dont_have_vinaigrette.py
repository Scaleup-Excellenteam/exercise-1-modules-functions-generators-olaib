import re
from datetime import datetime, timedelta
from random import random

DATE_FORMAT = r"^\d{4}/\d{2}/\d{2}$"
DATE_MSG = "The date is not valid. The format should be YYYY/MM/DD"
MONDAY = 0


def check_range(num: int, min: int, max: int) -> bool:
    return min <= num <= max


def is_valid_date(date: str) -> bool:
    """Check if the date is valid in the format YYYY/MM/DD
    :param date: date in the format YYYY/MM/DD
    :return: True if the date is valid
    """
    [year, month, day] = date.split("/")
    return check_range(int(month), min=1, max=12) and check_range(int(day), min=1, max=31)


def rand_date_between(start_date: str, end_date: str) -> str:
    """Generate a random date between two dates
    :param start_date: start date
    :param end_date: end date
    :return: random date between the two dates
    """
    start = datetime.strptime(start_date, "%Y/%m/%d")
    end = datetime.strptime(end_date, "%Y/%m/%d")
    delta = (end - start) + timedelta(days=1)
    return (start + timedelta(days=random() * delta.days)).strftime("%Y/%m/%d")


def is_monday(date: str) -> bool:
    """Check if the date is Monday"""
    return datetime.strptime(date, "%Y/%m/%d").weekday() == MONDAY


def readDate(index: str) -> str:
    """Read a date from the user till it is valid
    :param index: the index of the date
    :assert: the date is valid
    :return: the date in the format YYYY/MM/DD
    """
    check_format = lambda date: re.match(DATE_FORMAT, date)
    is_valid = False
    while not is_valid:
        date = input("Enter the {} date (YYYY-MM-DD): ".format(index))
        is_valid = check_format(date) and is_valid_date(date)
    return date


# ================== MAIN ==================
if __name__ == "__main__":
    first_date = readDate("first")
    second_date = readDate("second")

    start_date = min(first_date, second_date)
    end_date = max(first_date, second_date)

    rand_date = rand_date_between(start_date, end_date)
    print("Date: {} {}".format(rand_date, "\nI don't have Vinaigrette!" if is_monday(rand_date) else ""))
