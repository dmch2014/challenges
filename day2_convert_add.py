# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.
def convert_add(list_of_things):
    total=0
    for value in list_of_things:
        try:
            total+= int(value)
        except ValueError:
            print("Can't convert to an integer")
    result=f"the answer is:  {total}"
    return print(result)
