# Задание No1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
from typing import Callable


def guess() -> Callable:
    num: int = int(input('Enter number between 1 and 100: '))
    tries: int = int(input('Enter amount tries between 1 and 10: '))

    def input_num():
        nonlocal num
        nonlocal tries
        guess_num = -1
        for _ in range(tries):
            if guess_num != num:
                guess_num = int(input("Enter your guess: "))
            if guess_num == num:
                print(f'Bingo the number is {num}')
        if guess_num != num:
            print('Better luck another time')
    return input_num()


guess_func = guess()
