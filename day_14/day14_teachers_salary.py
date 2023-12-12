# Extra Challenge: Teacher’s Salary
#
# A school has asked you to write a program that will calculate
# teachers' salaries. The program should ask the user to enter the
# teacher’s name, the number of periods taught in a month,
# and the rate per period. The monthly salary is calculated by
# multiplying the number of periods by the monthly rate.
# The current monthly rate per period is $20. If a teacher has
# more than 100 periods in a month, everything above 100 is
# overtime. Overtime is $25 per period. For example, if a teacher
# has taught 105 periods, their monthly gross salary should be
# 2,125. Write a function called your_salary that calculates a
# teacher’s gross salary. The function should return the
# teacher’s name, periods taught, and gross salary. Here is
# how you should format your output:
# Teacher: John Kelly,
# Periods: 105
# Gross salary:2,125

def your_gross_salary():
    teacher_name = input("what's your name: ")
    number_of_periods = int(input("how many periods have you worked in a month"))
    rate_per_period = float(input("what's your rate per period"))
    extra_periods = 0
    if number_of_periods > 100:
        extra_periods = number_of_periods - 100
        number_of_periods = number_of_periods - extra_periods
        return number_of_periods * 20 + extra_periods * 25
    else:
        return number_of_periods * rate_per_period



