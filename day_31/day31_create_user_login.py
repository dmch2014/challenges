# Extra Challenge: Create User
#
# Write a function called create_user. This function asks the
# user to enter their name, age, and password. The function
# saves this information in a dictionary. For example, if the use
# enters name as Peter, age - 18 and password - love. The
# function should save the information as: {'name': 'Peter',
#                                           'age': 18, 'password': 'love'}
# Once the information is saved. The function should print to the
# user that - "User saved. Please login"
# The function should then ask the user to re-enter their name
# and password. If the name and password match with what is
#     saved in the dictionary, the function should return "Logged in
# successfully". If the name and password do not match with
# what is saved in the dictionary, the function should print
# ('Wrong password or user name. Please try again'. The
#  function should keep running until the user enters correct
#  logging details.

def create_user():
    name = input("Tell me your name: ")
    age = int(input("What's your age?: "))
    pwd = input("enter a password: ")

    user_dict = {"name": name, "age": age, "password": pwd}
    return user_dict

def login(user_dict):
    print("...Proceeding to login now:")
    name = input("Name: ")
    pwd = input("Password: ")
    if name in user_dict.values() and pwd in user_dict.values():
        return True
    else:
        return False



def register_and_log():
    user_dict=create_user()
    if not user_dict == False:
       print("User saved. Please login...")

    while True:
        logged= login(user_dict)
        if logged:
            return print("login succesfully")
            break
        else:
            print("please try again:")
            logged= login(user_dict)
    #print(user_dict)


