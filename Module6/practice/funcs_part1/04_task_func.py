# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    # TODO: your code here
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
        return True
    else:
        return False


def distance(x1, y1, x2, y2):
    # TODO: your code here
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))

# Не забудьте протестировать вашу функцию
