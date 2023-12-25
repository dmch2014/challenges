# Write a function called repeated_name that finds the most
# repeated name in the following list.
#['Peter', 'Peter', 'Mary', 'Mary', 'Mary']


def most_repeated_name(list):
    my_dict = {i:list.count(i) for i in list}
    return max(my_dict, key=my_dict.get)
