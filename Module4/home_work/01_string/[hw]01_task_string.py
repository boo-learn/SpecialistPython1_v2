text = input("Введите текст для проверки: ")

point_count = text.count('.')
comma_point = text.count(',')

if point_count > comma_point:
    print("Точек больше")
elif comma_point > point_count:
    print("Запятых больше")
else:
    print("Одинаково")
