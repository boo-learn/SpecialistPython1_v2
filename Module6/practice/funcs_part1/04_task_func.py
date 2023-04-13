# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками


def distance(x1, y1, x2, y2):
    d = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    return d
def can_triangle(p1, p2, p3):
    a = distance(p1[0], p2[0], p1[1], p2[1])
    b = distance(p1[0], p3[0], p1[1], p3[1])
    c = distance(p2[0], p3[0], p2[1], p3[1])
    return a + b > c and a + c > b and b + c > a

# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))
