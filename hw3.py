"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    '''
        This function return all possible combination of items
        from K lists.
    '''
    sets = []
    all_combination = []
    partial_combination = []
    numbers_element = []
    k = len(args)
    for i in range(k):
        sets.append(set(args[i]))
    for i in range(k):
        sets[i] = list(sets[i])
    partial_combination.append(len(sets[0]))
    for i in range(k-1):
        partial_combination.append(partial_combination[i]*len(sets[i+1]))
    numbers_element.append(int(partial_combination[-1]/len(sets[0])))
    for i in range(k-1):
        numbers_element.append(int(numbers_element[i]/len(sets[i+1])))
    for i in range(len(sets[0])):
        for j in range(numbers_element[0]):
            all_combination.append(list())
            all_combination[i*numbers_element[0]+j].append(sets[0][i])
    for i in range(k-1):
        for j in range(partial_combination[i]):       
            for x in range(len(sets[i+1])):           
                for y in range(numbers_element[i+1]): 
                    all_combination[
                        j*numbers_element[i] +
                        x*numbers_element[i+1] +
                        y].append(sets[i+1][x])
    return(all_combination)
    
