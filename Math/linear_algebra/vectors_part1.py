"""Vectors."""

# +
import numpy as np
from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt не проходит по линтерам

vector = np.array([2, -1])
plt.plot([0, vector[0]], [0, vector[1]])
plt.axis([-3.0, 3.0, -3.0, 3.0])
