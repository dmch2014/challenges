# Write a function called add_reverse. This function takes two
# lists as argument and adds each corresponding number, and
# reverses the outcome. For example, if you pass [10, 12, 34]
# and [12, 56, 78]. Your code should return [112, 22, 68]. If the
# two lists are not of equal lengths, the code should return a
# message that "the lists are not of equal lengths".


def add_reverse(list1 , list2):
    reversed_list = []
    if len(list1) == len(list2):
        for i, val in enumerate(list1):
            reversed_list.append(list1[i]+list2[i])
    else:
        print("the lists are not of equal lengths")
    return list(reversed(reversed_list))