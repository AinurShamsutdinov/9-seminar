# Задание No2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.
import random
from typing import Callable


def input_checker(func: Callable):
    num: int = int(input('Enter number between 1 and 100: '))
    tries: int = int(input('Enter amount tries between 1 and 10: '))
    if not 1 <= num <= 100:
        num: int = random.randint(1, 100)
    if not 1 <= tries <= 10:
        tries: int = random.randint(1, 10)

    def wrapper():
        func(num, tries)

    return wrapper


@input_checker
def console_input(num, tries):
    guess_num = -1
    for _ in range(tries):
        if guess_num != num:
            guess_num = int(input("Enter your guess: "))
        if guess_num == num:
            print(f'Bingo the number is {num}')
            break
    if guess_num != num:
        print('Better luck another time')


console_input()
