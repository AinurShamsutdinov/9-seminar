# Задание No3
# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
#       возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.
import json
import uuid
from typing import Callable


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


@write_json
def call_func(number_1: int, number_2: int) -> int:
    return number_1 * number_2


@write_json
def test_func(number_1: int, number_2: int, number_3: int) -> int:
    return number_1 + number_2 + number_3


call_func(2420, 2322)
test_func(484, 342, 958)
