# Задание No5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.
import json
import uuid
from random import random
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


def write_json(func: Callable):
    file_name = func.__name__
    func_data: dict = {}
    try:
        with open((file_name + '.json'), 'r', encoding='utf-8') as f_json:
            func_data = json.load(f_json)
    except FileNotFoundError:
        print(f'File with name {file_name} does not exist')

    def wrapper(*args, **kwargs):
        nonlocal func_data
        current_func = dict()
        current_func['funcName'] = func.__name__
        if len(args) > 0 and len(kwargs) == 0:
            current_func['args'] = args
            result = func(*args)
        elif len(args) == 0 and len(kwargs) > 0:
            for key, item in kwargs:
                current_func[key] = item
            result = func(**kwargs)
        elif len(args) > 0 and len(kwargs) > 0:
            current_func['args'] = args
            for key, item in kwargs:
                current_func[key] = item
            result = func(*args, **kwargs)
        current_func['return'] = result
        func_call_id = uuid.uuid4()
        str_uuid = func_call_id.__str__()
        func_data[str_uuid] = current_func
        print(func_data)
        with open((file_name + '.json'), 'w', encoding='utf-8') as f_json:
            json.dump(func_data, f_json, ensure_ascii=False, indent=2)
        return result
    return wrapper


def decorator(func: Callable):
    repeat: int = 5

    def wrapper(*args, **kwargs):
        nonlocal repeat
        for i in range(repeat):
            func(*args, **kwargs)
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

