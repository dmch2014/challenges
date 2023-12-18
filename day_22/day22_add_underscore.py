# Create three functions. The first called add_hash takes a string and
# adds a hash # between the words.
# The second function called add_underscore removes the hash (#) and replaces it with an
#     underscore "_"
#The third function called remove_underscore,
#                                              removes the underscore and replaces it with nothing. if you pass
# ‘Python’ as an argument for the three functions, and you call them at
# the same time like:
#     print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.
def add_hash(list_of_words):
    list_with_hash = []
    for word in list_of_words:
        list_with_hash.append(word+'#')

    return print(list_with_hash)


def add_hash_2(list_of_words):
    list_with_hash = list_of_words.split()
    if len(list_with_hash)==1:
        result=list_of_words+'#'
        return result
    else:
        result ='#'.join(list_with_hash)
        return result

def add_underscore(list_of_words):
    list_with_underscore= list_of_words.replace('#', '_')
    return list_with_underscore

def remove_underscore(list_of_words):
    list_without_underscore= list_of_words.replace('_', ' ')
    return list_without_underscore




