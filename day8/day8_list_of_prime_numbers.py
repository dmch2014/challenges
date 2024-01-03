# Write a function called prime_numbers. This function asks a
# user to enter a number (integer) as an argument and returns a
# list of all the prime numbers within its range. For example, if user
#     enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers(number):
    list_of_prime_numbers= []
    for i in range(2,number):
        if is_prime(i):
            list_of_prime_numbers.append(i)
    return list_of_prime_numbers

def is_prime(n):
    #If you’ve looped through the entire range of numbers from 2 all the way up to n – 1
    # without finding a number that divides n evenly, then the number is prime.
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True