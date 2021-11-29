"""
Скрипт выводит содержимое файла с нумерацией строк:
 - просто запуск скрипта — выводит все записи;
 - запуск скрипта с одним параметром-числом — выводит все записи с номера, равного этому числу, до конца;
 - запуск скрипта с двумя числами — выводит записи, начиная с номера, равного первому числу, по номер,
   равный второму числу, включительно.
"""
import sys

with open('bakery.csv', encoding='utf-8') as f:  # вывод всего списка
    if len(sys.argv) == 1:
        i = 1
        for line in f:
            print(i, ' ', line, end='')
            i += 1
    elif len(sys.argv) == 2:  # вывод списка с указанного номера до конца
        for n in range(1, int(sys.argv[1])):
            f.readline()
        i = int(sys.argv[1])
        for line in f:
            print(i, ' ', line, end='')
            i += 1
    elif len(sys.argv) == 3:  # вывод списка в интервале указанных номеров
        for n in range(1, int(sys.argv[1])):
            f.readline()
        i = int(sys.argv[1])
        for line in f:
            print(i, ' ', line, end='')
            i += 1
            if i > int(sys.argv[2]):
                break
