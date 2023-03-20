"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

from typing import Tuple, List

def custom_range(arg_1: str, arg_2="☻", step=1) -> List[str]:
    output_list = []
    '''
        This function return range of values. Depends from input values.
    '''
    def type_arg(char1: str) -> int:
        '''
            This function assign every type of input data unical index,
            depend from utf-8 order.
        '''
        index1 = ord(char1)
        if index1 >= 48 and index1 <= 57:
            return 1                                           # Types:
        elif index1 >= 65 and index1 <= 90:                    #   1 - digits
            return 2                                           #   2 - LatLitera, UpCase
        elif index1 >= 97 and index1 <= 122:                   #   3 - LatLitera, LowCase
            return 3                                           #   4 - KirLitera, UpCase
        elif index1 >= 1040 and index1 <= 1071:                #   5 - KirLitera, LowCase
            return 4
        elif index1 >= 1072 and index1 <= 1103:
            return 5
        else:
            return 0

    def start_of_types(type_index: int) -> Tuple[int, int]:
        '''
            This function find utf-8 order of first symbol from group.
        '''
        if type_index == 1:
            return [48, 57]
        elif type_index == 2:
            return [65, 90]
        elif type_index == 3:
            return [97, 122]
        elif type_index == 4:
            return [1040, 1071]
        elif type_index == 5:
            return [1072, 1103]

    if ord(arg_2) == 9787:
        start_index = start_of_types(type_arg(arg_1))[0]
        finish_index = ord(arg_1)
    else:
        (start_index, finish_index) = (ord(arg_1), ord(arg_2))
        if ord(arg_2) > ord(arg_1):
            if step < 0:
                step *= -1
        else:
            if step > 0:
                step *= -1
    if step > 0:
        while start_index < finish_index:
            output_list.append(str(chr(start_index)))
            start_index += step
    else:
        while start_index > finish_index:
            output_list.append(str(chr(start_index)))
            start_index += step
    return output_list

