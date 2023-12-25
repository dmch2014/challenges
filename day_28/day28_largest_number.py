# Extra Challenge: Largest Number
#
# Write a function called largest_number that takes a list of
# integers and re-arrange the individual digits to create the largest
# number possible. For example, if you pass the following as an
# argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
# number in this exact format: 9,877,632 as the largest number.

def largest_number_23(list_numbers):
    list = []
    for num in list_numbers:
        digit= str(num)
        for d in digit:
            list.append(d)
    # Join list items using join()
    lar_num =  int("".join(sorted(list,reverse=True)))
    for_lar_num= f'{lar_num:,}'
    print(for_lar_num)

#Usando este de ChatGPT no da el mismo resultado
def largest_number_2(list_numbers):
    # Convert integers to strings and sort based on concatenated values
    sorted_str = sorted(map(str, list_numbers), key=lambda x: x * 3, reverse=True)
    largest = ''.join(sorted_str)
    return largest


def largest_number(list):
    res = int("".join(sorted(map(str, list),reverse=True)))
    print(res)

