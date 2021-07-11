import requests

response = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
content = response.content.decode(encoding=response.encoding)
with open("nginx_logs.txt", "w", encoding="utf-8") as f:
    f.write(content)  # копирование и запись в файл информации из удаленного источника

logs = []  # список с информацие о запросах

with open("nginx_logs.txt", "r", encoding="utf-8") as f:  # открытие файла с информацией
    for row in f:  # проход по каждой строке для экономии ОЗУ
        remote_adr = row.split("-")[0].replace(" ", "")  # получение информации о IP,
        request = row.split('"')[1]
        request_type = request.split(" ")[0]  # типу запроса,
        requested_resource = request.split(" ")[1]  # и запрашиваемых данных
        logs.append((remote_adr, request_type, requested_resource))
        # запись информации, объединенной в кортеж, в список

# выявление спамера:
response_dict = {}  # объявение пустого словаря
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for row in f:
        response_adr = row.split("-")[0].replace(" ", "")
        if response_adr in response_dict:  # проверка количества запросов для каждого адреса
            response_dict[response_adr] += 1
        else:
            response_dict[response_adr] = 1


sorted_values = sorted(response_dict.values())  # список с отсортированными значениями ключей
sorted_responses = {}
for i in sorted_values:
    for k in response_dict.keys():
        if response_dict[k] == i:
            sorted_responses[k] = response_dict[k]
            break

# print(sorted_responses)
print(f"IP с самым большим количеством запросов - {list(sorted_responses)[-1]}"
      f"({sorted_values[-1]} запросов)")  # вывод на экран информации о спамере
