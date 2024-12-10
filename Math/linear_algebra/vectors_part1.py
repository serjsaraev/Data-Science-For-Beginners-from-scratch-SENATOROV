"""Vectors."""

# +
import numpy as np
from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt не проходит по линтерам

vector = np.array([2, -1])
plt.plot([0, vector[0]], [0, vector[1]])  # X,Y
plt.axis((-3, 3, -3, 3))  # в оригинале [], но выскакивают как проблема

# +
v1 = [2, 5, 4, 7]  # list
v2 = np.array([2, 5, 4, 7])  # array, no orientation
v3 = np.array([[2], [5], [4], [7]])  # column vector
v4 = np.array([[2, 5, 4, 7]])  # row vector
v4transposed = v4.T  # column vector from row vector

print(v1, v2, v3, v4, v4transposed)

# +
# важно не одноименные переменные иметь, ибо конфликт форматов
vc1 = np.array([2, 5, 4, 7])
vc2 = np.array([4, 1, 0, 2])
vc3 = 4 * vc1 - 2 * vc2

print(vc3)
