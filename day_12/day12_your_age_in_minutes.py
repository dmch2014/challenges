# Extra Challenge: Your Age in Minutes
# Write a function called age_in_minutes that tells a user how
# old they are in minutes. Your code should ask the user to
# enter their year of birth, and it should return their age in
# minutes (by subtracting their year of birth to the current year).
# Here are things to look out for:
#     a. The user can only input a 4-digit year of birth. For
# example, 1930 is a valid year. However, entering any
# number longer or less than 4 digits long should render
# input invalid. Notify the user to input a four digits
# number.
# b. If a user enters a year before 1900, your code should
# tell the user that input is invalid. If the user enters the
# year after the current year, the code should tell the user,
# to input a valid year.
# The code should run until the user inputs a valid year.
# Your function should return the user's age in minutes. For
# example, if someone enters 1930, as their year of birth your
# function should return:
# You are 48,355,200 minutes old.

import datetime
def your_age_in_minutes():
    while True:

            year_birth=input("Tell us your year:")
            year_birth_num= int(year_birth)

            if (year_birth_num < 1900 or len(year_birth)>4):
                print("Sorry, this year it's not a valid one...try again")
                continue
            else:
                #we're happy with the value given.
                #we're ready to exit the loop.
                today = datetime.date.today()
                current_year = today.year
                difference_years=current_year-year_birth_num
                minutes= difference_years * 365 * 24 * 60
                return print("Your age in minutes is:", minutes)
                break




