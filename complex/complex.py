import math

from ..utils import integerise

def complexify(r):
    """
        Turns a real number into a complex number if it not complex, otherwise
        returns the same number.
    """
    return complex(r) if not type(r) == complex else r


def complex_format(z):
    """
        Formats a complex number z = a + bi to ensure that real and/or
        imaginary parts a and b are displayed as integers if they are actually
        integers. This is because the display of Python native complex numbers
        is a bit inconsistent: complex numbers with a 0 real part can sometimes
        be displayed with the real part as -0. Also, complex numbers such as
        1 - 2.0j are better read as 1 - 2j.
    """
    if type(z) == int:
        return complex(z)
    elif type(z) == float:
            return complex(integerise(z))
    elif type(z) == complex:
        a, b = map(integerise, [z.real, z.imag])
        return complex(a, b)


def complex_reflections(z):
    """
        Generates a sequence of reflections of a complex number z = a + bi in the real
        and imaginary planes:

            z = a + bi -> a + bi, a - bi, -a - bi, -a + bi
    """
    z = complex_format(z)
    a, b = map(integerise, [z.real, z.imag])
    if a and b:
        yield z.conjugate()
        yield -z
        yield -z.conjugate()
        yield z
    elif a and not b:
        yield -a
        yield a
    elif b and not a:
        yield complex(0, b).conjugate()
        yield complex(0, b)
        

def complex_divide(z1, z2):
    """
        Divides complex numbers using explicit formulae for the real and
        imaginary parts of the quotient. Python supports division of native
        complex numbers but this is reported to be inconsistent for large
        operands.
    """
    a, b, c, d = z1.real, z1.imag, z2.real, z2.imag
    m = c**2 + d**2
    u, v = map(integerise, [(a*c + b*d) / m, (b*c - a*d) / m])
    return complex(u, v)


def is_gaussian_integer(z):
    """
        Checks whether a given real or complex number is a Gaussian integer,
        i.e. a complex number g = a + bi such that a and b are integers.
    """
    if type(z) == int:
        return True
    return z.real.is_integer() and z.imag.is_integer()


def gaussian_divisors(g):
    """
        Generates a sequence of Gaussian divisors of a rational or Gaussian
        integer g, i.e. a Gaussian integer d such that g / d is also a Gaussian
        integer.
    """
    if not is_gaussian_integer(g):
        return
    g = complex_format(g)
    ubound = math.ceil(math.sqrt(abs(g))) if g.real and g.imag else int(g.real) if g.real else int(g.imag)
    for a in range(ubound + 1):
        for b in range(ubound + 1):
            if a or b:
                d = complex(a, b)
                if is_gaussian_integer(complex_divide(g, d)):
                    for f in complex_reflections(d):
                        yield f

