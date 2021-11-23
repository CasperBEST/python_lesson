# Генераторы.
from sys import getsizeof
from time import perf_counter

MAX_NUM = 10 ** 2


def nums_gen():
    for n in range(1, MAX_NUM + 1):
        if n % 7 == 0:
            yield n


start = perf_counter()
nums = []
for num in range(1, MAX_NUM + 1):
    if num % 7 == 0:
        nums.append(num)
# print(nums)
print(sum(nums), getsizeof(nums), perf_counter() - start)

start = perf_counter()
result = 0
for num in range(1, MAX_NUM + 1):
    if num in range(1, MAX_NUM + 1):
        if num % 7 == 0:
            result += num
print(result, perf_counter() - start)

start = perf_counter()
nums = nums_gen()
# print(nums)
# print(next(nums))
# print(next(nums))
# print(next(nums))
print(sum(nums), getsizeof(nums), perf_counter() - start)

start = perf_counter()
# nums = (num for num in range(1, MAX_NUM + 1) if num % 7 ==0)
# nums = (num if num % 7 == 0 else num ** 2 for num in range(1, MAX_NUM + 1))  # генератор
# nums = [num if num % 7 == 0 else num ** 2 for i in range(1, MAX_NUM + 1) for num in range(1, MAX_NUM + 1)]
# nums = {num: i ** 2 for i in range(1, MAX_NUM + 1) for num in range(1, MAX_NUM + 1)}
nums = {num for i in range(1, MAX_NUM + 1) for num in range(1, MAX_NUM + 1)}
print(sum(nums), getsizeof(nums), perf_counter() - start)
print(nums)
