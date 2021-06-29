#  выполнение усложненного задания

numbers = {  # создание словаря с переводом чисел
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять"
}


def num_translate_adv(number):
    if number.istitle():  # проверка, есть ли у введенного числа заглавная буква
        number = number.lower()  # приведение строки к нижнему регистру, иначе функция вернет None
        return numbers.get(number).capitalize()  # возвращение значения с заглавное буквой
    else:
        return numbers.get(number)  # иначе возврат стандартного значения ключа


user_number = input("Напишите число от 1 до 9 на английском, чтобы получить перевод: ")  # небольшая вариация задания,
print(num_translate_adv(user_number))  # надеюсь, мне не снизят за это балл

