# Calculates number of days between two date.
# Enter your birth date and current date. This program will calculate the number of days

# Checks if dates are correct.
def dateErrorCheck(month1, day1, month2, day2):
    if month1 > 12 or month2 > 12 or day1 > 31 or day2 > 31:
        return False
    return True

# Checks if birth date is less than current date
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1<year2:
        return True
    if year1==year2:
        if month1<month2:
            return True
        if month1==month2:
            if day1<day2:
                return True
    return False

# Checks if the year is a leap year or not
def isLeapYear(year1):
    if (year1%400==0):
        return True
    if (year1%100==0):
        return False
    if (year1%4==0):
        return True
    return False

# Returns the number of days in the given month and year
def daysInMonth(year1, month1):
    if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
        return 31
    if month1 == 2:
        if isLeapYear(year1):
            return 29
        return 28
    return 30

# Returns the date of next day
def nextDay(year1, month1, day1):
    if day1<daysInMonth(year1, month1):
        return year1, month1, day1+1
    else:
        if month1<12:
            return year1, month1+1, 1
        else:
            return year1+1, 01, 01

# Calculates the days b/w birth date and current date
def daysCalculator(year1, month1, day1, year2, month2, day2):
    days = 0
    if not dateErrorCheck(month1, day1, month2, day2):
        return False #"Wrong date format! try again"
    if not dateIsBefore(year1, month1, day1, year2, month2, day2):
        return False #"No Time travelers allowed"
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
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
if daysCalculator(year1, month1, day1, year2, month2, day2) == False:
    print "Wrong Date! Try again"
else:
    print "Number of days:", daysCalculator(year1, month1, day1, year2, month2, day2)
    print "Number of hours:", daysCalculator(year1, month1, day1, year2, month2, day2) * 24
    print "Number of minutes:", daysCalculator(year1, month1, day1, year2, month2, day2) * 24 * 60
    print "Number of seconds:", daysCalculator(year1, month1, day1, year2, month2, day2) * 24 * 60 * 60
