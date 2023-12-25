# Write a function that has one parameter and takes a list of words
# as an argument. The function returns the longest word from the
# list. Name the function longest_word. The function should
# return the longest word and the number of letters in that word.
# For example, if you pass ['Java', 'JavaScript', 'Python'], your
# function should return
# [10, JavaScript] as the longest word.

def longest_word(list):
    my_dict = {}
    for word in list:
        my_dict[word] = len(word)
    print(my_dict)
    print(max(my_dict.items(), key=lambda x: x[1]))
