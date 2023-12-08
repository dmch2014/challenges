# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list. Here is a
# list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male'],
#             'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
#Your code should return a list of tuples. The list above should
# return:
# [(‘Male’,7), (‘female’,6)]

def students_sex(list_registry):
    female_count = 0
    male_count = 0

    for student in list_registry:
        student_lowercase=student.lower()
        if (student_lowercase== 'male'):
            male_count+=1
        elif (student_lowercase =='female'):
            female_count+=1
    male_tuple = ('Male', male_count)
    female_tuple = ('Female' , female_count)
    list_of_tuples = [male_tuple, female_tuple]
    return print("How many students: \n", list_of_tuples)