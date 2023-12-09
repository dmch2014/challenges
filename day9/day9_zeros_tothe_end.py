# Write a function called zeros_last. This function takes a list as
# argument. If a list has zeros (0), it will move them to the front of
# the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the
# original list sorted in ascending order. For example, if you pass
# [1, 4, 6, 0, 7,0,9] as an argument,
# your code should return [1,4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].
# este reto es mejorable

def zeros_to_the_end(list_of_numbers):
    if 0 in list_of_numbers:
        original_length = len(list_of_numbers)
        list_excluding_zeros = [elem for elem in list_of_numbers if elem != 0]
        how_many_zeros_to_add = original_length - len(list_excluding_zeros)
        print(list_excluding_zeros)
        print(how_many_zeros_to_add)
        # ordeno la lista sin ceros
        list_excluding_zeros = sorted(list_excluding_zeros)
        # addinng zeros again by extendinng the list
        list_excluding_zeros.extend([0 for i in range(how_many_zeros_to_add)])
        listed_sorted_zeros_in_front = list_excluding_zeros
        return listed_sorted_zeros_in_front
    else:
        return sorted(list_of_numbers)


# version 3 using only list comprenhension
def zeros_to_the_end_improved(list_of_numbers):
    zeros = [num for num in list_of_numbers if num == 0]
    non_zeros = [num for num in list_of_numbers if num != 0]

    if zeros:
        return zeros + non_zeros
    else:
        return sorted(list_of_numbers)
