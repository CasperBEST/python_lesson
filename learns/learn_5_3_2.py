import random

names = {'Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна'}
new_names = {'Андрей', 'Пётр', 'Иван', 'Сергей'}
print(names.intersection(new_names))  # & сравнение
print(names.union(new_names))  # | сложение
print(names - new_names)

rnd_nums = {random.randint(1, 5) for _ in range(10)}
print(rnd_nums)

names = ('Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна')
new_names = ('Андрей', 'Пётр', 'Иван', 'Сергей')
my_set = {names, new_names}
name = 'Пётр'
i = 1
for tupl in my_set:
    if name in tupl:
        i += 1
print(i)

names = {'Иван', 'Анна', 'Игорь', 'Иван', 'Сергей', 'Анна'}
new_names = {'Андрей', 'Пётр', 'Иван', 'Сергей'}
my_typle = (names, new_names)
name = 'Пётр'
i = 0
for st in my_typle:
    if name in st:
        i += 1
print(i)
