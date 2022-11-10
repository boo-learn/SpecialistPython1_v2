# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками


def can_triangle(p1, p2, p3):
    a = (((p2[1] - p1[1]) ** 2) + ((p2[0] - p1[0]) ** 2)) ** 0.5
    b = (((p3[1] - p3[1]) ** 2) + ((p2[0] - p2[0]) ** 2)) ** 0.5
    c = (((p3[1] - p3[1]) ** 2) + ((p1[0] - p1[0]) ** 2)) ** 0.5

    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
