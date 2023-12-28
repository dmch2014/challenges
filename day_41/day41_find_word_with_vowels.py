# Create a function called words_with_vowels, this function
# takes a string of words and returns a list of only words that have
# vowels in them. For example, ‘You have no rhythm’ should
# return [‘You’,’have’, ‘no’].


def only_vowels(string_of_words):
    #sentence = string_of_words.lower()
    #list_of_words= sentence.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    list_of_words_v=[]

    for word in string_of_words.lower().split():
        for char in word:
            if char in vowels and word not in list_of_words_v:
                print(word)
                list_of_words_v.append(word)

    #set_of_words= set(list_of_words_v)
    return list_of_words_v




