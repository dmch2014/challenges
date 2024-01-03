
# Verify the validity of Goldbach Conjecture for n, where n is an input parameter.

def goldbach_conjecture(num):
    if num % 2 == 0:
        list_prime_numbers = prime_numbers(num)
        list_of_goldbach_num = []
        if list_prime_numbers:
            for n in list_prime_numbers:
                copy_list_prime_numbers = list_prime_numbers
                index = list_prime_numbers.index(n)
                for m in copy_list_prime_numbers:
                    if n + m == num:
                        list_of_goldbach_num.append(n)
                        list_of_goldbach_num.append(m)
                        return list_of_goldbach_num
        else:
            return "There are no prime numbers in this number"
    else:
        return "Number is not even"

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