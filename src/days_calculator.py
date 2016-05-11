# Calculates number of days between two date.
# Enter your birth date and current date. This program will calculate the number of days


def date_error_check(month1, day1, month2, day2):  # Checks if dates are correct.
    if month1 > 12 or month2 > 12 or day1 > 31 or day2 > 31:
        return False
    return True


def date_is_before(year1, month1, day1, year2, month2, day2):  # Checks if birth date is less than current date
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
    return False


def is_leap_year(year1):  # Checks if the year is a leap year or not
    if (year1 % 400 == 0):
        return True
    if (year1 % 100 == 0):
        return False
    if (year1 % 4 == 0):
        return True
    return False


def days_in_month(year1, month1):  # Returns the number of days in the given month and year
    if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
        return 31
    if month1 == 2:
        if is_leap_year(year1):
            return 29
        return 28
    return 30


def next_day(year1, month1, day1):  # Returns the date of next day
    if day1 < days_in_month(year1, month1):
        return year1, month1, day1+1
    else:
        if month1 < 12:
            return year1, month1+1, 1
        else:
            return year1+1, 01, 01


def days_calculator(year1, month1, day1, year2, month2, day2):  # Calculates the days b/w birth date and current date
    days = 0
    if not date_error_check(month1, day1, month2, day2):
        return False  # "Wrong date format! try again"
    if not date_is_before(year1, month1, day1, year2, month2, day2):
        return False  # "No Time travelers allowed"
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days = days + 1
    return days

# Getting user input and printing results
print "Enter Birth date (yyyy-mm-dd)"
year1 = input("Enter year 1: ")
month1 = input("Enter month 1: ")
day1 = input("Enter day 1: ")
print "Enter current date (yyyy-mm-dd)"
year2 = input("Enter year 2: ")
month2 = input("Enter month 2: ")
day2 = input("Enter day 2: ")
if not days_calculator(year1, month1, day1, year2, month2, day2):
    print "Wrong Date! Try again"
else:
    print "Number of days:", days_calculator(year1, month1, day1, year2, month2, day2)
    print "Number of hours:", days_calculator(year1, month1, day1, year2, month2, day2) * 24
    print "Number of minutes:", days_calculator(year1, month1, day1, year2, month2, day2) * 24 * 60
    print "Number of seconds:", days_calculator(year1, month1, day1, year2, month2, day2) * 24 * 60 * 60
