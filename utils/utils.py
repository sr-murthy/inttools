from collections import Counter

from itertools import permutations

from math import factorial


def int_product(int_seq):
    """
        Returns the product of a sequence (or set) of integers, e.g.

            [1, 2, 3]   -> 6
            (-2, 10, 0) -> 0
            {-1, 2, -3} -> 6
            digits(123) -> 6
    """
    m = 1
    for i in int_seq:
        m *= i
    return m


def digits(n, reverse=False):
    """
        Generates the sequence of digits of a given integer `n`, starting from
        the most significant digit, by default. If reverse is True then the
        sequence is generated from the least significant digit, e.g.

            123 -> 1, 2, 3      (with no reverse or reverse=False)
            123 -> 3, 2, 1      (with reverse=True)
    """
    s = str(n) if not reverse else str(n)[::-1]
    for d in s:
        yield int(d)


def digit_sum(n, k=1):
    """
        Returns the sum of the `k`-th powers of the digits of a given positive
        integer `n`, e.g.

            (312, 2) -> 3^2 + 1^1 + 2^2 = 14
    """
    return sum(d**k for d in digits(n))


def digit_product(n, k=1):
    """
        Returns the product of the `k`-th powers of the digits of a given
        positive integer `n`, e.g.

            (312, 2) -> 3^2 x 1^2 x 2^2 = 36
    """
    return product(d**k for d in digits(n))


def int_from_digits(digits):
    """
        Returns a positive integer `n` which is a decimal expansion of a
        sequence of digits in descending order from the most significant
        digit. The input can be a sequence (list, tuple) or a generator,
        e.g.

            [1,2,3]      -> 1x10^2 + 2x10^1 + 3x10^0        =  123
            (2, 4, 5, 1) -> 2x10^3 + 4x10^2 + 5x10 + 1x10^0 = 2451
            digits(123)  -> 1x10^2 + 2x10^1 + 3x10^0        = 123
    """
    dgs = list(digits)
    n = len(dgs)
    return sum(d*10**i for d, i in zip(dgs, reversed(range(n))))


def is_pandigital(n, dset, dfreq='1+'):
    """
        Checks whether a given positive integer `n` is a pandigital number with
        respect to the digit base set `dset` and the digit frequency string
        dfreq. To be precise, `n` is pandigital with respect to the specified
        parameters if it has digits in the base set `dset` such that every digit
        occurs at least `dfreq` times, where `dfreq` is of the form

            `<positive integer>` or `<positive integer>+`

        The the additional `+` at the end indicates that the specified digit
        frequency should be considered a minimum - if '+' is not present then
        the digit frequency is taken to be exact, e.g.

            915286437, {1, 2, 3, 4, 5, 6, 7, 8, 9}     ->   True
            7346821,   {1, 2, 3, 4, 6, 7, 8}, '1+'     ->   True
            22441144,  {1, 2, 3, 4}, '2+'              ->   True
            123456789, {1, 2, 3, 4, 5, 6, 7, 8}        ->   False
            31290,     {0, 1, 2, 3, 8}                 ->   False
            1243314,   {1, 2, 3, 4}, '2+'              ->   False

    """
    count = Counter(digits(n))
    _dset = set(dset) if not type(dset) == set else dset
    _dfreq = int(dfreq.split('+')[0])
    return (
        set(count.keys()).issubset(_dset) and not any(count[d] != _dfreq for d in count) if '+' not in dfreq else
        set(count.keys()).issubset(_dset) and not any(count[d] < _dfreq for d in count)
   )


def rotations(n):
    """
        Generates a sequence of (right) rotations of a positive integer `n`, e.g.

            1234 -> 4123, 3412, 2341, 1234
    """
    digs = list(digits(n, reverse=True))
    n = len(digs)
    for i in range(n):
        yield sum(digs[(j + i) % n] * 10**j for j in range(n))


def int_permutations(n):
    """
        Generates a sequence of permutations of a given positive integer `n` in
        lexicographic order, e.g.

            123 -> 123, 132, 213, 231, 312, 321
    """
    for p in permutations(digits(n)):
        yield int_from_digits(p)


def concatenate(*seqs):
    """
        Generates the sequence obtained by concatenating a sequence of sequences,
        e.g.

            (1, 2), (3, 4, 5), (6, 7, 8, 9)        -> 1, 2, 3, 4, 5, 6, 7, 8, 9

        The arguments can be separate sequences (generators, lists, tuples) or
        an unpacked iterable of such sequences (use * to unpack an iterable
        argument), e.g.

            digits(12), digits(345), digits(6789)  -> 1, 2, 3, 4, 5, 6, 7, 8, 9
            digits(12), [3, 4, 5], (6, 7, 8, 9)    -> 1, 2, 3, 4, 5, 6, 7, 8, 9
            *[digits(12), [3, 4, 5], (6, 7, 8, 9)] -> 1, 2, 3, 4, 5, 6, 7, 8, 9
    """
    for seq in seqs:
        for c in seq:
            yield c


def interlace(*seqs):
    """
        Generates the sequence obtained by interlacing a sequence of sequences
        (of the same length), e.g.

            (1, 2, 3), (4, 5, 6), (7, 8, 9)       -> 1, 4, 7, 2, 5, 8, 3, 6, 9

        The arguments can be separate sequences (generators, lists, tuples) or
        an unpacked iterable of such sequences (use * to unpack an iterable
        argument), e.g.

            digits(123), digits(456), digits(789) -> 1, 4, 7, 2, 5, 8, 3, 6, 9
            digits(123), [4, 5, 6], (7, 8, 9)     -> 1, 4, 7, 2, 5, 8, 3, 6, 9
            *[digits(123), [4, 5, 6], (7, 8, 9)]  -> 1, 4, 7, 2, 5, 8, 3, 6, 9
    """
    for e in concatenate(*zip(*seqs)):
        yield e


def int_concatenate(*seq_ints):
    """
        Returns the integer obtained by concatenating a sequence of integers, e.g.

            12, 345, 6789    -> 123456789

        The arguments can be separate integers, as above, or an unpacked
        sequence of integers, e.g.

            *[12, 345, 6789] -> 123456789
    """
    return int_from_digits(reduce(concatenate, map(digits, seq_ints)))


def integerise(f):
    """
        Turns a float `f` into an integer if it is an integer, otherwise
        returns the same float.
    """
    return int(f) if type(f) == float and f.is_integer() else f


def multinomial(n, *ks):
    """
        Returns the multinomial coefficient (n; k_1, k_2, ... k_m), where
        k_1, k_2, ..., k_m are non-negative integers such that

            k_1 + k_2 + ... + k_m = n.

        This is the coefficient of the term

           x_1^k_1 + x_2^k_2 + ... + x_m^k_m

        in the expansion of

        (x_1 + x_2 + ... x_m)^n.

        The argument *ks can be separate non-negative integers adding up to the
        given non-negative integer `n`, or an unpacked sequence of such
        integers.
    """
    return int(factorial(n) / int_product(map(factorial, ks)))


def binomial(n, k):
    """
        Returns the familiar binomial cofficient - the number of ways
        of choosing a set of `k` objects (without replacement) from a set of
        `n` objects.
    """
    return multinomial(n, k, n - k)
