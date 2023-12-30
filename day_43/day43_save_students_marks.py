# Write a function called student_marks that records marks
# achieved by students in a test. The function should ask the user
# to input the name of the student and then ask the user to input
# the marks achieved by the student. The information should be
# stored in a dictionary. The name is the key and the marks is the
# value. When the user enters done, the function should return a
# dictionary of names and values entered.

def save_student_marks():
    user_name = str(input("Tell us your name: "))
    #se crea el dictionary con unn valor tipo array
    marks_dict = {user_name : []}
    while True:
        mark= input("Enter your marks / enter done when you finish: ")
        if mark.lower() == "done":
            return marks_dict
            break
        else :
            try:
                number_mark = int(mark)
                marks_dict[user_name].append(number_mark)
            except ValueError as ve:
                print(f'You entered {mark} that is not a number')




