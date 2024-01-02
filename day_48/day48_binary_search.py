# Write a function called search_binary that searches for the
#     number 22 in the following list and returns its index. The
# function should take two parameters, the list and the item that
# is being searched for. Use binary search (iterative Method).
# list1 = [12, 34, 56, 78, 98, 22, 45, 13]

def binary_search(list_values, value_to_find):
    sorted_list = sorted(list_values)
    lower_index = 0
    higher_index = len(sorted_list) -1
    print(sorted_list)

    while lower_index <= higher_index:
        #look for middle index, the average of the 2
        mid_index = (lower_index + higher_index) // 2

        if sorted_list[mid_index] == value_to_find:
            return mid_index
        elif sorted_list[mid_index] > value_to_find:
            higher_index = mid_index - 1
        elif sorted_list[mid_index] < value_to_find:
            lower_index = mid_index + 1

    return "No element found"
