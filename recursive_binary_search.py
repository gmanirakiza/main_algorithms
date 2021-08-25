""" 
The recursive_binary_search returns True if target is found, or false if it is not. The function takes a list and a number to find(target) 
"""


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def check(result):
        print("Target is found ", result)

# Test to find the number 5 below below is found or not. 
numbers_list = [i for i in range(0,101,5)]
print(numbers_list)
found = recursive_binary_search(numbers_list, 3)
check(found)  
