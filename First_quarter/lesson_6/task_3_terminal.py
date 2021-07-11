import sys
import json
import os


def make_dir(d):  # функция для создания новой папки под результат функции bio_gen
    os.mkdir(d)


def bio_gen(user, hobby, bio):
    with open(user, "r", encoding="utf-8") as users, open(hobby, "r", encoding="utf-8") as hobbies, \
         open(bio, "w", encoding="utf-8") as result:
        dict_u = []
        dict_h = []
        info_list = []
        for u in users:
            temp_dict = {}
            temp_dict.setdefault("Фамилия", u.split(",")[0])
            temp_dict.setdefault("Имя", u.split(",")[1])
            temp_dict.setdefault("Отчество", u.split(",")[2].rstrip())
            dict_u.append(temp_dict)
        for h in hobbies:
            temp_dict = {}
            hobby = h.split(",")
            temp_dict.setdefault("Хобби", ", ".join(hobby).rstrip())
            dict_h.append(temp_dict)
        for el in range(len(dict_u)):
            if el >= len(dict_h):
                dict_u[el].update({"Хобби": None})
                info_list.append(dict_u[el])
            else:
                dict_u[el].update(dict_h[el])
                info_list.append(dict_u[el])
        j_list = json.dumps(info_list, indent=1, ensure_ascii=False)
        result.write(j_list)


try:
    command = sys.argv[1]
    if command == "make_bio":
        bio_gen(sys.argv[2], sys.argv[3], sys.argv[4])
    if command == "make_dir":
        make_dir(sys.argv[2])
except IndexError:
    print("Файлы могут находиться в разных папках, введите путь к ним в формате, соответствующем вашей ОС.")
    print("Введите путь к файлам в формате make_bio 'пользователи, хобби, файл записи'")
    print("Если вы хотите создать папку для нового файла, введите make_dir 'новая папка'")

bio_gen("users/users.csv", "hobby/hobby.csv", "result/bio.csv")  # проверка для случая, когда файлы в разных папках
