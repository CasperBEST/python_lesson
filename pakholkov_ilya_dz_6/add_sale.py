"""
Данный скрипт записывает переданные значения в файл backery.py, каждый раз с новой строки.
Если файла не существует, он будет создан.
"""
import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    n = 10 - len(sys.argv[1])
    list_sale = sys.argv[1]
    for i in range(1, n + 1):  # дополняем строку пробелами до одинаковой длины и сохраняем в файл
        list_sale += ' '
    f.write(list_sale + '\n')
