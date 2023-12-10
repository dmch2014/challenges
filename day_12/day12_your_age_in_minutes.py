import datetime
def your_age_in_minutes():
    year_birth=int(input("Tell us your year:"))
    today = datetime.date.today()
    current_year = today.year
    print(current_year)
    difference_years=current_year-year_birth
    minutes= difference_years * 365 * 24 * 60
    print(minutes)

