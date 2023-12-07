# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
#fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(input_dict):
    longest =''
    for value in input_dict.values():
        if len(value) > len(longest):
            longest = value
    return longest

