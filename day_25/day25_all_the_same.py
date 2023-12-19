# Create a function called all_the_same that takes one
# argument, a string, a list, or a tuple and checks if all the
# elements are the same. If the elements are the same, the function
# should return True. If not, it should return False. For example,
# [‘Mary’, ‘Mary’, ‘Mary’] should return True.


# Python all() method is a built-in function that returns
# TRUE if all of the items of a passed iterable (List, Dictionary, Tuple, Set, etc.) are True; otherwise, it returns FALSE.
# It iterates through an iterable and returns a single result indicating if any element is true in a Boolean context.

def all_the_same(arg):
    yes_or_no= all(element == arg[0] for element in arg)
    print(yes_or_no)
