# Extra Challenge: Set or list
#
# You want to implement a code that will search for a number in
#     a range. You have a decision to make as to whether to store the
# number in a set or a list. Your decision will be based on time.
# You have to pick a data type that executes faster.
# You have a range and you can either store it in a set or a list
# depending on which one executes faster when you are searching
# for a number in the range. See below:
#     a = range(10000000)
# x = set(a)
# y = list(a)
# Let’s say you are looking for a number 9999999 in the range
# above. Search for this number in the list and the set. Your
# challenge is to find which code executes faster. You will pick the
# one that executes quicker, lists, or sets. Run the two searches
# and time them.
import timeit

a = range(10000000)
x = set(a)
y = list(a)


def set_performance_search():
    #serching for a number in set
    return 9999999 in x

def list_performance_search():
    #serching for a number in list
    return 9999999 in y

# Measure execution time for set search
set_time = timeit.timeit(set_performance_search, number=1000)


# Measure execution time for list search
list_time = timeit.timeit(list_performance_search, number=1000)

print(f"Time taken to search in set: {set_time:.6f} seconds")
#print("Time taken for search in set: ", set_t3ime)
print("Time taken for search in list: ", list_time)




