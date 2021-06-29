def thesaurus(*args):  # функция для создания словаря, принимающая неограниченное количество аргументов
    names = {}  # создание пустого словаря
    for name in args:  # проход по значениям аргументов
        value = str(name).capitalize()  # приведение строки к заголовку для красоты вывода
        key = value[0]  # определение ключа
        names.setdefault(key, []).append(value)  # определение значения для ключа
    sorted_names = {}  # создание словаря для сортированных значение
    for k in sorted(names.keys()):  # проход по ключам словаря
        sorted_names.setdefault(k, []).append(names[k])  # запись ключей и значений в сортированный словарь
    return sorted_names  # Возвращение сортированного словаря


def thesaurus_adv(*args):
    names = {}  # создание пустого словаря
    for name in args:  # проход по аргументам
        name_s = str(name).split()  # разделение на имя и фамилию
        first_key = name_s[1][0].capitalize()  # определение первого ключа
        second_key = name_s[0][0].capitalize()  # определение ключа для вложенного словаря
        full_name = name_s[0].capitalize() + " " + name_s[1].capitalize()  # получение строки типа 'имя фамилия'
        names.setdefault(first_key, {}).setdefault(second_key, []).extend(["".join(full_name)])  # запись ключей
    return names                                                                              # и их значений в словарь


print(thesaurus("дима", "максим", "мария", "Даниил", "паша"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
