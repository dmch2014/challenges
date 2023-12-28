# Extra Challenge: Find Missing Numbers
# list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
#         18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
# Write a function called missing_numbers that takes a list of
# sequence of numbers and finds the missing numbers in the
# sequence. The list above should return:
# [4, 8, 10, 13, 16, 29, 30]


def find_missing_numbers(list_sequence_numbes):
    max_num = max(list_sequence_numbes)
    min_num = min(list_sequence_numbes)
    print(min, max)
    missing_numbers=[]

    while min_num < max_num:
        following_num = min_num+1
        if following_num not in list_sequence_numbes:
            missing_numbers.append(following_num)
        min_num += 1
    return missing_numbers

#SE Pueden restar las listas
def find_missing_numbers_2(nums):
    # Find the range of numbers from the given list
    full_range = set(range(nums[0], nums[-1] + 1))
    print(full_range)

    # Create a set from the input list to find the missing numbers
    nums_set = set(nums)
    print(nums_set)

    # Find the missing numbers in the sequence
    missing = sorted(list(full_range - nums_set))

    return missing