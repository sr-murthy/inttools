from itertools import permutations

def digits(n, reverse=False):
    """
        Generates the sequence of digits of a given integer n, starting from
        the most significant digit, by default. If reverse is True then the
        sequence is generated from the least significant digit, e.g.

            123 -> 1, 2, 3      (with no reverse or reverse=False)
            123 -> 3, 2, 1      (with reverse=True)
    """
    s = str(n) if not reverse else str(n)[::-1]
    for d in s:
        yield int(d)


def int_from_digits(digits):
    """
        Returns a positive integer n which is a decimal expansion of a
        sequence of digits in descending order from the most significant
        digit. The input can be a sequence (list, tuple) or a generator,
        e.g.

            [1,2,3] -> 1x10^2 + 2x10^1 + 3x10^0 = 123
            (2, 4, 5, 1) -> 2x10^3 + 4x10^2 + 5x10 + 1x10^0 = 2451
    """
    dgs = list(digits)
    n = len(dgs)
    return sum(d*10**i for d, i in zip(dgs, reversed(range(n))))


def rotations(n):
    """
        Generates a sequence of (right) rotations of a positive integer n, e.g.

            1234 -> 4123, 3412, 2341, 1234
    """
    digs = list(digits(n, reverse=True))
    n = len(digs)
    for i in range(n):
        yield sum(digs[(j + i) % n] * 10**j for j in range(n))


def int_permutations(n):
    """
        Generates a sequence of permutations of a given positive integer n in
        lexicographic order, e.g.

            123 -> 123, 132, 213, 231, 312, 321
    """
    for p in permutations(digits(n)):
        yield int_from_digits(p)


def concatenate(int_seq):
    """
        Produces an integer which is a "concatenation" of the digits of a
        sequence of positive integers, e.g.

            [12, 345, 6789] -> 123456789
    """
    return int(''.join([str(n) for n in int_seq]))


def integerise(f):
    """
        Turns a float into an integer if it is an integer, otherwise returns
        the same float.
    """
    return int(f) if type(f) == float and f.is_integer() else f
