# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

def biggest_odd_number(string_of_numbers):
    if string_of_numbers != "":
        odd_numbers = [n for n in string_of_numbers if int(n) % 2 != 0]
        if not odd_numbers:
            return 'There were no odd numbers in this list' # Return None if no odd numbers are found
        return max(odd_numbers)
    else:
        return 'There were no odd numbers in this list' # Return None if no odd numbers are found