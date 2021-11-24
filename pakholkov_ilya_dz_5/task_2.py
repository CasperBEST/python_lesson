# Генератор чисел от 1 до max_num с помощью генераторного выражения

max_num = 10
nums_generator = (num for num in range(1, max_num + 1))

print(*nums_generator)

# print(next(nums_generator))  # 1
# print(next(nums_generator))  # 2
# print(next(nums_generator))  # 3
# print(next(nums_generator))  # 4
# print(next(nums_generator))  # 5
# print(next(nums_generator))  # 6
# print(next(nums_generator))  # 7
# print(next(nums_generator))  # 8
# print(next(nums_generator))  # 9
# print(next(nums_generator))  # 10
# print(next(nums_generator))  # ...StopIteration
