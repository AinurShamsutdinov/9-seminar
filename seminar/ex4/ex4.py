# Задание No4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.
from typing import Callable


def decorator(func: Callable):
    repeat: int = 5

    def wrapper(*args, **kwargs):
        nonlocal repeat
        for i in range(repeat):
            func(*args, **kwargs)
    return wrapper


@decorator
def test_func(param) -> int:
    print(f'decorated function call with {param = }')


test_func('test')
