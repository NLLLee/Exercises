age = input("What is your current age? ")

life = 90

number_of_day = 365
number_of_week = 52
number_of_month = 12

day_left = life - int(age) * number_of_day
weeks_left = life - int(age) * number_of_week
months_left = life - int(age) * number_of_month

print(f"You have {day_left} days, {weeks_left} weeks, and {months_left} months left.")