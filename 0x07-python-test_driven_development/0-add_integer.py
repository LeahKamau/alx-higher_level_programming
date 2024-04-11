#!/usr/bin/python3
"""

This module contains a function adds two numbers

"""


def add_integer(a, b=98):
    """

    This function adds two integers and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        sum of two given numbers

    Raises:
        TypeError: if a or b are not integers or floats

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b

