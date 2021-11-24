# Генератор случайных чисел от 1 до max_num


def nums_generator(max_num):
    for n in range(1, max_num + 1):
        yield n


num = nums_generator(5)
print(next(num))  # 1
print(next(num))  # 2
print(next(num))  # 3
print(next(num))  # 4
print(next(num))  # 5
print(next(num))  # ...StopIteration
