# You are given a string of words. Some of the words in the string
# contain uppercase letters. Write a code that will return all the
# words that have an uppercase letter. Your code should return a
# list of the words. Each word in the list should be reversed. Here
# is how your output should look:
# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
#'leArning is hard, bUt if You appLy youRself you can achieVe success'

def reversed_list(string_of_words):
    words = string_of_words.split()
    upper_case_words =[]
    for word in words:
        for ele in word:
            if ele.isupper():
                #slicing string and revesing
                upper_case_words.append(word[::-1])
    print(upper_case_words)