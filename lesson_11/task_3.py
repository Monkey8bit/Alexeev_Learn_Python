class NumberError(Exception):  # создание исключения
    pass


my_list = []
while True:  # цикл для запроса элементов от пользователя
    try:
        number = input("Enter a number: ")
        if number == "stop":  # если пользователь ввел stop
            print(my_list)
            break
        if number.isdigit():  # если введенный элемент - число
            number = int(number)
        elif "." in number:  # если во введенных данных есть точка
            number = float(number)
        else:  # иначе исключение
            raise NumberError(f"Invalid type of element: {type(number)}. Must be int.")
        my_list.append(number)
    except NumberError as er:
        print(er)
