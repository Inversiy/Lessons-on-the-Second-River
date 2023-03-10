"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    This function get file way, open this file, append all numbers in list and find min and max values.
    """
    numbers = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    min = max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
        if numbers[i] > max:
            max = numbers[i]
    return (min, max)

