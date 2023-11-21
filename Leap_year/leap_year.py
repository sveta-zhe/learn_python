is_leap_finished = False


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month. Enter the month number from 1 to 12."
    if year > 3000 or year < 1000:
        return "Invalid year. Enter the year from 1000 to 3000 AD."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


while not is_leap_finished:
    year = int(input("Enter a year number: "))
    month = int(input("Enter the month number: "))
    days = days_in_month(year, month)
    print(days)
    should_continue = input("Repeat entering the year and month? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        is_leap_finished = True
