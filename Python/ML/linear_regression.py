"""Рассматриваем функцию потерь, функцию знаков."""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# L1 функция потерь MAE
# Для поиска весов градиентный спуск,
# используем градиентный спуск
# (численные метод,интерационный).
#
# Модульная функция не гладкая в
# нуле (недифференцуемая), будем доопределять

# ![alt text](image.png)

# +
list1 = [28, 25.6, 62, 54.4, 81.3]
list2 = [11.2, 42.6, 34.4, 66, 51.3]

data = {"x": list1, "y": list2}

df = pd.DataFrame(data)
# -

df

df.plot(x="x", y="y", kind="scatter")
plt.show()

# инициализация веса
weight, bias = 1, 1

df["y_pred"] = df["x"] * weight + bias

df

plt.scatter(df["x"], df["y"])
plt.plot(df["x"], df["y_pred"])
plt.show()

# MAE
df["error_abs"] = np.abs(df["y"] - df["y_pred"])

df["error_abs"].mean()

np.sign(-999)

np.sign(1000)

np.sign(0)

# ![alt text](image-5.png)
#

# - x1e1
# - |e1|

# +
# df['w_change'] = df['x'] * (df['y'] - df['y_pred']/
# np.abs( df['y'] - df)['y_pred']) MAE, деление на 0
# df['w_change'] = df['x'] * np.sign(df['y'] - df)['y_pred']

df["w_change"] = np.where(
    df["y"] != df["y_pred"],
    df["x"] * (df["y"] - df["y_pred"]) / np.abs(df["y"] - df["y_pred"]),
    0,
)  # if y_true - y_pred
# -

df

# минус значит отпускаем вниз
df["w_change"].mean()

df["b_change"] = np.sign(df["y"] - df["y_pred"])

df["b_change"].mean()

nu = 0.1

# +
# сдвинем немного w,b
# w = weight + nu * df["w_change"].mean()
# -

# w = weight +  nu  * df['w_change'].mean()
