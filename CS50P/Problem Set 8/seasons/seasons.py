import datetime
from datetime import date
import inflect
import re
import sys

p = inflect.engine()

# 1999-01-01
# January 1, 1999


def main():
    user_input = input("Date of Birth: ")
    year, month, day = validate(user_input)
    print(calculate(year, month, day))


def validate(var):
    if user_input := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", var):
        year = int(user_input.group(1))
        month = int(user_input.group(2))
        day = int(user_input.group(3))
        return year, month, day
    else:
        sys.exit(ValueError('Invalid date'))


def calculate(year, month, day):
    initial_date = datetime.date(year, month, day)
    cur_date = date.today()
    difference = cur_date - initial_date
    minutes = round(difference.total_seconds() / 60)
    result = p.number_to_words(minutes) + ' minutes'
    result = result.capitalize()
    result = result.replace(" and", "")
    return result
# prints how old they are in minutes, rounded to the nearest integer
# without any and between words
# Use datetime.date.today to get today’s date
# date class,
# __sub__
# timedelta
# inflect

# Date of Birth: 1970-01-01
# Fifteen million, seven hundred seventy-eight thousand eighty minutes


if __name__ == "__main__":
    main()
