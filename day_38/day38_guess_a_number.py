# Write a function called guess_a_number. The function
# should ask a user to guess a randomly generated number. If the
# user guesses a higher number, the code should tell them that the
# guess is too high, if the user guesses low, the code should tell
# them that their guess is too low. The user should get a maximum
# of three guesses. When the user guesses right, the code should
# declare them a winner. After three wrong guesses, the code
# should declare them a loser.
import random
def guess_a_number():

    number= random.randint(0, 100)
    guessing_count= 0
    winner= False
    while guessing_count <3:
        guess_from_user=int(input("Guess the number the secret number from 0 to 100: "))

        if number == guess_from_user:
            print("You are the winner")
        if number > guess_from_user:
            print("Your guess is a bit  lower than the number")
            guessing_count+=1
        if number < guess_from_user:
            print("Your guess is a bit  higher than the number")
            guessing_count+=1

    if not winner:
        print("You've lost try again")
    print("The number is: ", number)


