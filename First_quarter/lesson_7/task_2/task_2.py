import os

ROOT = "./my_project"  # название проекта
my_project = {"settings":  # словарь со схемой ветвления проекта
              ["__init__.py", "dev.py", "prod.py"],
              "mainapp":
                  ["__init__.py", "models.py", "views.py", {"templates":

                                                            {"mainapp": ["base.html", "index.html"]}}],
              "authapp":
                  ["__init__.py", "models.py", "views.py", {"templates":
                                                            {"authapp":
                                                             ["base.html", "index.html"]}}]}


def create_tree(dirs, current_dir=ROOT):  # функция, создающая стартер из словаря
    for dir_name, sub_dir in dirs.items():
        try:
            os.mkdir(os.path.join(current_dir, dir_name))
        except FileExistsError:
            print(f"Папка {dir_name} уже существует")
        if isinstance(sub_dir, list):  # если значение ключа словаря - список
            for file in sub_dir:  # проход по списку
                if isinstance(file, dict):  # если элемент списка - словарь
                    create_tree(file, os.path.join(current_dir, dir_name))  # рекурсия с новыми атрибутами
                else:  # если это файл
                    if os.path.isfile(os.path.join(current_dir, dir_name, file)):
                        print(f"Файл {file} уже сущестует")  # вывести предупреждение, если файл уже существует
                    else:
                        f = open(os.path.join(current_dir, dir_name, file), "w")  # иначе создать файл
                        f.close()
        if isinstance(sub_dir, dict):  # если значение ключа словаря - словарь
            create_tree(sub_dir, os.path.join(current_dir, dir_name))  # начать рекурсивную функцию
        if isinstance(sub_dir, str):  # если значение ключа словаря - строка
            if os.path.isfile(os.path.join(current_dir, dir_name, sub_dir)):
                print(f"Файл {sub_dir} уже существует")  # проверка на существование и создание файла
            f = open(os.path.join(current_dir, dir_name, sub_dir), "w")
            f.close()


try:
    os.makedirs(ROOT)
    create_tree(my_project)
except FileExistsError:
    print(f"Проект {ROOT} уже существует")  # прервать функцию в случае существования папки с проектом

