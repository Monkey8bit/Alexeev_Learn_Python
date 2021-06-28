main_list = ["в", "5", "часов", "17", "минут", "температура", "была", "+5", "градусов"]
new_list = []  # создание нового списка, т.к. не решил задачу in place
for el in main_list:
    if "+" in el:  # проверка на наличие символа в элементе списка
        temp = list(el).pop(el.index("+"))  # временная переменная для символа, т.к. при
        number = f'{int(el):02}'  # форматировании символ удаляется
        new_list.append("'")  # обособление числа кавычками
        new_list.append(temp + number)  # возвращение символа в элемент
        new_list.append("'")
    elif not el.isdigit():  # если элемент списка - не число - записать его в новый список без преобразования
        new_list.append(el)
    if el.isdigit():  # если элемент списка - число -
        new_list.append("'")  # обособить его кавычками,
        number = f'{int(el):02}'  # форматировать,
        new_list.append(number)  # и записать в новый список
        new_list.append("'")


print(new_list)
result = " ".join(new_list)
print(result)
