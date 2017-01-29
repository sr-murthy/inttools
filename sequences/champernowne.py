
def champernowne_sequence(digits=None):
    """
        The Champernowne constant is an irrational number 

            0.12345678910111213141516171819202122...

        with a significant digit of 0 and whose fractional part is obtained
        by concatenating the sequence of positive integers 1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, etc. See

            https://en.wikipedia.org/wiki/Champernowne_constant

        for more information.

        This method generates the sequence of all the digits in the fractional
        part of the number. The optional parameter 'digits' can be used to
        specify an upper bound for the number of digits.
    """
    d = 0
    i = 1
    while True:
        if len(str(i)) == 1:
            yield i
            d += 1
            if digits and d == digits:
                return
        else:
            for c in str(i):
                yield int(c)
                d += 1
                if digits and d == digits:
                    return
        i += 1


def champernowne_sequence_term(n):
    """
        Returns the n-th digit of the fractional part of the Champernowne
        constant.
    """
    d = 0   
    m = 1
    while True:
        for c in str(m):
            d += 1
            if d == n:
                return int(c)
        m += 1
