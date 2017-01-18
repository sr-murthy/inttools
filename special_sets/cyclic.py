from itertools import permutations

def is_d_cyclic_set(int_set, d):
    """
        Checks whether a given set (or sequence) of positive integers has the
        d-cyclic property, namely that there exists an (ordered) sequence of
        all the integers from this set such that for any two consecutive
        integers in the sequence the d least significant digits of the first
        integer are equal to the d most significant digits of the second,
        this being true for the last and first integers as well, e.g. the
        set {2882, 8128, 8281} is 2-cyclic because the sequence

            8128, 2882, 8281

        has the 2-cyclic property.
    """
    m = len(int_set)
    for p in permutations(int_set):
        if all(str(p[i])[-d:] == str(p[(i + 1) % m])[:d] for i in range(m)):
            return True
    return False
