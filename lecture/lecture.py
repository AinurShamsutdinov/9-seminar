# def func(a):
#     x = 42
#     res = x + a
#     return res
#
#
# x = 73
# print(func(64))
##################################################################################
# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b
#
#
# print(add_str('Hello', 'world!'))
#
##################################################################################
# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#
#     return add_two_str
#
#
# print(add_one_str('Hello')('world!'))

##################################################################################
# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
# print(hello('world!'))
# print(hello('friend!'))
# print(bye('wonderful world!'))
# print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
##################################################################################
# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     names = []
#
#     def add_two_str(b: str) -> str:
#         names.append(b)
#         return a + ', ' + ', '.join(names)
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))
##################################################################################
# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''
#
#     def add_two_str(b: str) -> str:
#         nonlocal text
#         # text                     #UnboundLocalError: local variable 'text' referenced before assignment
#         text += ', ' + b
#         return a + text
#
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))
##################################################################################
# from typing import Callable
#
#
# def main(x: int) -> Callable[[int], dict[int, int]]:
#     d = {}
#
#     def loc(y: int) -> dict[int, int]:
#         for i in range(y):
#             d[i] = x ** i
#         return d
#     return loc
#
#
# small = main(42)
# big = main(73)
# print(small(7))
# print(big(7))
# print(small(3))
##################################################################################
import time
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в return result {time.time()}')
    return wrapper


def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
control = main(factorial)
print(f'{control.__name__ = }')
print(f'{control(1000) = }')
##################################################################################
# import time
# from typing import Callable
#
#
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в return result {time.time()}')
#     return wrapper
#
#
# @main
# def factorial(n: int) -> int:
#     f =1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000) = }')
##################################################################################
# from typing import Callable
#
#
# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#     print('Возвращаем декоратор A')
#     return wrapper_a
#
#
# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#     print('Возвращаем декоратор B')
#     return wrapper_b
#
#
# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#     print('Возвращаем декоратор C')
#     return wrapper_c
#
#
# def deco_d(func: Callable):
#     def wrapper_d(*args, **kwargs):
#         print('Старт декоратора D')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора D')
#         return res
#     print('Возвращаем декоратор D')
#     return wrapper_d
#
#
# @deco_d
# @deco_c
# @deco_b
# @deco_a
# def main(text):
#     print('Старт основной функции ', text)
#
#
# main('test')
##################################################################################
# from typing import Callable
#
#
# def cache(func: Callable):
#     _cache_dict = {}
#
#     def wrapper(*args):
#         if args not in _cache_dict:
#             _cache_dict[args] = func(*args)
#         return _cache_dict[args]
#     return wrapper
#
#
# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
##################################################################################
# import time
# from typing import Callable
#
#
# def count(num: int = 1):
#     def deco(func: Callable):
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#             print(f'Результаты замеров {time_for_count}')
#             return result
#         return wrapper
#     return deco
#
#
# @count(10)
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000) = }')
# print(f'{factorial(1000) = }')
##################################################################################
# import time
# from functools import wraps
# from typing import Callable
#
#
# def count(num: int = 1):
#     def deco(func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 stop = time.perf_counter()
#                 time_for_count.append(stop - start)
#             print(f'Результаты замеров {time_for_count}')
#             return result
#         return wrapper
#     return deco
#
#
# @count(10)
# def factorial(n: int) -> int:
#     """Returns the factorial of the number n."""
#     f =1
#     for i in range(2, n + 1):
#         f *= i
#         return f
#
#
# print(f'{factorial(1000) = }')
# print(f'{factorial.__name__ = }')
# help(factorial)
##################################################################################
# from functools import cache
#
#
# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#         return f
#
#
# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
##################################################################################
