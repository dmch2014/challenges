# Write a function called difference that takes two lists as
# arguments. This function should return all the elements that are
# in list a but not in list b and all the elements in list b not in list
# a. For example:
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]
# Use list comprehension in your function.

def difference_in_lists(list1, list2):
    in_list1_not_list2 = [i for i in list1 if i not in list2]
    in_list2_not_list1 = [i for i in list2 if i not in list1]
    print(in_list1_not_list2)
    print(in_list2_not_list1)
    return sorted(in_list1_not_list2 + in_list2_not_list1, reverse=False)

