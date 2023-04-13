# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

p1 = 1, 4
p2 = 164, 5
p3 = 11, 9


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p2, *p3)
    return a + b > c and a + c > b and b + c > a


if can_triangle(p1, p2, p3):
    ab = distance(*p1, *p2)
    bc = distance(*p2, *p3)
    ac = distance(*p1, *p3)
    min_segment = min(ab, bc, ac)

    if ab == min_segment:
        print("Самый короткий отрезок: AB")
    elif bc == min_segment:
        print("Самый короткий отрезок: BC")
    else:
        print("Самый короткий отрезок: AC")
else:
    print("Треугольник не существует !")
