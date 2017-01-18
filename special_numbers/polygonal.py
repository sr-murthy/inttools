import math

from functools import partial

def polygonal_number(n, k):
    """
        Returns the kth n-gonal number P(n, k) given by the general formula:

            P(n, k) = [(n - 2)k^2 - (k - 4)n] / 2
    """
    return int(((n - 2)*k**2 - (n - 4)*k) / (2))


def n_polygonal_number_func(n):
    """
        Returns a function to generate the n-gonal numbers for a given n - 
        mathematically this function is obtained by restricting the general
        function, which is a function of two variables n and k, to the given
        value of n, e.g. to have a triangular number generating function do
        the following

            >>> tri = n_polygonal_number_func(3)

            >>> tri
            >>> functools.partial(<function polygonal_number at 0x10f53bea0>, n=3)
            
            >>> [tri(k=i) for i in range(1, 11)]

            >>> [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """

    return partial(polygonal_number, n=n)


def is_polygonal_number(m, n):
    """
        Checks whether a given number m is a polygonal number for some n, i.e.
        whether it is an n-gonal number for some n > 2. If so, it returns the
        index of the number in the sequence, otherwise it returns null.
    """
    if m == 1:
        return True
    k = (((n - 4) + math.sqrt((n - 4)**2 + 8*m*(n - 2))) / (2*(n - 2)))
    return int(k) if k.is_integer() else False
