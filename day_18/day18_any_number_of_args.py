# Write a function called any_number that can receive any
# number of arguments (integers and floats) and return the
# average of those integers. If you pass 12, 90, 12, 34 as
# arguments your function should return 37.0 as average. If you
# pass 12, 90 your function should return 51.0 as average.

def any_number_of_args_avg(*args):
    sum = 0
    for arg in args:
        sum += float(arg)
    return sum / len(args)

