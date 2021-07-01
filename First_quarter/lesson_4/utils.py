import task_2  # импортирование пользовательского и системного модулей
import sys


print(task_2.currency_rates("aud"))  # проверка, что код выполняется только из этого скрипта
print(task_2.currency_rates("byn"))

try:
    print(task_2.currency_rates(sys.argv[1]))
except IndexError:  # если аргумент, который принимает функция не введен
    print("Введите код валюты")
