import math


def is_hilbert_number(n):
    """
    Simply check whether n is positive and the remainder of n is equal to 1
    modulus 4.
    """
    return n > 0 and n % 4 == 1


def is_hilbert_square(n):
    """
    I define a Hilbert square as the square of a Hilbert number - this is
    necessarily also a Hilbert number.

    If n is a Hilbert square it has the form

        n = (4k + 1)^2 = 16k^2 + 18k + 1

    for some positive integer k. Solving for k the positive solution is

        (-1 + sqrt(n)) / 4

    and to check whether a given n is a Hilbert square we simpy need to check
    that this is an integer.
    
    """
    return ((-1 + math.sqrt(n)) / 4).is_integer()


def is_hilbert_squarefree_number(n):
    """
    I define a "Hilbert squarefree" number as a positive integer not divisible
    by the square of any Hilbert number, i.e. by a Hilbert square.

    Note: the given n need not be a Hilbert number but could be any positive
    integer.

    """
    ubound = math.ceil(n / 2)
    for a in range(5, ubound + 1):
        if is_hilbert_square(a) and n % a == 0:
            return False
    return True


def is_squarefree_hilbert_number(n):
    """
    As defined in the problem a squarefree Hilbert number is a Hilbert number
    not divisible by the square of any Hilbert number, i.e. by a Hilbert
    square.

    It follows that this is just a special case of a Hilbert squarefree number
    which happens to be a Hilbert number.
    """
    return is_hilbert_number(n) and is_hilbert_squarefree_number(n)


def hilbert_numbers(int_range):
    for n in int_range:
        if is_hilbert_number(n):
            yield n


def hilbert_squares(int_range):
    for n in int_range:
        if is_hilbert_square(n):
            yield n


def hilbert_squarefree_numbers(int_range):
    for n in int_range:
        if is_hilbert_squarefree_number(n):
            yield n


def squarefree_hilbert_numbers(int_range):
    for n in int_range:
        if is_squarefree_hilbert_number(n):
            yield n


def hcount(number_type, int_range):
    if number_type == 'hilbert':
        return sum(1 for n in hilbert_numbers(int_range))
    elif number_type == 'hilbert square':
        return sum(1 for n in hilbert_squares(int_range))
    elif number_type == 'hilbert squarefree':
        return sum(1 for n in hilbert_squarefree_numbers(int_range))
    elif number_type == 'squarefree hilbert':
        return sum(1 for n in squarefree_hilbert_numbers(int_range))
