class DateError(Exception):  # создание исключения
    pass


class Date:  # создание класса
    def __init__(self, date):
        self.date = date
        Date.validate(date)  # валидация при создании

    @classmethod
    def extract(cls, date):
        date = date.split("-")
        return {"day": date[0], "month": date[1], "year": date[2]}  # возвращение словаря для удобства доступа к данным

    @staticmethod
    def validate(date):
        date = date.split("-")
        try:
            if int(date[0]) > 31:  # проверка дня на валидность
                raise DateError(f"Wrong day {date[0]}. Must be no more than 31")
            if int(date[1]) > 12:  # проверка месяца на валидность
                raise DateError(f"Wrong month {date[1]}. Must be no more than 12.")
        except DateError as r:
            print(r)
            # в случае, если проверка не пройдена - вызвать исключение

    def __str__(self):
        return f"Date: {self.date}"


d = Date("25-06-1994")  # проверка класса и методов
print(d)
# print(Date.extract(d.date))
# date_1 = Date.extract(d.date)
# print(date_1)
d2 = Date("33-05-1997")
