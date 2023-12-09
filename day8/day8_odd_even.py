# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the
# difference between the largest even number in the list and the
# smallest odd number in the list. For example, if you pass
# [1,2,4,6] as an argument the function should return 6 -1= 5.

def max_even_min_odd_difference(list_numbers):
    odd_numbers = []
    even_numbers = []
    for number in list_numbers:
        #it's an even number
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    difference_max_min = max(even_numbers) - min(odd_numbers)
    print("difference is:", difference_max_min)

