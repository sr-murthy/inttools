from math import factorial
from .digits import generalised_product


def multinomial(n, *ks):
    """
        Returns the multinomial coefficient (n; k_1, k_2, ... k_m), where
        k_1, k_2, ..., k_m are non-negative integers such that

            k_1 + k_2 + ... + k_m = n.

        This coefficient is the coefficient of the term

           x_1^(k_1)x_2^(k_2)...x_m^(k_m)

        (with the k_i summing to n) in the expansion of

        (x_1 + x_2 + ... x_m)^n.

        The argument ks can be separate non-negative integers adding up to the
        given non-negative integer `n`, or a list, tuple or set of such
        integers prefixed by '*', e.g. *[1, 2, 3].
    """
    return int(factorial(n) / generalised_product(map(factorial, ks)))


def binomial(n, k):
    """
        Returns the familiar binomial cofficient - the number of ways
        of choosing a set of `k` objects (without replacement) from a set of
        `n` objects.
    """
    return multinomial(n, k, n - k)