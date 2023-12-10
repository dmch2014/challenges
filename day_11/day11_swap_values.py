# Write a function called swap_values. This function takes a list
# of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your
# function should return
# [7, 4, 67, 2].

def swap_values(list_items):
    if len(list_items) >= 2:
        first_element = list_items[0]
        last_element = list_items[-1]
        #al primer elemento de la lista le asigno el ultimo
        list_items[0] = last_element
        #al ultimo elemento de la lista le asigno el primero
        list_items[-1] = first_element

    return print(list_items)

