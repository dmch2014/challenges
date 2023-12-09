# Write a function called check_duplicates that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below
# should return apple as a duplicate and list of names should
# return "no duplicates".
#['apple', 'orange', 'banana', 'apple']
def find_duplicates(list_names):
    revisados = set()
    duplicados = set()

    for item in list_names:
        if item in revisados:
            duplicados.add(item)
        else:
            revisados.add(item)
    len_of_dup=len(duplicados)
    if(len_of_dup==0):
        return print('No duplicates')
    return list(duplicados)