"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    len_by_2 = len(input_array)/2
    print str(len_by_2)

    find = -1
    t = 0

    while t == 0:
        for i in range(0,len_by_2):
            if input_array[i] == value:
                print str(value) +" - "+ str(len_by_2)
            if input_array[i] > value:
                print str(value) +" - "+ str(len_by_2)
        t=1

    return find

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
# print binary_search(test_list, test_val2)