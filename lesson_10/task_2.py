from abc import abstractmethod


class Clothes:  # создание основного класса
    @abstractmethod  # определение абстрактного метода
    def calc_cloth(self):
        pass


class Coat(Clothes):  # дочерний класс Пальто
    def __init__(self, v):  # инициализатор, принимающий размер пальто аргументом
        self.v = v

    @property
    def calc_cloth(self):  # переопределение абстрактного метода
        return round(self.v / 6.5 + 0.5)


class Suit(Clothes):  # дочерний класс Костюм
    def __init__(self, h):  # инициализатор, принимающий рост аргументом
        self.h = h

    @property
    def calc_cloth(self):
        return round(2 * self.h + 0.3)


coat = Coat(20)

suit = Suit(30)

print(coat.calc_cloth)  # проверка методов классов
print(suit.calc_cloth)
