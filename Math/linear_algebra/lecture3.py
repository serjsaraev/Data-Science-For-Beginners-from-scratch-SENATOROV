"""Vectors.

Python programming. Third part.
"""

# +
import numpy as np
from numpy import array, diag, identity, trace
from numpy.linalg import det, inv, matrix_rank
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

# define square matrix
mx = array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(mx)
# extract diagonal vector
dg_v = diag(mx)
print(dg_v)
# create diagonal matrix from vector
dg_mrx = diag(dg_v)
print(dg_mrx)

# +
# Identity Matrix
# An identity matrix is a square matrix that does not change a vector when
# multiplied. The values of an identity matrix are known. All of the scalar
# values along the main diagonal (top-left to bottom-right) have the value
# one, while all other values are zero.

idnt_m = identity(3)
print(idnt_m)
# -

# orthogonal matrix
# define orthogonal matrix
mtrx = array([[1, 0], [0, -1]])
print(mtrx)
# inverse equivalence
inv_mx = inv(mtrx)
print(mtrx.T)
print(inv_mx)
# identity equivalence
idnt = mtrx.dot(mtrx.T)
print(idnt)

# invert matrix
# define matrix
mtr_a = array([[1.0, 2.0], [3.0, 4.0]])
print(mtr_a)
# invert matrix
mtr_b = inv(mtr_a)
print(mtr_b)
# multiply mtr_a and mtr_b
mltp = mtr_a.dot(mtr_b)
print(mltp)

# +
# matrix trace
# define matrix
mtx = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtx)
# calculate trace
m_trace = trace(mtx)
print(m_trace)

# tr(mtx) = mtx[0, 0] + mtx[1, 1] + mtx[2, 2]
# -

# matrix determinant
# define matrix
mt3 = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mt3)
# calculate determinant
det_mt3 = det(mt3)
print(det_mt3)

# vector rank
# rank
v1 = array([1, 2, 3])
print(v1)
vr1 = matrix_rank(v1)
print(vr1)
# zero rank
v2 = array([0, 0, 0, 0, 0])
print(v2)
vr2 = matrix_rank(v2)
print(vr2)

# matrix rank
# rank 0
M0 = array([[0, 0], [0, 0]])
print(M0)
mr0 = matrix_rank(M0)
print(mr0)
# rank 1
M1 = array([[1, 2], [1, 2]])
print(M1)
mr1 = matrix_rank(M1)
print(mr1)
# rank 2
M2 = array([[1, 2], [3, 4]])
print(M2)
mr2 = matrix_rank(M2)
print(mr2)
