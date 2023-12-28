# Write a function called translate that takes the following
# words and translates them into pig Latin.
# a = 'i love python'
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
# end. For example, ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move
# the first letter to the end and add ‘ay’ to the end. For
# example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay

def tranlate(string_of_words):
    vowels= ['a', 'e', 'i', 'o', 'u']
    list_of_words= string_of_words.split()
    new_list=[]
    for word in list_of_words:
        len_word= len(word)
        if word[0] in vowels:
            new_word= word+'yay'
            new_list.append(new_word)
        else:
            first_letter= word[0]
            new_word= word[1:len_word] + 'ay'
            new_list.append(new_word)
    print(new_list)