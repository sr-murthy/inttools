from itertools import (
    product,
    starmap,
)

from primes import prime_factors

from utils import int_product


def divisors(n):
    """
        Generates the sequence of divisors of a given positive integer n, in
        ascending order, e.g.:

            312 -> 1, 2, 3, 4, 6, 8, 12, 13, 24, 26, 39, 52, 78, 104, 156, 312
    """
    pfs = [pf for pf in prime_factors(n, multiplicities=True)]
    divs = [
        int_product(starmap(pow, zip((pf[0] for pf in pfs), mt))) for mt in product(*(range(pf[1] + 1) for pf in pfs))
    ]
    divs = sorted(divs)
    for div in divs:
        yield div


def d(n):
    """
        Returns the number of divisors of a given positive integer n, e.g.

            312 -> 16

        Uses the prime factorization of n: if n has the prime factorisation

            n = p_1^e_1 x p_2^e_2 x ... p_k^e_k

        (where the p_i are the prime factors of n and e_i are their 
        multiplicities, then using the counting theorem the number of divisors
        of n is equal to the product

            (e_1 + 1) x (e_2 + 1) x ... x (e_k + 1)
    """
    return int_product((pf[1] + 1) for pf in prime_factors(n, multiplicities=True))
