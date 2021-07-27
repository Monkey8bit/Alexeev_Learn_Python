class Worker:  # создание класса

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname  # инициализация атрибутов
        self.position = position
        self._income = income


class Position(Worker):  # дочерний класс

    def get_full_name(self):  # метод для вывода имени
        return f"Сотрудник: {self.name} {self.surname}"

    def get_total_income(self):  # метод для вывода дохода
        return f"Полный доход: {self._income['wage'] + self._income['bonus']}"


john = Position("John", "Doe", "Worker", {"wage": 100, "bonus": 50})
print(john.get_full_name())
print(john.get_total_income())  # проверка методов
