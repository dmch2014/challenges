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




