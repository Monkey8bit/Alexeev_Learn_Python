#  задание с *
import requests  # импорт необходимых модулей
import datetime

# списки ниже не объявлены константами по причине того, что информация при парсинге может меняться

responce = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")  # парсинг с сайта
content = responce.content.decode(encoding=responce.encoding)  # декодирование информации
currency_list = []  # список с кодами валют
name_list = []  # список с названием валют, оба выведены за границы функции для вывода помощи по кодам валют
date = []  # пустой список для даты, пока не разобрался, как ее получить без него

for d in content.split('Date="')[1:]:  # поиск значений даты,
    date.append(d.split('"')[0])
for code in content.split("<CharCode>")[1:]:  # кода валюты,
    currency_list.append(code.split("<")[0])
for name in content.split("<Name>")[1:]:  # и наименования валюты в коде страницы
    name_list.append(name.split("<")[0])

current_date = datetime.datetime.strptime(*date, "%d.%m.%Y").date()  # приведение распакованного списка к типу date

print("Возможные для определения курса валюты: ")  # подсказка, как соотносить коды валют с их именами
for el, name in zip(currency_list, name_list):  # вывод подсказки через zip и списков с наименованиями и кодами валют
    print(f"{el}({name})")


def currency_rates(currency):  # сама функция, принимающая в качестве аргумента код валюты
    currency = currency.upper()  # приведение аргумента к верхнему регистру
    value_list = []  # список курсов, который не нужен вне функции

    for value in content.split("<Value>")[1:]:  # поиск значений курсов в коде страницы
        value_list.append(value.split("<")[0])

    if currency in currency_list:  # если значение аргумента в списке кодов валют:
        return (f"1 {currency}({name_list[currency_list.index(currency)]}) = "  # вернуть развернутую информацию по нему
                f"{value_list[currency_list.index(currency)]} рублей (Информация от {current_date})")
    else:
        return None  # иначе вернуть None


if __name__ == "__main__":  # код, который не выполняется при импорте модуля
    print(currency_rates("eur"))
    print(currency_rates("usd"))
    print(currency_rates(input("Введите валюту, курс которой хотите проверить по отношению к рублю: ")))
