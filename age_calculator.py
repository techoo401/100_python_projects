from datetime import datetime

date = int(input("Enter your birth date: "))
month = int(input("Enter your birth month: "))
year = int(input("Enter your birth year: "))

today = datetime.today()
birthday = datetime(year, month, date)

years = today.year - birthday.year
months = today.month - birthday.month
days = today.day - birthday.day

if days < 0:
    months -= 1

    previous_month = today.month - 1
    previous_year = today.year

    if previous_month == 0:
        previous_month = 12
        previous_year -= 1

    days += (
        datetime(previous_year, previous_month + 1, 1)
        - datetime(previous_year, previous_month, 1)
    ).days

if months < 0:
    years -= 1
    months += 12

print(f"You are {years} years, {months} months and {days} days old.")