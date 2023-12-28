# Create a function called generate_password that generates any
# length of password for the user. The password should have a
# random mix of upper letters, lower letters, numbers, and
# punctuation symbols. The function should ask the user how
# strong they want the password to be. The user should pick from -
# weak, strong, and very strong. If the user picks weak, the
# function should generate a 5-character long password. If the user
# picks strong, generate an 8-character password and if they pick
# very strong, generate a 12-character password./

import random
import string

def pwd_generator():
    choice= int(input("How strong do you  want the pwd, type 1 for weak, 2 for strong, 3 for very strong: "))
    pwd_len = 0
    #weak pwd
    if choice == 1:
        pwd_len = 5
    if choice == 2:
        pwd_len = 8
    if choice == 3:
        pwd_len = 12

    if choice > 0 and choice< 4:
        chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
        generated_pwd= ''.join(random.choice(chars) for x in range(pwd_len))
        return generated_pwd
    else:
        return "try again"