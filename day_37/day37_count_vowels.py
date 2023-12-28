# Create a function called count_the_vowels. The function
# takes one argument, a string, and returns the number of vowels
# in the string. For example, ‘hello’ should return 2 vowels. If a
# vowel appears in a string more than once it should be counted
# as one. For example, ‘saas’ should return 1 vowel. Your code
# should count lowercase and uppercase vowels.


def count_vowels(string):
    sentence = string.lower().replace(" ", "")
    vowels = ['a', 'e', 'i', 'o', 'u']
    counting_vowels = sum(1 for ele in vowels if ele in sentence)

    return counting_vowels


