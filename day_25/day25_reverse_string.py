# Extra Challenge: Reverse a String
#
# str1 = "the love is real"
# Write a function called read_backwards that takes a string as
# an argument and reverses it. For example, the string above
# should return: "real is love the"


def reverse_string(string):
    result=string.split()[::-1]
    print(' '.join(result))