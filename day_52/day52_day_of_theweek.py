# 2. Given dd/mm/yyyy as an input, return the corresponding weekday (Mon-Sun)
from datetime import date
import datetime
import calendar

#given date like day,month,year
def get_day_of_the_week(day, month, year):

    d = datetime.date(year, month, day)
    return calendar.day_name[d.weekday()]  #'Wednesday'