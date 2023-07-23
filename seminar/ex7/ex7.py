# Задание
# 📌 Решить задачи, которые не успели решить на семинаре. 📌 Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import math
import random
from functools import wraps


def solve_equations(func):
    @wraps(func)
    def wrapper(*args):
        with open('random_nums.csv', 'r') as f_read:
            csv_read = csv.reader(f_read, dialect='excel', delimiter=';')
            for i, line in enumerate(csv_read):
                if i != 0:
                    a = int(line[0])
                    b = int(line[1])
                    c = int(line[2])
                    result = func(a, b, c)
                    print(f'{result = }')
    return wrapper


def write_json(func):
    list_results = list()

    @wraps(func)
    def wrapper(*args):
        file_name = 'log_' + func.__name__ + '.json'
        dict_func_data = dict()
        dict_func_data['a'] = args[0]
        dict_func_data['b'] = args[1]
        dict_func_data['c'] = args[2]
        result = func(*args)
        if result is not None:
            sol_dict = dict()
            for i, item in enumerate(result):
                sol_dict[('x_' + str(i + 1))] = item
            dict_func_data['solution'] = sol_dict
        else:
            dict_func_data['solution'] = 'None'

        list_results.append(dict_func_data)
        with open(file_name, 'w') as f_rw:
            json.dump(list_results, f_rw, ensure_ascii=False, indent=2)
        print('write json ', func.__name__, args)
    return wrapper


def rand_generator():
    with open('random_nums.csv', 'w') as f_write:
        csv_write = csv.writer(f_write, dialect='excel', delimiter=';')
        csv_write.writerow(['a', 'b', 'c'])
        for _ in range(150):
            row_list: list = list()
            for _ in range(3):
                row_list.append(random.randint(0, 1000))
            csv_write.writerow(row_list)


@solve_equations
@write_json
def find_roots(a, b, c):
    disc = b ** 2 - 4 * a * c
    x_1: float
    x_2: float
    if disc > 0:
        x_1 = ((-b) + math.sqrt(disc)) / (2 * a)
        x_2 = ((-b) - math.sqrt(disc)) / (2 * a)
        return x_1, x_2
    elif disc == 0:
        x_1 = ((-b) / (2 * a))
        return x_1


find_roots(10, 20, 20)
