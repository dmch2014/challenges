#day 1:
#Write a function called divide_or_square that takes one
# argument (a number), and returns the square root of the number
# if it is divisible by 5, returns its remainder if it is not divisible by
# 5. For example, if you pass 10 as an argument, then your function
# should return 3.16 as the square root...
import math
def divide_or_square(param_number):
    #the reminder operator it's used to check divisibility of a number with 5
    if param_number % 5 == 0:
        return (math.sqrt(param_number))
    else:
        return (param_number % 5)

