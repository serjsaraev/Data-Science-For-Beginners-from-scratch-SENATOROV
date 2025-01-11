"""Vectors.

Python programming.
"""

# mypy: allow-untyped-defs
# mypy: allow-untyped-calls
import numpy as np
from matplotlib import pyplot as plt

# ![image.png](attachment:image.png)

# L2 norm
# Euclidean distance
#
# сильно штрафует выбросы в отличие от Манхэттенской нормы (L1), которая
# использует модуль
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

# Адамарово произведение - умножение каждого элемента 2х векторов друг на друга
#
# Важна одна размерность
#
# Коммутативность

# wt = np.array([1, 3, 0])
wwt = np.array([[2, 5, 7]])
wt = np.array([[1, 2, 3]])
vc_adam_product = wt * wwt
print(vc_adam_product)

# Бродкастинг = "транслирование" (такого нет в математике, только внутренняя
# нативная операция numpy), зато в математике есть внешнее произведение (dot
# outer)

wwt = np.array([[1, 5, 7]])
wt = np.array([[2, 3]])
v_broadcasting = wt.T * wwt
print(v_broadcasting)

# dot outer
#
# Бродкастинг и outer - внешне ведут себя одинаково, но есть различия.
# Бродкастинг - более гибкий

# +
wwt = np.array([[3, 5, 7]])
wt = np.array([[1, 2, 3]])

v_outer_product = np.outer(wt, wwt)
print(v_outer_product)
# -

# Скалярное произведение

wwt = np.array([3, 5, 7])
wt = np.array([1, 2, 3])
wt3 = np.array([1, 2, 3])
# # доказательство, что скалярное произведение коммутативно
# np.dot(wwt, wt) == np.dot(wt, wwt)

# Дистрибутивное правило

# +
# # aT(b+c) = aTb+aTC
# np.dot(wwt, wt + wt3) == np.dot(wwt, wt) + np.dot(wwt, wt3)
# -

# 2 интерпретации: геометрическая (угол между векторами) и алгебраическая
# (умножаем между собой или складываем вектора)
#
# Косинусное сходство - это угол между векторами cos(angle)=aTb/|a|*|b|

# ![image.png](attachment:image.png)

# +
v_hum1 = np.array([1.72, 54, 36.2])
v_hum2 = np.array([1.74, 58, 36.3])

numerator = np.dot(v_hum1, v_hum2)
v_1_len = np.linalg.norm(v_hum1)
v_2_len = np.linalg.norm(v_hum2)
denominator = v_1_len * v_2_len

# возвращает число, принимает угол
cos_similarity = numerator / denominator
# косинус - это число -1 - + 1
print(cos_similarity)

# обратная к косинусу, в радианах
angle_radians = np.arccos(cos_similarity)
# получаем арккосинус от косинуса между векторами
print(angle_radians)

# получаем угол в градусах по формуле радианы
grade_cos_similarity = angle_radians * 180 / np.pi  # angle_radians/360/2/np.pi
print(grade_cos_similarity)
# -

# Напишите цикл for для транспонирования вектора-строки в вектор-столбец без
# использования встроенной функции или метода, такого как np.transpose() или
# v.T. Данное упражнение поможет вам создавать и индексировать векторы с
# наделенной ориентацией

# +
v_add = np.array([])
# vector_to_transpose = np.array([[1.72], [54], [36.2]])
vector_to_transpose = np.array([[1.72, 54, 36.2]])
if len(vector_to_transpose) == 1:  # входит вектор-строка
    for i, coordinate in enumerate(vector_to_transpose[0]):
        v_add = np.append(v_add, (coordinate))
        v_add = np.reshape(vector_to_transpose, (-1, 1))
else:  # входит вектор-столбец
    for i, coordinate in enumerate(vector_to_transpose):
        v_add = np.append(v_add, (coordinate))
        v_add = np.array(v_add, ndmin=2)

print(v_add)

# +
# Гибкость бродкастинга - разные математические операции в отличие от outer
# product
twt = np.array([[1, 2, 3]])
twwt = np.array([[2, 4]])
broadcasttwt = twt.T + twwt
print(broadcasttwt)

outerttwt = np.outer(twt, twwt)
print(outerttwt)
# -

tw = np.random.randn(2)
rw = np.random.randn(2)

# +
tw_para = rw * (np.dot(tw, rw) / np.dot(rw, rw))
tw_perp = tw - tw_para

# tw, tw_para + tw_perp
# array([ 0.82625583, -0.96648386]), array([ 0.82625583, -0.96648386])
# -

int(np.dot(tw_para, tw_perp))  # orto 10**(-17), 1/1000000000000000000 = 0

plt.figure(figsize=(6, 6))

plt.plot([0, tw[0]], [0, tw[1]], color="k", linewidth=3, label=r"t")
plotwt = [0, rw[0]], [0, rw[1]]
plt.plot(plotwt, color=[0.7, 0.7, 0.7], linewidth=3, label=r"r")
plt.axis("equal")
plt.legend()
plt.show()

plottwt = [0, tw_para[0]], [0, tw_para[1]]
plt.plot(plottwt, "k--", linewidth=3, label=r"tw_perp")
plt.plot([0, tw_perp[0]], [0, tw_perp[1]], "k:", linewidth=3, label=r"tw_orto")
plt.axis("equal")
plt.legend()
plt.show()
