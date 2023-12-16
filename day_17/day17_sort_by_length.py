# Extra Challenge: Sort by Length
#
# names = [ "Peter", "Jon", "Andrew"]
# Write a function called sort_length that takes a list of strings
# as an argument, and sorts the strings in ascending order
# according to their length. For example, the list above should
# return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions

def sort_length(list_of_strings):
    len_list = len(list_of_strings)
    #intecambiar los elementos de la lista
    #The outer loop must iterate once for each element in the data set (of size n)
    for i in range(len_list-1):
        swapped = False
        #while the inner loop iterates n times the first time it is entered, n-1 times the second, and so on.
        for j in range(0, len_list-i-1):
            if len(list_of_strings[j])> len(list_of_strings[j+1]):
                list_of_strings[j], list_of_strings[j+1] = list_of_strings[j+1], list_of_strings[j]
                swapped= True
        if swapped == False :
            break
    return print(list_of_strings)

