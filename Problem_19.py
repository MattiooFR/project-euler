# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


month_length = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def count_sundays():
    day_count = 1
    sunday_count = 0
    year = 1901
    while year < 2001:
        for month in range(1, 13):
            days_month = month_length[month]
            if month == 2:
                if is_leap_year(year):
                    days_month = 29
            for days in range(days_month):
                day_count += 1
                if day_count % 7 == 0 and days == 0:
                    sunday_count += 1
        year += 1

    print(sunday_count)


count_sundays()
