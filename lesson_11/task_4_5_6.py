from random import choice


class OfficeStorage:  # создание класса-склада
    eq_amount = 0  # количество единиц техники на складе
    tech_type_count = {}  # словарь, который показывает подробное информацию о продуктах

    @staticmethod
    def info():  # метод, возвращающий информацию о технике на складе
        return f"Amount of equipment in storage: {OfficeStorage.eq_amount}\n" \
         f"Equipment include: {OfficeStorage.tech_type_count}\n"


class OfficeEquipment:  # родительский класс всей техники
    def __init__(self, cost, name):
        self.name = name
        self.cost = cost
        OfficeStorage.eq_amount += 1  # при создании экземплра класса на Складе прибавляется единица


class Notebook(OfficeEquipment):  # дочерний класс Ноутбук
    def __init__(self, cost, name, screen_size, model):
        super().__init__(cost, name)
        self.screen_size = screen_size
        self.model = model
        # приведение названия экземпляра техники к красивому виду
        self.equipment = (self.name + " " + self.model + " " + self.screen_size + " " + self.cost)
        # добавление описания экземпляра на Склад
        OfficeStorage.tech_type_count.setdefault(self.__class__.__name__ + "s", []).append(self.equipment)

    def __str__(self):  # перегрузка метода для выведения информации о продукте
        return f"Notebook\n" \
               f"Name: {self.name}\n" \
               f"Model: {self.model}\n" \
               f"Screen size: {self.screen_size}'\n" \
               f"Cost: {self.cost}\n"


class Printer(OfficeEquipment):  # дочерний класс Принтер
    def __init__(self, cost, name, print_speed, model):
        super().__init__(cost, name)
        self.print_speed = print_speed
        self.model = model
        self.equipment = (self.name + " " + self.model + " " + self.print_speed + " " + self.cost)
        OfficeStorage.tech_type_count.setdefault(self.__class__.__name__ + "s", []).append(self.equipment)

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Model: {self.model}\n" \
               f"Print speed: {self.print_speed}\n" \
               f"Cost: {self.cost}\n"


class Basket:  # класс Корзина для покупок
    basket = []  # список с покупками

    @classmethod  # метод, добавляющий продукт в Корзину
    def add_product(cls, *args):
        for product in args:
            cls.basket.append(product)

    @staticmethod  # метод, выводящий информацию о продукте
    def info():
        total_cost = 0
        print(f"Basket includes {OfficeStorage.eq_amount} items:")
        for product in Basket.basket:
            print(product.equipment)
            total_cost += int(product.cost)
        print(f"Total cost: {total_cost}\n")


random_printer = [["Canon", "Brother", "HP", "Kyocera"],  # списки с абстрактными видами принтеров и ноутбуков
                  ["5000", "6500", "8600", "10200", "16700", "21300"],
                  ["10 p/min", "20 p/min", "30 p/min", "40 p/min"],
                  ["Pixma G2411", "Deskjet 2320", "LaserJet Pro", "Phaser 3052"]]

random_notebook = [["Acer", "Lenovo", "ASUS", "MSI"],
                   ["56300", "66000", "78300", "55800", "50234"],
                   ["15'", "16'", "17'", "18'", "19'", "20'"],
                   ["Nitro-5", "IdeaPad 3", "GF63", "GL65", "Aspire 3", "XPS 15"]]

e1 = Printer("19000", "Canon", "20 p/min", "LP600")  # создание экземпляров вручную
e2 = Printer("20000", "Canon", "30 p/min", "PixmaG2411")
print(e1.print_speed)  # проверка атрибутов экземпляра
e3 = Notebook("50000", "Acer", "19'", "Nitro-5")
print(OfficeStorage.info())  # выведение информации о Складе
print(e2)  # вывыедение информации о продукте
print(e1)
e4 = Notebook(choice(random_notebook[1]), choice(random_notebook[0]),  # создание случайного экземпляра
              choice(random_notebook[2]), choice(random_notebook[3]))
print(e4)
print(OfficeStorage.info())
Basket.add_product(e4, e3, e1)  # добавление продуктов в Корзину
Basket.info()  # выведение информации о продуктах в корзине
e5 = Printer(choice(random_printer[1]), choice(random_printer[0]),
             choice(random_printer[2]), choice(random_printer[3]))
print(e5)
