# Write a function called make_tuples that takes two lists,
# equal lists, and combines them into a list of tuples. For
# example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
# function should return [(1,5), (2,6), (3,7), (4,8)].

def list_of_tuples(list1 , list2):
    return list(zip(list1,list2))