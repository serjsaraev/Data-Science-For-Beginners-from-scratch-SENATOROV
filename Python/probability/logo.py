"""Урок распределение Пуассона."""

# 1. Изучили закон распределения Пуассона, который описывает вероятность того, что некоторое событие
# произойдет определённое количество раз за фиксированное время или в заданной области, если эти
# события происходят с постоянной средней интенсивностью и независимо друг от друга. Закон является
# хорошим приближением для биноминального распределения при больших значениях n и малых р, поэтому его
# называют законом редких явлений.
# Примеры:
# - число родившихся за определнный период близнецов;
# - число регистрируемых на АТС вызовов за определенный промежуток времени;
# - число опечаток в большом тексе;
# - число бракованных деталей в большой партии и т.д.
# Математическое ожидание и дисперсия в СВ, распределенной по закону Пуассона - равны между собой и
# равны параметру а (а = np). Если мат ожидание и дисперсия значительно разнятся между собой, то нет оснований
# такое распределение СВ считать пуассоновским.
#

# ![image.png](attachment:image.png)

# калькулятор Пуассон:
# https://math.semestr.ru/probability/poisson.php
#

# Таблица значений функции Пуассона:
#  https://www.matematicus.ru/teoriya-veroyatnosti/tablitsy/tablitsa-znachenij-funktsii-puassona

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# +
# Данные
num = 500  # Количество звонков
prob = 0.004  # Вероятность сбоя при одном звонке
lambda_ = num * prob  # Среднее число сбоев
k_ = 9  # Искомое число сбоев

# Генерируем значения для графика
ex = np.arange(0, 11)  # Возможные значения числа сбоев (от 0 до 14)
pmf_values = poisson.pmf(ex, lambda_)  # Вероятности

# Построение графика
plt.bar(ex, pmf_values, color="blue", alpha=0.6, label=f"P(λ={lambda_:.1f})")

# Выделяем вероятность P(X=9)
plt.bar(
    k_,
    poisson.pmf(k_, lambda_),
    color="red",
    alpha=0.8,
    label=f"P(X={k_}) = {poisson.pmf(k_, lambda_):.6f}",
)

# Подписи осей и заголовок
plt.xlabel("Число сбоев")
plt.ylabel("Вероятность")
plt.title(f"Распределение Пуассона (λ={lambda_:.1f})")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Показать график
plt.show()

# +
cdf_values = poisson.cdf(ex, lambda_)  # Вычисление CDF

# Построение графика
plt.plot(
    ex,
    cdf_values,
    marker="o",
    linestyle="-",
    color="blue",
    label=f"Poisson CDF (λ={lambda_:.1f})",
)

# Выделяем вероятность P(X ≤ 9)
plt.scatter(
    k_,
    poisson.cdf(k_, lambda_),
    color="red",
    zorder=3,
    label=f"P(X ≤ {k_}) = {poisson.cdf(k_, lambda_):.6f}",
)

# Подписи осей и заголовок
plt.xlabel("Число сбоев")
plt.ylabel("Вероятность P(X ≤ k)")
plt.title(f"Функция распределения (CDF) Пуассона (λ={lambda_:.1f})")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Показать график
plt.show()
