# Write a function called user_name that generates a username
# from the user’s email. The code should ask the user to input an
# email and the code should return everything before the @ sign
# as their user name. For example, if someone enters
# ben@gmail.com, the code should return ben as their user
# name.

def username_generator():
    user_email = input("Give me your email and I will guess your name:")
    return print("Your name is: ", user_email.split('@')[0])