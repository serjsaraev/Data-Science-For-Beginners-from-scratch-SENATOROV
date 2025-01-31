"""Vectors.

Python programming. Second part.
"""

# +
# mypy: allow-untyped-defs
# mypy: allow-untyped-calls
import numpy as np
from matplotlib import pyplot as plt

# from plotly import graph_objects as go
# -

# Перепишите исходный код линейно-взвешенной комбинации, но поместите скаляры
# в список, а векторы – в качестве элементов в списке (таким образом, у вас
# будет два списка, один из скаляров и один из массивов NumPy). Затем примените
# цикл for, чтобы реализовать операцию линейно-взвешенной комбинации.
# Инициализируйте выходной вектор функцией np.zeros(). Подтвердите, что вы
# получаете тот же результат, что и в приведенном ранее исходном коде.

# +
# Linear weighted combinations
l1, l2, l3 = 1, 2, 3
wc1 = np.array([4, 6, 8])
wc2 = np.array([3, 7, 0])
wc3 = np.array([9, 1, 6])

lin_weight_comb = l1 * wc1 + l2 * wc2 + l3 * wc3
print(lin_weight_comb)
# Линейно-взвешенная комбинация означает умножение на скаляр и сложение
# векторов в множестве
# -

# Затем примените цикл for, чтобы реализовать операцию линейно-взвешенной
# комбинации. Инициализируйте выходной вектор функцией np.zeros(). Подтвердите,
# что вы получаете тот же результат, что и в приведенном ранее исходном коде.

# +
scalars_list = [l1, l2, l3]
vectors_list = [wc1, wc2, wc3]

# initialize the linear combination
# signature
# zeros(shape, dtype=float, order='C', *, like=None)
# # np.zeros?

# lim_combo = np.zeros(wc1.shape)
# lim_combo = np.zeros(tuple)
# lim_combo = np.zeros((1,3))
# lim_combo = np.zeros(len(wc1))
lim_combo = np.zeros(3)
# array([0., 0., 0.])
# [(scalar1,vec), (scalar2,vec)]

# Функциональное программирование

# Unpacking iterator
# for in list
# list(zip(scalars_list,vectors_list))
# lim_combo + [1,2,3]

for svl, vvl in zip(scalars_list, vectors_list):
    # print('1:',s,'2:',v)
    lim_combo += svl * vvl
    # print(lim_combo)
print(lim_combo)
# -

type(wc1.shape)

#  local scope or the attributes and methods of a specific object.
# dir(wc1)
wc1.shape

# +
# Whether it works or throws an error depends on how you set up the code.
# Using zip() as above works, because zip() will use only the
# minimum-matching items.
# Re-writing the code using indexing will cause an error, as in the code
# below.
scalars_list = [l1, l2, l3]

for i in enumerate(scalars_list):
    # print(vectors_list[i])
    lim_combo += scalars_list[0] * vectors_list[0]

print(lim_combo)
# -

# Базис – это линейка для измерения пространства. Множество векторов может быть
# базисом для подпространства, если оно
#
# 1) охватывает это подпространство и
#
# 2) является линейно независимым.

# +
vct = np.array([1, 3])
xlim = [-4, 4]

scalars = np.random.uniform(low=xlim[0], high=xlim[1], size=100)
plt.figure(figsize=(6, 6))

# in - оператор членства
for ivl in scalars:
    pv = vct * ivl
    print(pv)
    # plt.plot(pv[0],pv[1],'ko')
    # plt.show()
# -

# X~U

# +
# # two vectors in R3
# v1 = np.array([3, 5, 1])
# v2 = np.array([0, 2, 2])

# # uncomment the lines below for the second part
# # v1 = np.array([ 3.0,5.0,1.0 ])
# # v2 = np.array([ 1.5,2.5,0.5 ])


# # random scalars in the x-axis range
# scalars = np.random.uniform(low=xlim[0], high=xlim[1], size=(100, 2))


# # create random points
# points = np.zeros((100, 3))
# for i in range(len(scalars)):

#     # define this point as a random weighted combination of the two vectors
#     points[i, :] = v1 * scalars[i, 0] + v2 * scalars[i, 1]


# # draw the dots in the plane
# fig = go.Figure(
#     data=[
#         go.Scatter3d(
#             x=points[:, 0],
#             y=points[:, 1],
#             z=points[:, 2],
#             mode="markers",
#             marker={"size": 6, "color": "black"},
#         )
#     ]
# )

# fig.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 0})
# plt.savefig("Figure_03_07b.png", dpi=300)
# fig.show()
# -

scalars

# ![image.png](attachment:image.png)

AMTRX = np.arange(60).reshape(6, 10)

np.arange(60)

AMTRX

sub = AMTRX[1:4:1, 0:5:1]

# Подматрица
sub

# +
# Матрица случайных чисел
M_ROW = 4
N_COL = 6

# AMTRX = np.random.randn(M_ROW, N_COL)

# +
# randn - random numbers from a standard normal distribution.
# AMTRX

# +
# скалярное произведение матриц

frs_mtrx = np.array([[1, 2], [3, 4], [5, 6]])

scd_mtrx = np.array([[1, 2], [3, 4]])

res_mtrx = frs_mtrx @ scd_mtrx

print(res_mtrx)
# -

# <!-- # # two vectors in R3
# v1 = np.array([3, 5, 1])
# v2 = np.array([0, 2, 2])
#
# # uncomment the lines below for the second part
# # v1 = np.array([ 3.0,5.0,1.0 ])
# # v2 = np.array([ 1.5,2.5,0.5 ])
#
#
# # random scalars in the x-axis range
# scalars = np.random.uniform(low=xlim[0], high=xlim[1], size=(100, 2))
#
#
# # # create random points
# # points = np.zeros((100, 3))
# # for i in range(len(scalars)):
#
# #     # define this point as a random weighted combination of the two vectors
# #     points[i, :] = v1 * scalars[i, 0] + v2 * scalars[i, 1]
#
#
# # # draw the dots in the plane
# # fig = go.Figure(
# #     data=[
# #         go.Scatter3d(
# #             x=points[:, 0],
# #             y=points[:, 1],
# #             z=points[:, 2],
# #             mode="markers",
# #             marker={"size": 6, "color": "black"},
# #         )
# #     ]
# # )
#
# # fig.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 0})
# # plt.savefig("Figure_03_07b.png", dpi=300)
# # fig.show() -->
