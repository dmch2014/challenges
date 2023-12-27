# Extra Challenge: Find my Position
#
# Write a function called find_index that takes two arguments;
# a list of integers, and an integer. The function should return the
# indexes of the integer in the list. If the integer is not in the list,
# the function should convert all the numbers in the list into the
# given integer.
# For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7,
# your code should return [4, 5] as the indexes of 7 in the list. If
# the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should
# return [8, 8, 8, 8, 8, 8] because 8 is not in the list.

def find_number(list_of_int, int_num):
    list_index = []
    for index, num in enumerate(list_of_int):
        print(index)
        if int(num) == int_num:
            list_index.append(index)
            return list_index
    if not list_index:
        list_of_int= [int_num for num in list_of_int ]
        return list_of_int
