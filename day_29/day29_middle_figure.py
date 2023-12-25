# Write a function called middle_figure that takes two
# parameters a, and b. The two parameters are strings. The
# function joins the two strings and finds the middle element.
# If the combined string has a middle element, the function should
# return the element, otherwise, return ‘no middle figure’. Use
# ‘make love’ as an argument for a and ‘not wars’ as an
# argument for b. Your function should return ‘e’ as the middle
# element. Whitespaces should be removed.

def middle_figure(string_a, strng_b):
    strng_c = string_a + strng_b
    strng_c = strng_c.replace(" ", "")
    if len(strng_c) % 2 != 0:
        middle = len(strng_c) // 2
        print(strng_c[middle])
    else:
        print('no middle figure')
   