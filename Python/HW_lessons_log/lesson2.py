"""Модуль по Математическим операторам."""

# +
# from typing import Tuple

# https://sky.pro/wiki/python/ukazanie-tipa-elementov-v-spiske-python-annotatsii-tipov/
# -

1 + 1, 8 - 1, 10 * 2, 35 / 5

# деление по модулю, остаток от деления
7 % 3

# +
# возведение в степень
# 2**3

for number in range(10):
    print(number)
# -

help(range)

# +
# сигнатура объекта - это его описание вызывается знаком ?
# # range?
# -

1 + 3 * 2

5

# <img src="https://www.programiz.com/sites/tutorial2program/files/create-function-python.png">

# +
# Для создания / определения функции мы используем ключевое слово def
# def(keyword) func_name():
# body / ... / pass
# по умолчанию если не писать в теле функции return то интерпретатор
# прописывает return None


# Void функция.


def greet() -> None:
    """Функция выводит текст на экран."""
    print("hello world")

    # return None пишет это автоматически


# call func => func_name + ()
# () => arguments
greet()


# +
# pseudo_name_of_funk = greet()

# +
# print(pseudo_name_of_funk)


# +
def greet_return() -> str:
    """Функция возвращает текст."""
    # Оператор return возвращает значение из функции
    return "hello world"


# функция type показывает тип данных
type(greet_return())
# -

pseudo_name_of_funk = greet_return()
pseudo_name_of_funk

# Функции делятся на два типа:
# 1. Войд - это не результирующая функция, возхвращает  None  нет return
# 2. Результирующая функция - функция где есть rerturn
# 3.

# <img src="https://www.programiz.com/sites/tutorial2program/files/working-of-function-python.png">

# +
# def func_name(param1, param1):
#   body

# def sum_to_numbers(num1: int, num2: int) -> int:
# '''The code defines a function named `sum_to_numbers` that takes two
# parameters `num1` and `num2`, both of which are integers. The function
# returns the sum of `num1` and `num2`. The return type of the function is
# specified as `int`, indicating that the function will return an integer
# value.h'''
#     return num1 + num2


def sum_to_numbers(num1: int, num2: int) -> int:
    """Функция отдает сумму двух чисел.

    Args:
        num1 (int): первое число
        num2 (int): второе число

    Returns:
        int: сумма двух чисел
    """
    return num1 + num2


# sum_to_numbers(arg)
sum_to_numbers(2, 3)  # позиционные аргументы
sum_to_numbers(num1=3, num2=2)  # ключевые аргументы


# +
def say_hello(string: str = "Hello") -> str:
    """Функция выдает строку.

    Args:
        string (str, optional): текст. Defaults to "Hello".

    Returns:
        str: текст
    """
    # конструкция f-stringr позволяет подставить переменную в строку:
    return f"{string} word"


# say_hello("By,")
say_hello()

# +
# def find_sume(*numbers: int) -> Tuple[int, ...]:
#     """Функция выдает числа.

#     Returns:
#         Tuple[int, ...]: список
#     """
#     for num in numbers:
#         print(num)
#     return numbers


# find_sume(1, 2, 3)
