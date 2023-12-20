# Extra Challenge: Length of Words
#
# s = 'Hi my name is Richard'
# Write a function called string_length that takes a string of
# words (words and spaces) as argument. This function should
# return the length of all the words in the string. Return the results
# in a form of a dictionary. The string above should return:
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}

def string_length_2(string_of_words):
    list= string_of_words.split()
    dict_of_words_lengths= {}
    for word in list:
        dict_of_words_lengths[word]=len(word)
    return dict_of_words_lengths


#using dict comprehension
def string_length(string_of_words):
    #split() is used to separate the input string into a list of words.
    list =string_of_words.split()
    #dictionary comprehension
    len_dict_words= {word: len(word) for word in list}
    return len_dict_words
