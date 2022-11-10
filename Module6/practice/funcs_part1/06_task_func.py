# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:
point_x = int(input("Введите координату x точки: "))
point_y = int(input("Введите координату y точки: "))
circle_x = int(input("Введите координату x центра окружности: "))
circle_y = int(input("Введите координату y центра окружности: "))
circle_r = int(input("Введите радиус окружности: "))


def point_in_circle(x, y, xc, yc, r):
    distance = ((x - y) ** 2 + (yc - xc) ** 2) ** 0.5
    if distance <= r:
        print("Точка принадлежит кругу")
    else:
        print("Точка не принадлежит кругу")


point_in_circle(point_x, point_y, circle_x, circle_y, circle_r)

# Не забудьте протестировать вашу функцию
