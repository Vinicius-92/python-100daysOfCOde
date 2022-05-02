def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True


def days_in_month(year, month):
    """" Take a year and month, returns the number of days"""
    if is_leap(year) and month == 2:
        return 29
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year_input = int(input("Enter a year: "))
month_input = int(input("Enter a month: "))
days = days_in_month(year_input, month_input)
print(days)
