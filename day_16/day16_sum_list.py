# Write a function called sum_list with one parameter that takes
# a nested list of integers as an argument and returns the sum of
# the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
# as an argument your function should return a sum of 33.
# You can achieve this by using recursion to handle the nested lists and calculate the sum of integers within the nested structure
def sum_list(nested_list):
    added_list = 0
    for value in nested_list:
        if isinstance(value, list):
            print(value)
            added_list += sum(value)
        else:
            print(value)
            added_list+= value
    print(added_list)
