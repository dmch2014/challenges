# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0). For example, the list
# below should return 2.
# words1 = ["Hate", "remorse", "vengeance"]

def word_index(list_of_things):
    longest_word_index=0
    longest_word= ''
    for item in list_of_things:
        if len(item) > len(longest_word):
            print(item)
            longest_word=item
            longest_word_index=list_of_things.index(item)
        else:
            return 0
    return print(longest_word_index)
