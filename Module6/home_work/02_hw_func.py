# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1,x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def min(p1, p2, p3):
    ab = distance(*p1, *p2)
    bc = distance(*p2, *p3)
    ac = distance(*p1, *p3)
    if (ab >= bc) and (ab >= ac):
        return "AB"
    if ( bc>= ab) and (bc >= ac):
        return "BC"
    if (ac >= ab) and (ac >= bc):
        return "AC"

print("Самый короткий отрезок:", min((5, 6), (3, 3), (4, 4) )) # Выводим название отрезка, например “АС”.
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
