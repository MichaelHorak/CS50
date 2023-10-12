months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        data = input("Date: ")
        # condition check if input is in correct format
        # check for format September 8, 1636
        # check if contains item from list
        if any(element in data for element in months):
            first_list = data.split(',')
            # extract year
            year = first_list[1].strip()
            # extract day & month
            rest = first_list[0]
            second_list = rest.split()
            # extract day
            day = int(second_list[1])
            # check day is <32
            if day > 31:
                raise Exception
            elif day > 9:
                zero_day = ''
            else:
                zero_day = 0
            # extract month
            str_month = second_list[0]
            # convert to number & add 0 if <10
            month = (months.index(str_month)) + 1
            # check month is <13
            if month > 12:
                raise Exception
            elif month > 9:
                zero_month = ''
            else:
                zero_month = 0
            # output that same date in YYYY-MM-DD format.
            # September 8, 1636
            print(f"{year}-{zero_month}{month}-{zero_day}{day}")
            break

            # else
        elif '/' in data:
            third_list = data.split('/')
            # get year
            year = third_list[2].strip()
            # get month, add 0, verify data < 13
            month = int(third_list[0])
            if month > 12:
                raise Exception
            elif month > 9:
                zero_month = ''
            else:
                zero_month = 0
            # get day, add 0, verify data < 32
            day = int(third_list[1])
            # check day is <32
            if day > 31:
                raise Exception
            elif day > 9:
                zero_day = ''
            else:
                zero_day = 0
        # check format 9/8/1636
        # if fail raise Exception
        # if succeed, return in format YYYY-MM-DD
        print(f"{year}-{zero_month}{month}-{zero_day}{day}")
        break

    except Exception:
        pass

# In a file called outdated.py, implement a program that prompts
# the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636,
# wherein the month in the latter might be any of the values in
# the list below:
# Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format,
# prompt the user again. Assume that every month has no more than
# 31 days; no need to validate whether a month has 28, 29, 30, or
# 31 days.
