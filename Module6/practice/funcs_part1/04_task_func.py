# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def distance(p1: tuple, p2: tuple):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    print(type(p1))
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    return a < b + c and b < a + c and c < a + b


# Пример вызова функции
print(can_triangle((4, 0), (0, 3), (0, 0)))


# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
