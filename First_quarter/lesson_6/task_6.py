import sys


def add_sales(row, value):  # функция принимает аргументами номер строки и значение, которое необходимо добавить
    with open("bakery.csv", "r+", encoding="utf-8") as f:
        row = int(row)  # приведение к числу
        i = 0  # счетчик количества строк
        for _ in f:
            i += 1
        f.seek(0)  # возвращение в начало файла
        my_sales = []  # список для временного хранения записей
        for index, line in enumerate(f):
            value = str(value).replace(".", ",")  # замена разделителя, на случай если сумма введена в неверном формате
            if row > i:  # проверка, существует ли запись в файле
                print(f"Несуществующая запись. Количество записей в файле: {i}")
                break
            elif index == row - 1:  # если номер линии равен заданному числу
                my_sales.append(value.rstrip())  # добавить заданное значение во временный список
            else:
                my_sales.append(line.rstrip())  # иначе добавить существующее значение
    if my_sales:  # если список не пуст
        with open("bakery.csv", "w", encoding="utf-8") as f:  # открываем и перезаписываем файл с новыми данными
            for sale in my_sales:
                if sale == my_sales[-1]:
                    f.write(sale)  # ветвление, чтобы исключить появление пустой строки в конце
                else:
                    f.write(f"{sale}\n")


def show_sales(row=None, end=None):  # функция с пустыми значениями по умолчанию
    with open("bakery.csv", "r", encoding="utf-8") as f:
        sales = f.readlines()  # запись строк в переменную
        if row and end:  # если значения функции введены
            if row > len(sales):  # проверка на существование записи
                print(f"Запись не существует. Количество записей в файле: {len(sales)}")
            else:  # вывод записей с row по end
                for sale in sales[row - 1:end]:
                    print(sale, end="")
        elif row:  # если только значение row не пустое
            if row > len(sales):
                print(f"Запись не существует. Количество записей в файле: {len(sales)}")
            else:
                for sale in sales[row - 1:]:
                    print(sale, end="")
        else:  # если функция вызвана без аргументов
            f.seek(0)
            print(f.read())


try:
    command = sys.argv[1]
except IndexError:
    print("Введите команду")
else:
    if command == "show_sales":
        try:
            show_sales(int(sys.argv[2]), int(sys.argv[3]))
        except IndexError:
            try:
                show_sales(int(sys.argv[2]))
            except IndexError:
                show_sales()
    elif command == "add_sale":
        try:
            add_sales(sys.argv[2], sys.argv[3])
        except IndexError:
            print("Введите номер записи и значение, на которое хотите заменить запись.")
