"""Модуль для вычисления чисел Фибоначчи."""


def fib(num: int) -> None:
    """Print Fibonacci numbers up to n.

    Args:
        n: Upper limit for Fibonacci sequence

    Prints each Fibonacci number less than n, separated by spaces.
    """
    alfa, beta = 0, 1
    while alfa < num:
        print(alfa, end=" ")
        alfa, beta = beta, alfa + beta
    print()


def fib2(num: int) -> list[int]:
    """Return list of Fibonacci numbers up to n.

    Args:
        n: Upper limit for Fibonacci sequence

    Returns:
        List containing Fibonacci numbers less than n
    """
    result = []
    alfa, beta = 0, 1
    while alfa < num:
        result.append(alfa)
        alfa, beta = beta, alfa + beta
    return result
