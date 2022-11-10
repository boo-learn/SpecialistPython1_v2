# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    pass


# TODO: your code here
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.


def dist(x1, y1, x2, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d


def long(*args):
    min_long = min(ab, bc, ac)
    return min_long


point1_x1 = int(input("x1 "))
point1_y1 = int(input("y1 "))
point2_x2 = int(input("x2 "))
point2_y2 = int(input("y2 "))
point3_x3 = int(input("x3 "))
point3_y3 = int(input("y3 "))

ab = dist(point1_x1, point1_y1, point2_x2, point2_y2)
bc = dist(point2_x2, point2_y2, point3_x3, point3_y3)
ac = dist(point3_x3, point3_y3, point1_x1, point1_y1)

if ab == long():
    print("ab минимальный")

elif bc == long():
    print("bc минимальный")
else:
    print("ac минимальный")
