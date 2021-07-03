from random import randint
from time import perf_counter

NUM_MAX = 100

nums = [randint(1, NUM_MAX) for num in range(1, NUM_MAX + 1)]  # генерация списка случайных чисел
print(nums)  # вывод на экран для проверки правильной последовательности unique_nums
start = perf_counter()
unique_nums = [num for num in nums if nums.count(num) == 1]  # генерация списка уникальных чисел
print(perf_counter() - start)
print(unique_nums)  # сверка с оригинальным списком

