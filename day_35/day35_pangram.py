# Write a function called check_pangram that takes a string
# and checks if it is a pangram. A pangram is a sentence that
# contains all the letters of the alphabet. If it is a pangram,
# the function should return True, otherwise, return False. The
# following sentence is a pangram so it should return True:
# 'the quick brown fox jumps over a lazy dog'
import timeit


string= 'the quick brown fox jumps over a lazy dog'

def check_pangram():
    list_alphabet = [chr(characters) for characters in range (ord("a"), ord("z")+1)]
    list_words = string.replace(" ", "")

    list3 = [ele for ele in list_alphabet if ele in list_words]

    if len(list_alphabet) == len(list3):
        return True
    else:
        return False


def check_panggram_2():
    #crea un set (unique letters)
    # Convert sentence to lowercase and remove spaces
    sentence = string.lower().replace(" ", "")

    # Create a set of unique letters in the sentence
    unique_letters = set(string)

    # Check if all 26 letters of the alphabet are present
    return len(unique_letters) == 26

# Measure execution time for set search
p1 = timeit.timeit(check_pangram, number=1000)


# Measure execution time for list search
p2 = timeit.timeit(check_panggram_2, number=1000)

print(p1)
#print("Time taken for search in set: ", set_t3ime)
print(p2)
