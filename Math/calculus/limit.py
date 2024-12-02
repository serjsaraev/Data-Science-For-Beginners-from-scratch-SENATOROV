# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
"""Example of limits."""

# %%
import sympy as sp

# %% [markdown]
# #### 1. Обычный предел функции:

# %%
x_ = sp.symbols("x")
# Определяем функцию
f_ = sp.sin(x_) / x_

# Вычисляем предел, когда x стремится к 0
limit_at_0 = sp.limit(f_, x_, 0)
print(f"Предел sin(x)/x при x -> 0: {limit_at_0}")

# %% [markdown]
# #### 2. Односторонние пределы:

# %%
# Левосторонний предел
left_limit = sp.limit(f_, x_, 0, dir="-")
print(f"Левосторонний предел sin(x)/x при x -> 0: {left_limit}")

# Правосторонний предел
right_limit = sp.limit(f_, x_, 0, dir="+")
print(f"Правосторонний предел sin(x)/x при x -> 0: {right_limit}")

# %% [markdown]
# #### 3. Пределы бесконечности:

# %%
# Предел функции, когда x стремится к бесконечности
f2 = x_**2 / (x_**2 + 1)
limit_infinity = sp.limit(f2, x_, sp.oo)
print(f"Предел x^2 / (x^2 + 1) при x -> бесконечность: {limit_infinity}")


# %% [markdown]
# #### 4. Предел последовательности:

# %%
n_ = sp.symbols("n")
# Определение последовательности
sequence = 1 / n_

# Предел последовательности, когда n стремится к бесконечности
limit_sequence = sp.limit(sequence, n_, sp.oo)
print(f"Предел 1/n при n -> бесконечность: {limit_sequence}")

# %% [markdown]
# #### 5. Сложные пределы:

# %%
# Определяем более сложную функцию
f3 = (sp.sin(x_) ** 2) / (x_**2)

# Предел при x стремящемся к 0
limit_complex = sp.limit(f3, x_, 0)
print(f"Предел sin^2(x)/x^2 при x -> 0: {limit_complex}")
