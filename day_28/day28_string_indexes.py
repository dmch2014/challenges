# Write a function called index_position. This function takes a
# string as a parameter and returns the positions or indexes of all
# lower letters in the string. For example, ‘LovE’ should return
# [1,2].

def lower_case_indexes(string):
    index_list = []
    for index, ele in enumerate(string):
        if ele.islower():
            index_list.append(index)
    return index_list
