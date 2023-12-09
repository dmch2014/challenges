# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.

def hide_password():
    password_raw = str(input("What is the password you want to hide?:"))
    password_hidden = (len(password_raw) - 1) * '*'
    return print("'"+password_hidden+"'", "Your password is " + str(len(password_hidden)) + " characters long")
