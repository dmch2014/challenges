# Write a function called user_name, that creates a username
# for the user. The function should ask a user to input their name.
# The function should then reverse the name and attach a
# randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.

# seed the pseudorandom number generator
from random import seed
from random import random
from random import randint

def username():
    name = str(input("Tell me your name: "))

    reverse_name = name[::-1] + str(randint(0,9))

    return print(reverse_name)