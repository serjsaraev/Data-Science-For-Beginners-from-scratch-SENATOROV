"""Векторы в линейной алгебре."""

import numpy as np

# Создадим неориентированный вектор
list_vec = [1, 2, 3]  #
arr_vec = np.array(
    list_vec
)  # это одномерный массив скобочки одинираные = неориентированный вектор
arr_vec.ndim  # показывает количество измерений
arr_vec.shape  # показывает количество строк и столбцов (3,) 1- param row, 2 - column

# Создадим ориентированный вектор
row_vec = np.array([list_vec])  # двумерный массив  , row vector
col_vec = np.array([[1], [2], [3]])
col_vec.shape  # (3, 1) три строки и один столбец

col_vec

col_vec.ndim

# broadcasting / транслирование
row_vec + col_vec

row_vec + row_vec

row_vec * 5

row_vec * 0.5
row_vec * 1 / 2

dir(row_vec)

# транспонирование
row_vec.T
# array([[1],
#    [2],
#    [3]])

row_vec * row_vec  # адомаромарово произведение
