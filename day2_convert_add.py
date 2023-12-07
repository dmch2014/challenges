def convert_add(list_of_things):
    total=0
    for value in list_of_things:
        try:
            total+= int(value)
        except ValueError:
            print("Can't convert to an integer")
    result=f"the answer is:  {total}"
    return print(result)
