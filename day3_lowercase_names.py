# names = ["kerry", "dickson", "John", "Mary",
#          "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order. Using the list above, your
# code should return:
#('kerry', 'dickson', 'carol', 'adam')

def lowercase_names(list_names):
    #using a tuple for result
    lowercase_names_set= set()
    for item in list_names:
        if str(item).islower():
            lowercase_names_set.add(item)
    return print(sorted(lowercase_names_set, reverse=True))

