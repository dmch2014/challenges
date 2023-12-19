# Create a function called average_calories that calculates the
# average calories intake of a user. The function should ask the user
# to input their calories intake for any number of days and once they
# hit ‘done’ it should calculate and return the average intake.

def average_calories():
    calories = []

    while True:
        calories_input_by_day= input("Type your calories by day or type STOP when you are done")

        if calories_input_by_day=='STOP':
            break
        try:
            calories.append(float(calories_input_by_day))
        except ValueError:
            print("Calories are expected as a number")

    if not calories:
        return print("No calories provided")
    average = sum(calories) / len(calories)
    return average

