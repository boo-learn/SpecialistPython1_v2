# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def distance(x1, y1, x2, y2):
    l = ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 0.5
    return l


def can_triangle(p1, p2, p3):
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p1[0], p1[1], p3[0], p3[1])
    c = distance(p3[0], p3[1], p2[0], p2[1])
    if a + b > c and a + c > b and c + b > a:
        return print("Можно")
    return print("Нельзя")
# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
