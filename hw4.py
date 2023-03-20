"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable
from typing import Tuple


def cache(func: Callable) -> Callable:
    '''
        This function can save the cache in the dictionary. If
        calculating value is in dict, function return if, else
        function calculate it and write to the dict.
    '''
    cache_values = {}
    def catching(*args):
        if not cache_values.get(args):
            value = func(*args)
            cache_values[args] = value
        cache_values[args]
    return(catching)

