# Write a function called flat_list that takes one argument, a
#
# nested list. The function converts the nested list into a one-
# dimension list. For example [[2,4,5,6]] should return
#
# [2,4,5,6].

def flat_your_list(nested_list):
    flat_list= []
    for value in nested_list:
        flat_list.extend(value)
    return print(flat_list)


