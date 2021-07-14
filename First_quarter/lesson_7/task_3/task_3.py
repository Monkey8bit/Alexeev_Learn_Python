import os
import shutil

# shutil.copytree("./my_project", "my_project/templates2")
# простой вариант с помощью модуля shutil

ROOT = ".//my_project"
dst_dir = os.path.join(ROOT, input("Введите название папки, в которую хотите скопировать ваш проект: "))
for root, dirs, files in os.walk(ROOT):
    for file in files:
        f_path = os.path.join(root, file)  # пусть к файлу в цикле
        r = root.split("\\")[1:]  # разбитие пути к папке с файлом на составляющие, отбрасывая имя корневой папки
        r = "/".join(r)  # соединение пути в строку
        copy_path = os.path.join(dst_dir, r)
        if not os.path.exists(copy_path):
            os.makedirs(copy_path)
        shutil.copy(f_path, os.path.join(copy_path, file))