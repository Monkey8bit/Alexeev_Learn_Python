import re

RE_PARSE = re.compile(r'(?P<remote_addr>.+\b)\s.+\[(?P<request_datetime>.+)]\s"'
                      r'(?P<request_type>\w+)\s(?P<requested_source>[^"]+)"\s(?P<response_code>\d+)\s'
                      r'(?P<response_size>\d+)\s')
# паттерн, измененный в соответствии с вариациями логов

i = 0  # счетчик, через который выявил, что стандартный паттерн не подходит под все строки в файле
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for log in f:  # итерация по строкам в файле
        parse_dict = RE_PARSE.finditer(log)
        i += 1
        print(i)  # вывод номера каждой строки в файле
        if not re.match(RE_PARSE, log):
            raise ValueError
        for parse in parse_dict:
            print(parse.groupdict())
