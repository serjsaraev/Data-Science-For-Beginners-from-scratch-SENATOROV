"""lesson3."""

# from .modul1 import *
# from .modul2 import *

# as псевдо нейм,устранение конфликта пространста имен
from .modul1 import value as val1
from .modul2 import value as val2

print("RUN __INIT__")
