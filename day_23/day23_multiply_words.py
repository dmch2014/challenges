# Extra Challenge: Multiply Words
#
# s = "love live and laugh"
# Write a function called multiply_words that takes a string as an
# argument and multiplies the length of each word in the string by
# the length of other words in the string. For example, the string
# above should return 240 - love (4) live (4) and (3) laugh (5).
# However, your function should only multiply words will all
# lowercase letters. If a word has one upper case letter, it should be
# ignored. For example, the following string:
# s = "Hate war love Peace" should return 12 – war (3) love (4).
# Hate and Peace will be ignored because they have at least one
# uppercase letter.

def is_upper_word(word):
    for ele in word:
        if ele.isupper():
            return True
        else:
            return False

def multiply_uppercase_words_len(string_of_words):
    list= string_of_words.split()
    uppercase_list= [word for word in list if is_upper_word(word)]
    result= 1
    for word in uppercase_list:
        result *= len(word)
    return(result)
