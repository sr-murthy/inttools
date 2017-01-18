from itertools import (
    permutations,
    starmap,
)

from ..special_numbers import is_polygonal_number

def is_polygonal_representative_set(int_set, poly_reps):
    """
        If P is a set of polygonal numbers a set S is called a P-polygonal
        representative set, or simply P-polygonal, if 

        Checks whether a given set of positive integers contains polygonal
        numbers of every type (n) specified in the set (or sequence)
        'poly_reps', e.g. whether for every value of n in 'poly_reps' there
        is an n-gonal number in the given set of integers, e.g. the set
        {2882, 8128, 8281} contains a triangular number (8128), a square number
        (8281) and a pentagonal number (8128).
    """
    return any(
        (
            False not in starmap(is_polygonal_number, zip(int_set, poly_rep_perm))
            for poly_rep_perm in permutations(poly_reps)
        )
    )