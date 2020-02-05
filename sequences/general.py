import math

from inttools.utils import binomial

def arithmetic(a, d, index_range=None, seq_range=None):
    """
        Generates the arithmetic sequence with a first term of 'a' and a common
        difference of 'd':

            a, a + d, a + 2d, ...

        The 'index_range' option can be used to specify a consecutive sequence
        of terms to generate, or the 'seq_range' option to specify an interval
        in which the generated terms should lie.
    """
    t = lambda n: a + (n - 1) * d
    if index_range:
        for n in index_range:
            yield t(n)
        return
    elif seq_range:
        u = math.ceil(((seq_range.start - a) / d) + 1)
        v = math.floor(((seq_range.stop - 1 - a) / d) + 1)
        for n in range(u, v + 1):
            yield t(n)
        return

    k = 0
    while True:
        yield t(k)
        k += 1


def geometric(a, r, index_range=None, seq_range=None):
    """
        Generates the geometric sequence with a first term of 'a' and a common
        ratio of 'r':

            a, ar, ar^2, ...
    """
    t = lambda n: a * r ** (n - 1)
    if index_range:
        for n in index_range:
            yield t(n)
        return
    elif seq_range:
        u = math.ceil(1 + math.log(seq_range.start / a, r))
        v = math.floor(1 + math.log((seq_range.stop - 1) / a, r))
        for n in range(u, v + 1):
            yield t(n)
        return
    k = 0
    while True:
        yield t(k)
        k += 1


def fibonacci(n):
    """
        Returns the n-th number in the Fibonacci sequence given by:

            f(1) = 1, f(2) = 1, f(n) = f(n - 1) + f(n - 2) for n > 2

        The first 10 terms are

            1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    """
    if n in [1, 2]:
        return 1
    a = b = 1
    k = 2
    while k < n:
        a, b = b, a + b
        k += 1
    return b

def pascal_triangle(n):
    """
        Prints out Pascal's triangle for a given positive integer n.

        Pascal's triangle for a given positive integer n is the sequence
        of sequence of coefficients of the binomial expansions

            (x + 1)^1, (x + 1)^2, ... , (x + 1)^n
    """
    for k in range(n + 1):
        for i in range(k + 1):
            yield binomial(k, i)
        yield