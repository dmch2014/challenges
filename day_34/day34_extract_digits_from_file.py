# In this challenge, copy the text below and save it as a CSV file.
# Save it in the same folder as your Python file. Save it as
# python.csv.
# Write a function called just_digits that reads the text from the
# CSV file and returns only digit elements from the file. Your
# function should return 1991, 2, 2000, 3, 2008 as a list of
# strings.
#
# “Python was released in 1991 for the first time. Python 2 was
# released in 2000 and introduced new features, such as list
# comprehensions and a cycle-detecting garbage collection system
# (in addition to reference counting). Python 3 was released in 2008
# and was a major revision of the language that is not
# completely backward-compatible.”
# Source: Wikipedia

def extract_digits():
    file_to_analize= open('text_to_analize.csv', 'r')
    lines= file_to_analize.readlines()
    digit_list_file=[]
    for line in lines:
        line_list_of_words = line.split()
        for word in line_list_of_words:
            try:
                if isinstance(int(word), int):
                    digit_list_file.append(word)
            except ValueError:
                pass
    return digit_list_file









