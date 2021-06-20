duration = int(input("Пожалуйста, введите время в секундах: "))

# 1a:
if duration < 60:
    print(f"Время: {duration} сек")
# 1b:
elif 60 <= duration < 3600:
    minutes = duration // 60
    seconds = duration - minutes * 60
    print(f"{minutes} мин {seconds} сек")
# 1c:
elif 3600 <= duration < 86400:
    minutes = duration // 60
    hours = minutes // 60
    minutes -= hours * 60
    seconds = duration - (hours * 3600 + minutes * 60)
    print(f"{hours} час {minutes} мин {seconds} сек")
# 1d, задание под *:
else:
    minutes = duration // 60
    hours = minutes // 60
    minutes -= hours * 60
    days = hours // 24
    hours -= days * 24
    seconds = duration - (days * 86400 + hours * 3600 + minutes * 60)
    print(f"{days} дн {hours} час {minutes} мин {seconds} сек")

