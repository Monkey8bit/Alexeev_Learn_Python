import re

MAIL = "kyu-obscure@mail.ru"
RE_MAIL = re.compile(r"(?P<username>[A-z0-9!#$%/+=&*'{}|~-]+)[@](?P<domain>\w+\.\w+)")
# паттерн регулярного выражения расширен для более точного определения адреса


def email_parse(email):
    mail_dict = RE_MAIL.finditer(email)  # ищем совпадения по группам
    if not re.match(RE_MAIL, MAIL):  # если совпадений в строке нету - вызываем Value Error
        raise ValueError(f"wrong mail:{MAIL}")
    return mail_dict  # возвращаем словарь с совпадениями


iter_dict = email_parse(MAIL)
for mail in iter_dict:  # итерация по словарю с совпадениями
    print(mail.groupdict())

