import json

u_list = []  # список пользователей
h_list = []  # список хобби
with open("users.csv", "r+", encoding="utf-8") as users, open("hobby.csv", "r+", encoding="utf-8") as hobbies:
    if sum(1 for _ in users) < sum(1 for _ in hobbies):  # если пользователей меньше, чем хобби - выход с кодом 1
        exit(1)
    users.seek(0), hobbies.seek(0)  # возврат к началу файлов
    for u in users:  # читаем файл построчно для экономии ОЗУ
        user = u.split(",")  # разделение ФИО на отдельные составляющие
        user[-1] = user[-1].rstrip()  # обрезка символов-переносов строк
        u_list.append(" ".join(user))  # приведение к красивому виду
    for h in hobbies:  # то же самое для хобби
        hobby = h.split(",")
        hobby[-1] = hobby[-1].rstrip()
        h_list.append(", ".join(hobby))

# генератор словаря
info = {u_list[idx]: h_list[idx] if len(h_list) > idx else None for idx in range(len(u_list))}

for k, v in info.items():
    print(f"{k}: {v}")


dict_u = []
dict_h = []
with open("users.csv", "r", encoding="utf-8") as users, open("hobby.csv", "r", encoding="utf-8") as hobbies:
    # чтение файла построчно, разделение на имя, фамилию, и отчество
    for u in users:
        temp_dict = {}  # запись элементов ведется в словарь для доступа по ключу
        temp_dict.setdefault("Фамилия", u.split(",")[0])
        temp_dict.setdefault("Имя", u.split(",")[1])
        temp_dict.setdefault("Отчество", u.split(",")[2].rstrip())
        dict_u.append(temp_dict)
    for h in hobbies:
        temp_dict = {}
        hobby = h.split(",")
        temp_dict.setdefault("Хобби", ", ".join(hobby).rstrip())
        dict_h.append(temp_dict)


info_list = []  # пустой список для записей словарей с пользователями и хобби
for el in range(len(dict_u)):  # итерация по длине списка словарей с пользователями
    if el >= len(dict_h):  # если элемент цикла больше, чем длина списка словарей с хобби
        dict_u[el].update({"Хобби": None})  # добавление к словарю с пользователем ключа Хобби со значением None
        info_list.append(dict_u[el])
    else:
        dict_u[el].update(dict_h[el])  # добавление к словарю с пользователем ключа Хобби
        info_list.append(dict_u[el])  # со значением из списка словарей с хобби

with open("bio.csv", "w", encoding="utf-8") as f:
    j_list = json.dumps(info_list, indent=1, ensure_ascii=False)  # преобразование словаря в json объект
    f.write(j_list)  # запись json объекта в файл

with open("bio.csv", "r", encoding="utf-8") as j:
    j_list = json.load(j)  # проверка словаря, загруженного из файла

print(j_list)
