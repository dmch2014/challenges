# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element
# appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count_string(cadena):
    #convert string to list
    list_chars = list(cadena)
    my_dict = {i:list_chars.count(i) for i in list_chars}
    return my_dict