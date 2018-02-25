##this block of code does a simple task. it calculates the age and seeks to determine the date of retirement
## of an employee in an organization.
import datetime
from datetime import timedelta as td
from datetime import date as dt

def calc_retirement(birth, appoint):
    try:
        # The employee is expected to retire after 60 years of age
        #retirement by age
        span = 60 * 365
        doB = dt(*birth)
        date_retire1 = doB + td(span)
        date_retirement1 = date_retire1.strftime('%d-%m-%Y')
        print("Due date of retirement by age is %s" % date_retirement1)
        
        retire_yr = doB.replace(year=doB.year + 60)
        print('Retire year is ' + str(retire_yr))
    
        #retirement by years of service
        # The employee is expected to retire after 35 years of service
        lengthofservice = 35 * 365
        dofirstappointment = dt(*appoint)
        date_retire2 = dofirstappointment + td(lengthofservice)
        date_retirement2 = date_retire2.strftime('%d-%m-%Y')
        print("Due date of retirement by years of service is %s" % date_retirement2)
        
        if date_retire1 < date_retire2:
            return 'Retirement due by %s' % date_retirement1
        else:
            return 'Retirement due by %s' % date_retirement2
    except: 
        raise TypeError('The argument should be an integer')
    