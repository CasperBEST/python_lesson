# Скрипт выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла,
# а значения — общее количество файлов (в том числе и в подпапках)

import os

ROOT = 'some_data'


def get_key_dict(number):  # создание ключей
    i = 1
    while True:
        if number // 10:
            i += 1
        else:
            break
        number //= 10
    return 10 ** i


dict_size = {}
for root, dirs, files in os.walk(ROOT):  # узнаем размер файлов по заданному пути
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        key_dict = get_key_dict(size)
        if key_dict not in dict_size:  # если ключа в словаре нет - создаем
            dict_size[key_dict] = 0
        dict_size[key_dict] += 1  # увеличиваем значение по ключу в словаре
# сортируем словарь по ключам и выводим результат
sort_key = sorted(dict_size.keys())
sort_dict = {}
for key in sort_key:
    sort_dict[key] = dict_size[key]

for item in sort_dict:
    print(f'{item}: {sort_dict[item]}')
