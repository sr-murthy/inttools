import math
import re

from collections import Counter

from functools import reduce
from itertools import (
    chain as itertools_chain,
    permutations,
    zip_longest,
)

from math import factorial


def num_digits(n, b):
    """
    Returns the number of digits in the base ``b`` required to represent a given
    (decimal) integer ``n``. Both ``n`` and ``b`` must be integers, and ``b``
    must be a positive integer.
    """
    if not (isinstance(n, int) and isinstance(b, int)):
        raise ValueError('The integer n and base b must both be integers')

    if b == 0:
        raise ValueError('Base b must be a positive integer')

    if n == 0:
        return 1

    return int(math.log(n, b)) + 1


def digits_(n, reverse=False):
    """
    Generates the sequence of digits of a given integer ``n``, starting from
    the most significant digit, by default. If reverse is True then the
    sequence is generated from the least significant digit, e.g.
    ::
        123, False -> 1, 2, 3
        123, True  -> 3, 2, 1
    """
    m = num_digits(n, 10)

    for k in reversed(range(m)):
        yield (n // (10 ** k)) % 10


def generalised_sum(int_seq, k=1, mod=None):
    """
    Returns the sum of a sequence (or set) of integers ``int_seq`` raised to a
    given power ``k``, reduced by a given modulus ``mod``, e.g.
    ::
        [1, 2, 3], 1, None    -> 6
        [1, 2, 3], 2, None    -> 14
        [1, 2, 3], 1, 5       -> 4
        (-2, 10, 0), 1, None  -> 8
        (-2, 10, 0), 2, None  -> 104
        (-2, 10, 0), 2, 3     -> 2
        {-1, 2, -3}, 1, None  -> -2
        {-1, 2, -3}, 3, None  -> -20
        {-1, 2, -3}, 13, None -> 2
        digits(123), 1, None  -> 6
        digits(123), 2, None  -> 14
        digits(123), 2, 5     -> 4
    """
    r = reduce(lambda x, y: x + y, (n ** k for n in int_seq))
    if mod is None:
        return r
    return r % mod


def generalised_product(int_seq, k=1, mod=None):
    """
    Returns the product of a sequence (or set) of integers ``int_seq`` raised to a
    given power ``k``, reduced by a given modulus ``mod``, e.g.
    ::
        [1, 2, 3], 1, None    -> 6
        [1, 2, 3], 2, None    -> 36
        [1, 2, 3], 1, 5       -> 1
        (-2, 10, 1), 1, None  -> -20
        (-2, 10, 1), 2, None  -> 400
        (-2, 10, 1), 2, 3     -> 1
        {-1, 2, -3}, 1, None  -> 6
        {-1, 2, -3}, 3, None  -> 216
        {-1, 2, -3}, 13, None -> 8
        digits(123), 1, None  -> 6
        digits(123), 2, None  -> 36
        digits(123), 2, 5     -> 1
    """
    r = reduce(lambda x, y: x * y, (n ** k for n in int_seq))
    if mod is None:
        return r
    return r % mod


def sum_of_digits(n, k=1, mod=None):
    """
    Returns the sum of the ``k``-th powers of the digits of a given positive
    integer ``n``, reduced by a given modulus ``mod``, e.g.
    ::
        (123, 1, None) -> 1^1 + 2^1 + 3^1 = 6
        (123, 2, None) -> 1^2 + 2^2 + 3^2 = 14
        (123, 2, 5)    -> (1^2 + 2^2 + 3^2) mod 5 = 14 mod 5 = 4
    """
    return generalised_sum(digits_(n), k=k, mod=mod)


def digit_sum(n, k=1, mod=None):
    """
    Returns the reduced digit sum of a given positive integer ``n``
    and its (additive) persistence, i.e. the number of steps taken to
    reduce ``n`` to a single digit by repeated addition of digits.
    In each step the summation is of ``k``-th powers of digits, and
    the sum is reduced by the given modulus ``mod``.
    """
    if n < 10 and k == 1:
        return n, 0, {}
    m = sum_of_digits(n, k=k, mod=mod)
    o = [m]
    p = 1
    while m > 9:
        p += 1
        m = sum_of_digits(m, k=k, mod=mod)
        o.append(m)
    return m, p, o


def additive_persistence(n, k=1, mod=None):
    """
    The number of steps taken to reduce ``n`` to a single digit by repeated
    addition of digits raised to a given power ``k``, and the total sum reduced
    by a given modulus ``mod``.
    """
    return digit_sum(n, k=k, mod=mod)[1]


def product_of_digits(n, k=1, mod=None):
    """
    Returns the product of the ``k``-th powers of the digits of a given
    positive integer ``n``, reduced by a given modulus ``mod``, e.g.
    ::
        (123, 1, None) -> 1^1 * 2^1 * 3^1 = 6
        (123, 2, None) -> 1^2 * 2^2 * 3^2 = 36
        (123, 2, 5)    -> (1^2 * 2^2 * 3^2) mod 5 = 36 mod 5 = 1
    """
    return generalised_product(digits_(n), k=k, mod=mod)


def digit_product(n, k=1, mod=None):
    """
    Returns the multiplicative digital root of a given positive integer ``n``
    and its (multiplicative) persistence, i.e. the number of steps taken to
    reduce ``n`` to a single digit by repeated multiplication of digits.
    In each step the multiplication is of ``k``-th powers of digits, and
    the product is reduced by the given modulus ``mod``.
    """
    if n < 10 and k == 1:
        return n, 0
    m = product_of_digits(n, k=k, mod=mod)
    o = [m]
    p = 1
    while m > 9:
        p += 1
        m = product_of_digits(m, k=k, mod=mod)
        o.append(m)
    return m, p, o


def multiplicative_persistence(n, k=1, mod=None):
    """
    The number of steps taken to reduce ``n`` to a single digit by repeated
    multiplication of digits raised to a given power ``k``, and the total sum
    reduced by a given modulus ``mod``.
    """
    return digit_product(n, k=k, mod=mod)[1]


def chain(*seqs):
    """
    Generates the sequence obtained by chaining (or concatenating) a
    sequence of sequences, e.g.
    ::
        (1, 2), (3, 4, 5), (6, 7, 8, 9) -> 1, 2, 3, 4, 5, 6, 7, 8, 9

    The arguments can be separate sequences (generators, lists, tuples) or
    an unpacked iterable of such sequences (use * to unpack an iterable
    argument), e.g.
    ::
        digits(12), digits(345), digits(6789)  -> 1, 2, 3, 4, 5, 6, 7, 8, 9
        digits(12), [3, 4, 5], (6, 7, 8, 9)    -> 1, 2, 3, 4, 5, 6, 7, 8, 9
        *[digits(12), [3, 4, 5], (6, 7, 8, 9)] -> 1, 2, 3, 4, 5, 6, 7, 8, 9
    """
    for c in itertools_chain(c for seq in seqs for c in seq):
        yield c


def interlace(*seqs):
    """
    Generates the sequence obtained by interlacing a sequence of sequences
    (of the same length), e.g.
    ::
        (1, 2, 3), (4, 5, 6), (7, 8, 9) -> 1, 4, 7, 2, 5, 8, 3, 6, 9

    The arguments can be separate sequences (generators, lists, tuples) or
    an unpacked iterable of such sequences (use * to unpack an iterable
    argument), e.g.
    ::
        digits(123), digits(456), digits(789) -> 1, 4, 7, 2, 5, 8, 3, 6, 9
        digits(123), [4, 5, 6], (7, 8, 9)     -> 1, 4, 7, 2, 5, 8, 3, 6, 9
        *[digits(123), [4, 5, 6], (7, 8, 9)]  -> 1, 4, 7, 2, 5, 8, 3, 6, 9
    """
    for x in itertools_chain.from_iterable(zip_longest(*seqs)):
        yield x


def int_from_digits(digits):
    """
    Returns a positive integer ``n`` which is a decimal expansion of a
    sequence of digits in descending order from the most significant
    digit. The input can be a sequence (list, tuple) or a generator,
    e.g.
    ::
        [1,2,3]      -> 1x10^2 + 2x10^1 + 3x10^0        =  123
        (2, 4, 5, 1) -> 2x10^3 + 4x10^2 + 5x10 + 1x10^0 = 2451
        digits(123)  -> 1x10^2 + 2x10^1 + 3x10^0        = 123
    """
    digs = list(digits)
    n = len(digs)
    return sum(d * 10 ** i for d, i in zip(digs, reversed(range(n))))


def int_concatenate(*seq_ints):
    """
    Returns the integer obtained by concatenating a sequence of
    integers, e.g.
    ::
        12, 345, 6789    -> 123456789

    The arguments can be separate integers, as above, or an unpacked
    sequence of integers, e.g.
    ::
        *[12, 345, 6789] -> 123456789
    """
    return int_from_digits(reduce(chain, map(digits_, seq_ints)))


def rotation(n, k):
    """
    Returns an integer which is the k-th right-cyclic rotation of a given
    integer ``n``. By definition, this is the integer produced from ``n`` by a
    right-cyclic rotation of order ``k`` of its digits, e.g.
    ::
        1234, 1 -> 4123
        1234, 2 -> 3412
        1234, 3 -> 2341
        1234, 4 -> 1234
    """
    if k == 0:
        return n

    digs = list(digits_(n))

    m = len(digs)

    _k = k % m

    new_digs = digs[m - _k:] + digs[:m - _k]

    return sum(map(lambda t: t[0] * 10 ** t[1], zip(new_digs, reversed(range(m)))))


def rotations(n):
    """
    Generates a sequence of all right-cyclic rotations of a given integer
    ``n``, e.g.
    ::
        1234 -> 4123, 3412, 2341, 1234
    """
    K = num_digits(n, 10)

    for k in range(1, K + 1):
        yield rotation(n, k)
    

def int_permutations(n):
    """
    Generates a sequence of permutations of a given positive integer ``n`` in
    lexicographic order, e.g.
    ::
        123 -> 123, 132, 213, 231, 312, 321
    """
    for p in permutations(digits_(n)):
        yield int_from_digits(p)


def is_pandigital(n, zeroless=False, dig_freq='1+'):
    """
    Checks whether a positive integer ``n`` is pandigital with respect
    to the (decimal) base and has a digit frequency given by the
    string ``dig_freq``. The optional ``zeroless`` argument can be used
    to indicate whether ``0`` should or should not be included in
    checking for the pandigital property, i.e. whether ``0`` should be
    included in the base digit set.

    Note: ``dig_freq`` is an integer string with an optional ``+``
    suffix to indicate min. digit frequency - otherwise the digit
    frequency is taken to be exact.

    Some examples are given below.
    ::
        915286437, False, '1+'           ->   False
        915286437, True, '1+'            ->   True
        9152860437, False, '1+'          ->   True
        112233445566778899, False, '2'   -> False
        112233445566778899, True, '2'    -> True
        11223344556677889900, False, '2' -> True
    """
    _digits = Counter(digits_(n))

    _dfreq, dfreq_min = re.match(r'(\d+)(\+)?', dig_freq).groups()
    _dfreq = int(_dfreq)

    base = set(Counter(str(1234567890)).keys()).difference(['0'] if zeroless else [])

    return base.issubset(_digits.keys()) and (
        min(_digits.values()) == max(digits.values()) == _dfreq if dfreq_min != '+' else
        min(_digits.values()) >= _dfreq
    )
