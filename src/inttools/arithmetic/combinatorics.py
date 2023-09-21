from .digits import generalised_product


def factorial(n):
    return generalised_product(range(1, n + 1))


def multinomial(n, *ks):
    """
    Returns the multinomial coefficient ``(n; k_1, k_2, ... k_m)``, where
    ``k_1, k_2, ..., k_m`` are non-negative integers such that
    ::

        k_1 + k_2 + ... + k_m = n

    This number is the coefficient of the term
    ::

       x_1^(k_1)x_2^(k_2)...x_m^(k_m)

    (with the ``k_i`` summing to ``n``) in the polynomial expansion
    ::

    (x_1 + x_2 + ... x_m)^n

    The argument ``ks`` can be separate non-negative integers adding up to the
    given non-negative integer ``n``, or a list, tuple or set of such
    integers prefixed by ``'*'``, e.g. ``*[1, 2, 3]``.
    """
    return int(factorial(n) / generalised_product(map(factorial, ks)))


def binomial(n, k):
    """
    Returns the familiar binomial cofficient - the number of ways
    of choosing a set of ``k`` objects (without replacement) from a set of
    ``n`` objects.
    """
    return multinomial(n, k, n - k)


def binomial2(n, k):
    """
    Faster binomial method using a more direct way of calculating factorials.
    """
    m = min(k, n - k)
    return int(generalised_product(range(n - m + 1, n + 1)) / generalised_product(range(1, m + 1)))