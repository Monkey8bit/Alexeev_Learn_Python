import re

MAIL = "kyu-obscure@mail.ru"  # данные, взятые из задания №1
RE_MAIL = re.compile(r"(?P<username>[A-z0-9!#$%/+=&*'{}|~-]+)[@](?P<domain>\w+\.\w+)")


def val_checker(func):  # функция-декоратор
    def wrapper(arg):  # функция, принимающая лямбду в качестве аргумента
        def new_f(x):  # функция, которая принимает аргумент из внешней функции при вызове
            if func(x):  # если мэйл прошел лямбда-проверку
                return arg(x)  # вернуть результат функции
            else:
                raise ValueError(f"wrong mail: {x}")  # иначе вызвать исключение
        return new_f
    return wrapper


@val_checker(lambda x: re.match(RE_MAIL, x))  # декоратор с функцией-валидатором в качестве аргумента
def email_parse(email):
    iter_dict = RE_MAIL.finditer(email)
    return iter_dict


mail_dict = email_parse(MAIL)
for mail in mail_dict:
    print(mail.groupdict())


