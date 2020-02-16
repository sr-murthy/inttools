__all__ = [
    '_divisors',
    'd',
    'divisors',
    's',
    'sigma',
    'sigma_k_func'
]

from collections import OrderedDict

from itertools import (
    product,
    starmap,
)

from functools import partial

from inttools.primes import prime_factors
from inttools.arithmetic import (
    generalised_product,
    generalised_sum,
)


def _divisors(n):
    """
    Generates the sequence of divisors of a given positive integer n, in
    ascending order, e.g.:

        312 -> 1, 2, 3, 4, 6, 8, 12, 13, 24, 26, 39, 52, 78, 104, 156, 312
    """
    pfs = OrderedDict((pf[0], pf[1]) for pf in prime_factors(n, multiplicities=True))
    divs = [
        generalised_product(
            starmap(
                pow, zip(pfs.keys(), mt))) for mt in product(*(range(pfs[p] + 1) for p in pfs
            )
        )
    ]
    divs.sort()
    for div in divs:
        yield div


def divisors(n, generator=False):
    """
    This is a wrapper for the divisors generator to allow the divisors to be
    returned as a list.
    """
    divs = _divisors(n)
    if not generator:
        return [d for d in divs]
    return divs


def d(n):
    """
    Returns the number of all divisors of a given positive integer ``n``,
    including proper and improper divisors, e.g. the divisors of ``10``
    are ``1``, ``2``, ``5``, ``10`` so we will get a result of ``4``.
    ::
        10 -> 2

    Uses the prime factorization of ``n``: if ``n`` has the prime factorisation
    ::
        n = p_1^e_1 x p_2^e_2 x ... p_k^e_k

    (where the ``p_i`` are the prime factors of ``n`` and ``e_i`` are their 
    multiplicities, then using the counting theorem the number of divisors
    of ``n`` is equal to the product
    ::
        (e_1 + 1) x (e_2 + 1) x ... x (e_k + 1)
    """
    return generalised_product((pf[1] + 1) for pf in prime_factors(n, multiplicities=True))


def sigma(n, k):
    """
    The sum of the k-th powers of the divisors of n - in number theory this
    is traditionally denoted by \sigma_k(n) (LaTeX notation):

        (12, 2) -> 1^2 + 2^2 + 3^2 + 4^2 + 6^2 + 12^2 = 210
    """
    return generalised_sum(_divisors(n), k=k)


def sigma_k_func(k):
    """
    Returns the restriction of the sigma function obtained by fixing k, e.g.

        >>> s2 = sigma_k_func(2)

        >>> s2(12)
        >>> 210
    """

    return partial(sigma, k=k)


def s(n):
    """
    Returns sum of the proper divisors of a positive integer n, e.g.

        12 -> 1 + 2 + 3 + 4 + 6 = 16
     """
    return sum(filter(lambda d: d < n, _divisors(n)))

