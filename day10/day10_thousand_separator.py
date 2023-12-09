# Your new company has a list of figures saved in a list. The issue
# is that these numbers have no separator. The numbers are
# saved in the following format:
# [1000000, 2356989, 2354672, 9878098].
# You have been asked to write a code that will convert each of the
# numbers in the list into a string. Your code should then add a
# comma on each number as a thousand separator for
#     readability. When you run your code on the above list, your
# output should be:
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]

def convert_numbers(unformatted_list):
    formated_list = [f"{num:,}" for num in unformatted_list]
    return formated_list

