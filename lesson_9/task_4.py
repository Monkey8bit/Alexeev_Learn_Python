class Car:  # создание родительского класса
    def __init__(self, speed, color, name, is_police=False):  # инициализация атрибутов
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"Car speed: {self.speed} Km/h"

    def go(self):
        return f"{self.color} {self.name} starts with speed {self.speed} Km/h"

    def stop(self):
        return f"{self.color} {self.name} stops"

    def turn(self, direction):
        if direction == "right":
            return f"{self.color} {self.name} turns {direction}"
        elif direction == "left":
            return f"{self.color} {self.name} turns {direction}"
        else:
            return "Wrong direction."


class TownCar(Car):  # дочерний класс
    def show_speed(self):
        if self.speed > 60:  # вывод предупреждения, если превышена скорость
            return f"Caution: High speed {self.speed} Km/h, please slow down."
        else:
            return f"Car speed: {self.speed} Km/h"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Caution: High speed {self.speed} Km/h, please slow down."
        else:
            return f"Car speed: {self.speed} Km/h"


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = True


# проверка каждого типа класса
a = TownCar(70, "Black", "Mazda")
print(a.show_speed())
print(a.turn("right"))
print(a.turn("left"))
b = PoliceCar(50, "White", "Lada", True)
print(b.turn("left"))
print(b.show_speed())
print(b.is_police)
c = WorkCar(50, "Red", "Lada")
print(c.turn("right"))
print(c.show_speed())
print(c.is_police)
d = SportCar(90, "Blue", "Kia")
print(d.turn("left"))
print(d.show_speed())
print(d.is_police)



