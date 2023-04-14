# Исправлено название переменной sides на month_year
while True:
    month_year = input("Введите номер месяца и год: ")
    try:
        month = int(month_year.split(" ")[0])
        year = int(month_year.split(" ")[1])
        break
    except ValueError:
        print("Некорректные параметры")

if month == 2:
    if year % 4 == 0:
        total_days = 29
    else:
        total_days = 28
elif month in [1, 3, 5, 7, 8, 10, 12]:
    total_days = 31
else:
    total_days = 30

print(f"В данном месяце {total_days} дней")
