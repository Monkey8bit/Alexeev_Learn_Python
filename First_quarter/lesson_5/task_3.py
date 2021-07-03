# Вариант 1:
import itertools  # импорт модуля для использования zip_longest


def tut_klass_gen(tutor, klass):  # функция для генерации объектов вида tuple
    for el in itertools.zip_longest(tutor, klass):
        yield el  # через yield возвращает каждую отдельную итерацию цикла


tutors = ["Иван", "Дмитрий", "Петр", "Сергей", "Дмитрий", "Борис", "Елена", "Дима", "Павел"]
klasses = ["9А", "7В", "9Б", "9В", "8Б", "10А", "10Б", "9А"]

tut_klass = tut_klass_gen(tutors, klasses)
print(type(tut_klass))  # проверка, что задача выполнена с помощью генератора
print(next(tut_klass))
print(next(tut_klass))
print(next(tut_klass))

# Вариант 2:
result = (el for el in itertools.zip_longest(tutors, klasses))  # генератор в одну строку
print(type(result))  # проверка, является ли объект генератором
print(*result)  # вывод распакованного генератора




