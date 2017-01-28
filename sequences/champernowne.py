from ..special_numbers import (
    champernowne_constant,
    champernowne_digit,
)

def champernowne_sequence(digits=None):
    """
        A wrapper for the `champernowne_constant` function in the
        `special_numbers` module.
    """
    return champernowne_constant(digits=digits)


def champernowne_sequence_term(n):
    """
        A wrapper for the `champernowne_digit` function in the
        `special_numbers` module.
    """
    return champernowne_digit(n)