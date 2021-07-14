import json
import os

d_stat = {100: 0, 1000: 0, 10000: 0, 100000: 0}  # заготовка для словаря со статистикой

ROOT = "./my_project"
quantity_100 = [0, []]
quantity_1000 = [0, []]  # списки для значений и расширений в зависимости от размера файла
quantity_10000 = [0, []]
quantity_100000 = [0, []]

for dirs, sub_dirs, files in os.walk(ROOT):
    for f in files:
        f_ext = os.path.splitext(os.path.join(dirs, f))[1]  # определение расширения файла
        f_size = os.stat(os.path.join(dirs, f)).st_size  # путь файла
        if f_size <= 100:  # если размер файла > или = 100
            quantity_100[0] += 1
            if f_ext not in quantity_100[1]:  # если расширения нету в списке расширений
                quantity_100[1].append(f_ext)
        elif 100 > f_size <= 1000:
            quantity_1000[0] += 1
            if f_ext not in quantity_1000[1]:
                quantity_1000[1].append(f_ext)
        elif 1000 > f_size <= 10000:
            quantity_10000[0] += 1
            if f_ext not in quantity_10000[1]:
                quantity_10000[1].append(f_ext)
        elif 10000 < f_size <= 100000:
            quantity_100000[0] += 1
            if f_ext not in quantity_100000[1]:
                quantity_100000[1].append(f_ext)

d_stat[100] = tuple(quantity_100)  # преобразование в кортеж и определение для ключа словаря
d_stat[1000] = tuple(quantity_1000)
d_stat[10000] = tuple(quantity_10000)
d_stat[100000] = tuple(quantity_10000)
print(d_stat)

with open("./my_project_summary.json", "w", encoding="utf-8") as j:
    json.dump(d_stat, j)