class Complex:  # создание класска комплекных чисел
    def __init__(self, number):
        self.number = number

    def __str__(self):  # перегрузка метода для выведения корректной информации о экземпляре
        return self.number

    def __add__(self, other):  # перегрузка метода сложения двух комплексных чисел
        c1 = int(self.number.split(" + ")[0])
        c2 = int(self.number.split(" + ")[1].split("i")[0])
        c3 = int(other.number.split(" + ")[0])
        c4 = int(other.number.split(" + ")[1].split("i")[0])
        temp_complex = (str(c1 + c3) + " + " + str(c2 + c4) + "i")
        return Complex(temp_complex)  # вернуть новый экземпляр класса

    def __mul__(self, other):  # перегрузка метода умножения двух компексных чисел
        c1 = int(self.number.split(" + ")[0])
        c2 = int(self.number.split(" + ")[1].split("i")[0])
        c3 = int(other.number.split(" + ")[0])
        c4 = int(other.number.split(" + ")[1].split("i")[0])
        temp_complex = str(str((c1 * c3 - c2 * c4)) + " + " + str(c1 * c4 + c2 * c3) + "i")
        return Complex(temp_complex)


n1 = Complex("2 + 3i")  # создание экземпляров класса
n2 = Complex("4 + 7i")
print(n1)  # выведение экземпляров на экран
print(n2)
n3 = n1 + n2  # проверка метода сложения
print(n3)
n4 = n3 + n2
print(n4)
n5 = n1 * n2  # проверка метода умножения
print(n5)
n6 = Complex("2 + 5i")
n7 = n6 + n1
print(n7)
