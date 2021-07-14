import os


root = "./my_project"  # название папки проекта
folders = ["settings", "mainapp", "adminapp", "authapp"]  # список с подпапками
for folder in folders:
    try:
        os.makedirs(os.path.join(root, folder))  # обработка исключений в случае существования папок
    except FileExistsError as e:
        print(f"Папка {os.path.join(root, folder)} уже существует")
