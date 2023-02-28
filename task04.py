"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import collections
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    '''
    This function finds all possible value of two numbers from first and second lists,
        and how many its. After that function find all possible combination,
        when summ of four elements is zero: when
        A[i] + B[j] = -(C[k] + D[l]).
    '''
    half_summ = collections.Counter(first + second for first in a for second in b)
    return sum(half_summ[-third - forth] for third in c for forth in d)