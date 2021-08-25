""" 
Define binary_search function. The function takes a list and a number to find(target), 
then returns the position of the number in the list
"""
def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
def check(index):
    if index is not None:
        print("Target is found at index ", index)
    else:
        print("Target is not in the list")

# Test to find the number 5 below, from the numbers_list list made with a list comprehension(start at 0, stop at 101, step of 5)
numbers_list = [i for i in range(0,101,5)]
print(numbers_list)
position = binary_search(numbers_list, 5)
check(position)
