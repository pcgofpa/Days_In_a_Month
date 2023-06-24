from days_functions import is_leap
from days_functions import days_in_month


year = int(input("Enter the year you would like to check: "))
month = int(input("What month would you like to check: enter 1 for January, 2 for February: "))
days = days_in_month(year, month)
print(days)