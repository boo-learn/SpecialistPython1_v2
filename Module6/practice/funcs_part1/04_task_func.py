# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверяЮщую можно ли построить треугольник, соединив данные точки отрезками
def distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d


# print(distance(2,5,3,9))
def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p2, *p3)
    c = distance(*p1, *p3)

    return b + c > a and a + c > b and b + a > c


# Пример вызова функции
print(can_triangle((10, 10), (14, 18), (10, 12)))

# Не забудьте протестировать вашу функцию
