numbers = []

for number in range(1, 1001):  # Генерация списка кубов нечетных чисел
    if number & 2 == 0:
        number = number ** 3
        numbers.append(number)
    else:
        continue

print(numbers)  # Вывод списка

# 2a:
sum_total = 0  # Переменная, которая будет содержать сумму чисел списка, сумма цифр которых делится на 7 нацело

for number in numbers:
    sum_digits = 0
    while number > 0:  # Цикл, считающий сумму цифр
        num = number % 10
        number = number // 10
        sum_digits += num
    if sum_digits % 7 == 0:  # Проверка деления на 7 нацело
        sum_total += sum_digits
    else:
        continue

print(sum_total)  # Вывод суммы чисел

# 2b:
new_numbers = []  # Новый список с числами, основанный на первом, с прибавлением 17 к каждому числу первого списка

for number in numbers:  # Цикл, прибавляющий к каждому числу первого списка 17 и добавляющий результат в новый список
    number += 17
    new_numbers.append(number)

print(new_numbers)  # Вывод нового списка

sum_total = 0  # Обновление переменной с суммой

for number in new_numbers:
    sum_digits = 0
    while number > 0:
        num = number % 10
        number = number // 10
        sum_digits += num
    if sum_digits % 7 == 0:
        sum_total += sum_digits
    else:
        continue

print(sum_total)

# 2c*: решение предыдущей задачи без создания нового списка
for i in range(len(numbers)):  # Замена элементов списка новыми значениями
    numbers[i] = numbers[i] + 17

sum_total = 0

for number in numbers:
    sum_digits = 0
    while number > 0:
        num = number % 10
        number = number // 10
        sum_digits += num
    if sum_digits % 7 == 0:
        sum_total += sum_digits
    else:
        continue

print(numbers)
print(sum_total)
#  end
