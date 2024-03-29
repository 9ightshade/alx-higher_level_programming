#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple (or use 0 if not present)
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    # Perform element-wise addition and return the result as a tuple
    result = (a[0] + b[0], a[1] + b[1])
    return result
