# Write a function called analyse_string that returns the number of
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
#         and, total characters (all letters and special characters minus
# whitespaces) in a string. Return everything in a dictionary format:
# {“special character”: “number”, “words”: “number”, “total
# characters”: “number”}
# Use the string below as an argument:
# “Python has a string format operator %. This functions
# analogously to printf format strings in C, e.g. "spam=%s
# eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".
import re
import string

def count_words_sc(cadena_de_palabras):
    specials = "(#$%&'()*+,-./:;<=>?@\[\]^_`\{|\}~)"
    analysis_dicy= {}
    #remplazo los espacios y tengo el total de caracteres
    all_chars = cadena_de_palabras.replace(" ", "")
    items = cadena_de_palabras.split()

    list_of_total_schars =  [c for c in all_chars if c in string.punctuation]
    print(list_of_total_schars)

    # count_specials = 0
    # for char in all_chars:
    #     if char in specials:
    #         count_specials += 1

    count_words = 0
    for item in items:
        list_of_schars =  [c for c in item if c in string.punctuation]
        if not list_of_schars:
            count_words += 1

    analysis_dicy["number_of_specials"]= len(list_of_total_schars)
    analysis_dicy["number_of_words"]= count_words
    analysis_dicy["total_chars"]= len(all_chars)

    return analysis_dicy

