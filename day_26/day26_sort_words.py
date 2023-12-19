# Write a function called sort_words that takes a string of words
# as an argument, removes the whitespaces, and returns a list of
# letters sorted in alphabetical order. Letters will be separated by
# commas. All letters should appear once in the list. This means
# that you sort and remove duplicates. For example ‘love life’
# should return as ['e,f,i,l,o,v'].

def sort_words(string_of_words):
    #hay que usar un set porque quita los duplicados
    string_no_spaces= ''.join(string_of_words.split())
    string_sorted_commas= ','.join(sorted(set(string_no_spaces)))
    return string_sorted_commas