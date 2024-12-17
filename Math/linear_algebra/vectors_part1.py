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
# -

# ![image.png](attachment:image.png)

vc2d = np.array([1, 2])
plt.plot([0, vc2d[0]], [0, vc2d[1]])
for i in range(10):
    sn = np.random.randn()
    sv = sn * vc2d
    plt.plot([0, sv[0]], [0, sv[1]])
plt.grid("on")
plt.axis((-4, 4, -4, 4))

# +
# dot product
# vc1 = np.array([2, 5, 4, 7]) #выше заданы как array
# vc2 = np.array([4, 1, 0, 2])
vcdot = np.dot(vc1, vc2)  # 2*4+5*1+0+2*7

print(vcdot)
# -

# vector broadcasting
vbrd = np.array([[1, 2, 3]]).T  # важно, что 2 квадратные скобки, тк вектор!
wbrd = np.array([[10, 20]])
brdsum = vbrd + wbrd  # addition in broadcasting
print(brdsum)

# +
# Tensor creation
tensor = np.array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
        [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    ]
)

print(tensor.shape)
print(tensor)
