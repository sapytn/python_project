duration = int(input("Введите количество секунд:"))

sec = duration % 60
minutes = duration % 3600 // 60
hours = duration % 86400 // 3600
days = duration // 86400

if duration < 60:
    print(f"{sec} секунд")
elif duration < 3600:
    print(f"{minutes} минут и {sec} секунд")
elif duration < 86400:
    print(f"{hours} часов {minutes} минут и {sec} секунд")
else:
    print(f"{days} дней {hours} часов {minutes} минут и {sec} секунд")

