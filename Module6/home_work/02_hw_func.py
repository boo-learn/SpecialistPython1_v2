# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return length


def min_line(xa, ya, xb, yb, xc, yc):
    ab = distance(xa, ya, xb, yb)
    bc = distance(xb, yb, xc, yc)
    ac = distance(xa, ya, xc, yc)
    if ab > ac and bc > ac:
        print("Самый короткий отрезок:", end='')
        return "AC"
    elif ac > bc and ab > bc:
        print("Самый короткий отрезок:", end='')
        return "BC"
    elif ac > ab and bc > ab:
        print("Самый короткий отрезок:", end='')
        return "AB"


print(min_line(13, 18, 2, -9, 17, 8))
print(min_line(2, 4, 2, 9, 13, 4))
print(min_line(12, 8, 12, -9, 5, -1))
print(min_line(23, 20, 15, 2, 31, -1))
print(min_line(12, 8, 5, 9, 12, -9))
print(min_line(15, 32, 3, 1, 23, 0, ))
print(min_line(12, 8, 5, 9, 12, -9))
