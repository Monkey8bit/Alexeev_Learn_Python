from random import random


class Cell:  # создания класса Клетка
    def __init__(self, c):
        self.c = c  # инициализатор с аргументом-количеством ячеек

    def __add__(self, other):
        return Cell(self.c + other.c)  # сложение двух экземпляров класса, возвращает новый экземпляр

    def __sub__(self, other):  # вычитание одной клетки из другой
        if self.c - other.c > 0:
            return Cell(self.c + other.c)
        else:
            print("Cell count must be higher than 0.")

    def __mul__(self, other):  # умножение одной клетки на другую
        return Cell(self.c * other.c)

    def __floordiv__(self, other):  # деление одной клетки на другую
        return Cell(self.c // other.c)

    def make_order(self, count):
        row = ""  # временная пусткая строка
        for cell in range(self.c):
            if cell % count == 0 and len(row) > 0:  # если количество клеток не делится на заданную длину ряда
                row += "\n*"
            else:
                row += "*"
        return row


c1 = Cell(round(random() * 100))  # создание клеток со случайным количеством ячеек
c2 = Cell(round(random() * 100))
c3 = Cell(round(random() * 100))
print(c1.c, c2.c, c3.c)
c4 = c1 + c2  # проверка перегруженных методов
c5 = c2 * c3
c6 = c3 // c4
c7 = c3 - c2
print(c1.make_order(3))
print(c2.make_order(5))
print(c3.make_order(7))
print(c4.make_order(2))  # проверка метода, который выстраивает ячейки в ряды
print(c5.make_order(4))
print(c6.make_order(6))
try:
    print(c7.make_order(7))
except AttributeError:
    print("c7 is not exists.")
