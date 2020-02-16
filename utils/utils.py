from functools import reduce
from math import factorial


def integerise(f):
    """
    Turns a float `f` into an integer if it is an integer, otherwise
    returns the same float.
    """
    return int(f) if isinstance(f, float) and f.is_integer() else f
