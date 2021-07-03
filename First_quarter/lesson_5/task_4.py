from random import randint
import sys
from time import perf_counter

NUM_COUNT = 10000  # количество генерируемых чисел
nums = [randint(1, 100) for num in range(1, NUM_COUNT + 1)]  # генерация списка случайных чисел
#  print(nums) вывод списка на экран
start = perf_counter()  # старт таймера для comprehension
result = [num for num in nums if num > nums[nums.index(num) - 1]]  # использование comprehension ведет к увеличению
#  print(result)                                                      # занимаемого места и немного замедляет работу
print(perf_counter() - start)  # старт таймера для генератора
print(sys.getsizeof(result))  # вывод занимаемого места для comprehension
start = perf_counter()

result = (num for num in nums if num > nums[nums.index(num) - 1])  # использование генератора, а не comprehension
print(perf_counter() - start)                                      # снижает занимаемое место
print(sys.getsizeof(result))                                       # и ускоряет работу
