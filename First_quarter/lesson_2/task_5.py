import random  # импорт модуля для генерации чисел

prices = []  # создание списка для цен
prices_amount = 20  # количество цен в списке(опционально заменяется input, чтобы пользователь сам ввел желаемое)
prices_format = []  # создание списка для форматированных цен

for el in range(prices_amount):  # заполнение списка элементами типа float
    price = round(random.random() * 100, 2)  # генерация цены
    prices.append(price)  # добавление цены в список

for price in prices:  # форматирование цены
    temp_price = str(price).split(".")  # разделение на числа до и после точки
    r = temp_price[0]  # количество рублей
    kk = f"{int(temp_price[-1]):02}"  # количество копеек
    print(f"{r} руб {kk} коп")  # вывод форматированных цен
    prices_format.append(f"{r} руб {kk} коп")  # добавление форматированных цен в новый список

prices_increasing = sorted(prices_format)  # все цены по возрастанию
print(prices_increasing)
inverted_prices = sorted(prices_format, reverse=True)  # все цены по убыванию
print(inverted_prices)
top_5 = sorted(inverted_prices[:5])  # пять самых дорогих товаров по возрастанию
print(top_5)
