"""epsilon

Computes neighbor representable float.

For any float `f` such that `abs(f) < float.max`,
`next_float64(previous_float64(f)) == previous_float64(next_float64(f)) == f`
holds.

Note: works only in python implementations where `float` is IEEE754 64-bit float.
"""


import ctypes


def next_float64(f):
    """Computes next representable float.

    Given a 64-bit float `f`, returns the minimal representable float that is greater than `f`.

    Irregulars:
        - `inf` => `nan`
        - `float.max` => `inf`
        - `-inf` => `-float.max`
        - `nan` => `nan`
    """

    return -_nei(-f, -1) if f < 0 else _nei(f, 1)


def previous_float64(f):
    """Computes previous representable float.

    Given a 64-bit float `f`, returns the maximal representable float that is smaller then `f`.

    Irregulars:
        - `-inf` => `nan`
        - `-float.max` => `-inf`
        - `inf` => `float.max`
        - `nan` => `nan`
    """

    return -_nei(-f, 1) if f <= 0 else _nei(f, -1)


def _nei(f, s):
    return ctypes.c_double.from_buffer(ctypes.c_ulonglong(
            ctypes.c_ulonglong.from_buffer(ctypes.c_double(f)).value + s
        )).value
