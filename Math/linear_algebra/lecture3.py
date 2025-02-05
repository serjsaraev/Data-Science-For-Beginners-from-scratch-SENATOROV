"""Vectors.

Python programming. Third part.
"""

# +
import numpy as np
from sympy import Matrix, symbols

# библиотека для символьных вычислений
# from sympy import *  # выкинули всё пространство ИМЕН *

# import sympy


# init_printing(use_unicode=True)
# -

mt = np.array([[7, -3], [1, 1], [9, -1]])

r_m = np.linalg.matrix_rank(mt)

print(r_m)

ms = Matrix([[1, 2, 3], [0, -1, 1]])

ms

x_v, y_v, z_v = symbols("x y z")
# symbols(names, *, cls=<class 'sympy.core.symbol.Symbol'>, **args) -> 'Any'

temp_matrix = Matrix([[1, x_v], [2, y_v]])

temp_matrix

Matrix.eye(3)

Matrix.zeros(2, 3)

Matrix.ones(3, 2)

tt = Matrix.diag(1, 5, -2)

Matrix.diag(-1, Matrix.ones(2, 2), Matrix([[5, 7, 5]]))

Matrix([[1, 2, 3]])

Matrix([[1], [2], [3]])

Matrix([1, 2, 3])

t_m = Matrix([1, 2, 3])

t_m.shape

dir(Matrix)

tt

tt[:, 1:2]

tt[:, 1:2]
