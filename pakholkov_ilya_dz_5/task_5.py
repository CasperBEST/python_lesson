# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.

src = [2, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Вариант решения через словарь:
src_dict = dict()
for num in src:
    if num in src_dict:
        src_dict[num] += 1
    else:
        src_dict[num] = 1
print('Через словарь ', [key for key in src_dict if src_dict[key] == 1])

# Вариант решения через одно множество:
repeat_list = src[:]
for i in set(repeat_list):
    repeat_list.remove(i)
# выводим результат с сохранением порядка следования в исходом списке
print('Одно множество', [el for el in src if el not in repeat_list])

# Вариант решения через два множества:
unique_set = set()
repeat_set = set()
for num in src:
    if num in repeat_set:
        continue
    if num in unique_set:
        repeat_set.add(num)
        unique_set.discard(num)
        continue
    unique_set.add(num)
print('Два множества ', [num for num in src if num in unique_set])

# Вариант решения через count
print('Через count   ', [num for num in src if src.count(num) == 1])
