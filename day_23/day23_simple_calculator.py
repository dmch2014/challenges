# Create a simple calculator. The calculator should be able to perform
# basic math operations, add, subtract, divide and multiply. The
# calculator should take input from users. The calculator should be
# able to handle ZeroDivisionError, NameError, and
# ValueError.

def add(num1 , num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    result=0
    try:
        result=num1 /num2
    except ZeroDivisionError:
        print("Not possible to divide by zero")
        result = None
    return result


print("Select an operation from 1 to 4:")
print("1. is for sum")
print("2. is for substraction")
print("3. is for multiplication")
print("4. is for division")
while True:
    choice= input("enter an operation you want to perform with this calculator:")

    if choice in ('1','2','3','4'):
        try:
            num1= float(input("Number 1:"))
            num2= float(input("Number 2:"))
        except ValueError:
            print("Invalid iinput , not a number")
            continue
    if choice =='1':
        print("Result of sum is :", add(num1, num2))
    if choice == '2':
        print("Result of substracting is :", substract(num1, num2))
    if choice == '3':
        print("Result of multipliying is :", multiply(num1,num2))
    if choice == '4':
        print("Result of dividing is :", divide(num1,num2))
        # check if user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")

