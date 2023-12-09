# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
#     many times they appear in the dictionary. Here is a list below:
#names = ["Joseph","Nathan", "Sasha", "Selly"]
#"Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]

#Your code should return: {“Sasha”: 1, “Sera”: 2}

def dict_of_names(list_of_names):
    dict_of_names= {}
    for name in list_of_names:
        #the name already exist n the dictionaty I count them
        if name.startswith('S') and (name in dict_of_names):
           dict_of_names[name]+=1
        if name.startswith('S') and (name in dict_of_names)==False:
           dict_of_names[name]=1
    return print(dict_of_names)



