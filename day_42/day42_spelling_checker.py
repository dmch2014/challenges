# Write a function called spelling_checker. This code asks the
# user to input a word and if a user inputs a wrong spelling it
# should suggest the correct spelling by asking the user if they
# meant to type that word. If the user says no, it should ask the
# user to enter the word again. If the user says yes, it should
# return the correct word. If the word entered by the user is
# correctly spelled the function should return the correct word.
# Use the module textblob.
from textblob import TextBlob
def spelling_checker():
    while True:
        word= input("What is your word?: ")
        word_corrected = TextBlob(word).correct()
        print(word_corrected)
        if word != word_corrected:
            question= input(f"You entered: {word}\n Do you mean: {word_corrected}? \n Type Yes / No: ")
            print(question.lower())
            if question.lower() =='no':
                print("please try again")
            else:
                break
        elif word == TextBlob(word).correct():
            break
    return f"Your word is  ,{word_corrected}"



