# Write a function called even_or_average that ask a user to
# input five numbers. Once the user is done, the code should
# return the largest even number in the inputted numbers. If
# there is no even number in the list, the code should return the
# average of all the five numbers.

def even_or_average():
    list_num =[]
    list_num.append(float(input("Number 1:")))
    list_num.append(float(input("Number 2:")))
    list_num.append(float(input("Number 3:")))
    list_num.append(float(input("Number 4:")))
    list_num.append(float(input("Number 5:")))

    even_list= [i for i in list_num if i % 2 ==0]
    if len(even_list) >0:
        return print(max(even_list))
    else:
        sum_of_nums= sum(list_num)
        return print(sum_of_nums/len(list_num))