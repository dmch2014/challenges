# Write a function called zeroed code that takes a list of numbers
# as an argument. The code should zero (0) the first and the last
# number in the list. For example, if the input is [2, 5, 7, 8, 9],
# your code should return [0, 5, 7, 8, 0].
#
def zero_both_end(list_numbers):
    #nsert 0 at the beginning
    list_numbers.insert(0, 0)
    #nsert 0 at the end
    #The append() method allows you to add elements dynamically to the end of the list,
    # irrespective of the list's initial length
    list_numbers.append(0)
    return print(list_numbers)