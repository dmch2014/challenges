# Write a function called same_in_reverse that takes a string
# and checks if the string reads the same in reverse. If it is the
# same, the code should return True if not, it should return False.
# For example, ‘dad’ should return True, because it reads the
# same in reverse.
#Create a slice that starts at the end of the string, and moves backwards.



def same_in_reverse(word_string):
    #In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0,
    #move with the step -1, negative one, which means one step backwards.
    reverse_string = word_string[::-1]
    if reverse_string==word_string:
        print(True)
    else:
        print(False)
    print(reverse_string)

def same_in_reverse_2(word_string):
    # slicing the string in reverse fashion
    reverse_string=''
    for element in word_string[ : :-1]:
        print(element, end =' ')
        print('\n')
        reverse_string+=element
    if reverse_string==word_string:
        print(True)
    else:
        print(False)
    print(reverse_string)