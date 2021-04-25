# Write a Python 3 program that asks the user
# how old they are, displays that information back and
# then informs
# them how old they will be on their next birthday.


from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

currentAge = int(input('How old are you: \n'))
month = input('What month were you born: \n')
day = input('What day is your birthday" \n')

# print(currentAge)
year = datetime.now().year
date_str = f'{year}-{month}-{day}'
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
print(f'next year you will be {currentAge + 1}')
print(date_obj)
day_st = date_obj.strftime("%A")
print(f' your birthday this year is on {day_st}')


birthday_next_year = date_obj + relativedelta(years=1)
date_next_year = birthday_next_year.strftime('%A')

print(f' your birthday next year is on {date_next_year}')





