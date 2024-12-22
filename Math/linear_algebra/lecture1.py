"""Vectors.

Python programming.
"""

# mypy: allow-untyped-defs
# mypy: allow-untyped-calls
import numpy as np

# ![image.png](attachment:image.png)

# L2 norm
# Euclidean distance
#
#
# ![image.png](attachment:image.png)

vc = np.array([1, 2, 3, 7, 8, 9])
VC_DIM = len(vc)
vc_mag = np.linalg.norm(vc)


def norm_of_vector(vt):
    """Return a norm of a vector."""
    return np.sqrt(np.sum(vt**2))


norm_of_vector(vc)

vc_mag  # для сравнения с norm_of_vector

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# w_unit = np.array([0, 1, 0])
wt = np.array([1, 3, 0])


def vector_to_unit_vector(vt):
    """Return a vector to unit vector."""
    norm_of_vector2 = np.linalg.norm(vt)
    return vt / norm_of_vector2


vector_to_unit_vector(wt)

vector_to_unit_vector(np.zeros((4, 1)))  # error


# ![image.png](attachment:image.png)


def mag_vector(vct, mag):
    """Return a vector in the same direction with a magnitude."""
    norm = norm_of_vector(vct)
    return mag * vct / norm


wt = np.array([1, 0, 0])
mag_vector(wt, 2)

data = [1.72, 54, 36.2]
# type(data)

data_numpy = np.array(data)

data_matrix = np.array([[1.72, 54, 36.2], [1.74, 58, 36.3], [1.68, 52, 32.9]])

data_matrix  # визуализация матрицы

data_matrix.shape
