##this block of code does a simple task. it calculates the age and seeks to determine the date of retirement
## of an employee in an organization.
import datetime
import pytz

tday = datetime.date.today() # get the date today

doB = datetime.date(1990, 6, 16) # this is the birthday

age = tday - doB 

"""
get the timedelta difference between the date today and the date of birth
"""

age_in_days = age.days # This converts the datetime to int

def det_age(age):
    if age >= 365:
        my_years = age // 365
        remainder_days = age % 365
        if remainder_days >= 30:
            my_month = remainder_days // 30
            left = remainder_days % 30
            if left != 0:
                my_days = left                
        else:
            my_days = remainder_days
        return 'age is {0} years {1} months and {2} days old'.format(my_years, my_month, my_days)    
    elif age < 365 and age >= 30:
        my_month = age // 30
        left_days = age % 30
        if left_days != 0:
            my_days = left_days
        return 'age is {0} months and {1} days old'.format(my_month, my_days)
    elif age > 0 and age < 30:
        my_days = age
        return 'age is {0} days old'.format(my_days)
    else:
        raise ValueError('Invalid Input')