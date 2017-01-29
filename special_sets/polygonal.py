from itertools import (
    permutations,
    starmap,
)

from special_numbers import is_polygonal_number

def is_polygonal_representative_set(int_set, poly_reps):
    """
        If P is a set of polygonal side lengths n, a set S is called a
        P-polygonal representative set, or simply P-polygonal, if S
        consists of a different n-gonal number for every n in P, e.g.
        the set {2882, 8128, 8281} is {3,4,5}-polygonal because it
        contains the triangular number 8128, the square number 8281 and
        the pentagonal number 2882.
    """
    return any(
        (
            False not in starmap(is_polygonal_number, zip(int_set, poly_rep_perm))
            for poly_rep_perm in permutations(poly_reps)
        )
    )