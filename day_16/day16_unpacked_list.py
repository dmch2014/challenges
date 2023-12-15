# Extra Challenge: Unpack A Nest
# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from
# the nested list above – 34, 67, 78. Your output should be another
# list:
# [34, 67, 78]. The list output should not have duplicates.

def unpack_list(nested_list):
    unpacked_list=[]
    for value in nested_list:
        if isinstance(value, list):
            for v in value:
                if v not in unpacked_list:
                    unpacked_list.append(v)
        else:
            if value not in unpacked_list:
                unpacked_list.append(value)
    print(unpacked_list)

def unpack_list_2(nested_list):
    #using set that already avoid duplicates
    #and list comprenhesion

    unpacked_list= set(num for sublist in nested_list for num in sublist)
    print(unpack_list(unpacked_list))
