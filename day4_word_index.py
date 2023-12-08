# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0). For example, the list
# below should return 2.
# words1 = ["Hate", "remorse", "vengeance"]

def word_index(list_of_things):
    longest_word_index= 0
    longest_word= 0
    for index, word in enumerate(list_of_things):
        word_length=len(word)
        if word_length > longest_word:
            longest_word=word_length
            longest_word_index=index
        elif word_length == longest_word:
            longest_word_index= 0
    return longest_word_index
