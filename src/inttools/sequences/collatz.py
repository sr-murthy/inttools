def collatz(n):
    """
        The Collatz sequence generating function:

            f(n) = (1/2)n if n is even, or 3n + 1 if n is odd
    """
    return int(n / 2) if n % 2 == 0 else 3*n + 1

def collatz_sequence_term(seed, k):
    """
        Finds the k-th term of the Collatz sequence with the given seed.
    """
    if k == 1:
        return seed
    a = seed
    for i in range(k - 1):
        a = collatz(a)
        if a == 1:
            return None if k > i + 2 else a
    return a


COLLATZ_CACHE = dict()


def collatz_sequence(seed):
    """
        Generates the entire Collatz sequence for the given seed.

        Uses a module-level global cache for the collatz transform
        values.
    """
    global COLLATZ_CACHE

    n = seed
    yield n

    def lookup_cache(n):
        try:
            return COLLATZ_CACHE[n]
        except KeyError:
            ...

    while True:
        m = lookup_cache(n) or collatz(n)
        COLLATZ_CACHE[n] = m
        yield m

        n = m

        if n == 1:
            break


def longest_sequence_seed(ubound):
    """
        Finds the seed (below the given upper bound) which generates the
        longest Collatz sequence, and also the length of this sequence.
    """
    max_seq_seed = 1
    max_seq_len = 1
    for seed in range(1, ubound):
        seq_len = sum(1 for t in collatz_sequence(seed))
        if seq_len > max_seq_len:
            max_seq_len = seq_len
            max_seq_seed = seed
    return max_seq_seed, max_seq_len
