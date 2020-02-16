import math

from inttools.arithmetic import rotations


def is_prime(n):
    """
        Primality checker using trial division.
    """
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def primes(index_range=None, int_range=None):
    """
        Generates all primes, by default. Can also generate primes within a
        given index range (e.g. the first 50 primes, or the 20th to the 50th
        primes) by using the 'index_range' option, or a given interval for
        the primes (e.g. primes between 100 and 1000) by using the
        'int_range' option.
    """
    if index_range:
        n = 2
        i = 1
        while i not in index_range:
            if is_prime(n):
                i += 1
            n += 1
        while i in index_range:
            if is_prime(n):
                yield n
                i += 1
            n += 1
        return
    elif int_range:
        for n in int_range:
            if is_prime(n):
                yield n
        return

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def prime_factors(n, multiplicities=False):
    """
        Generates the distinct prime factors of a positive integer n in an
        ordered sequence. If the 'multiplicities' option is True then it
        generates pairs of prime factors of n and their multiplicities
        (largest exponent e such that p^e divides n for a prime factor p),
        e.g. for n = 54 = 2^1 x 3^3 we have

            54 -> 2, 3
            54, multiplicities=True -> (2, 1), (3, 3)

        This is precisely the prime factorisation of n.
    """
    if n == 1:
        return

    if is_prime(n):
        if not multiplicities:
            yield n
        else:
            yield n, 1
        return

    i = 0
    d = 2
    ub = math.ceil(n / 2) + 1
    while d <= ub:
        q = n / d
        if q.is_integer() and is_prime(d):
            if i == 1:
                ub = min(ub, q)
            if not multiplicities:
                yield d
            else:
                m = max(e for e in reversed(range(1, math.ceil(math.log(n, d)))) if n % (d**e) == 0)
                yield d, m
            i += 1
        d += 1 


def is_circular_prime(n):
    """
        A circular prime p satisfies the property that all (right) rotations of
        its digits yield primes also, e.g. 197 is a prime whose rotations 719
        and 971 are also primes.
    """
    if any(not is_prime(rot) for rot in rotations(n)):
        return False
    return True


def circular_primes(ubound=1000):
    """
        Generates the sequence of all circular primes below a given upper
        bound.
    """
    for n in range(1, ubound):
        if is_circular_prime(n):
            yield n
