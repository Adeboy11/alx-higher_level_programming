#!/usr/bin/python3
"""using numpy to multiply a matrices."""
import numpy as nump


def lazy_matrix_mul(m_a, m_b):
    """Returns the mult of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (nump.mul(m_a, m_b))
