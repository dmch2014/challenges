# Write a function called string_range that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.) For example, if you pass 6 as
# an argument, your function should return ‘0.1.2.3.4.5’.

def string_range(single_number):
    s_range= ''
    if single_number==0:
        return print('There is no range')
    for x in range(single_number):
        if (x ==single_number-1):
            s_range+=str(x)+''
        else:
            s_range+=str(x)+'.'
    return print(s_range)