class Stationery:  # создание класса-родителя
    title = "Chancellery"

    def draw(self):
        return "Start drawing.."


class Pen(Stationery):
    def draw(self):
        return "Start drawing with pen.."


class Pencil(Stationery):
    def draw(self):
        return "Start drawing with pencil.."


class Handle(Stationery):
    def draw(self):
        return "Start drawing with handle.."


# проверка всех классов
stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())