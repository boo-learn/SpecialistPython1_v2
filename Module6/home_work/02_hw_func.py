# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(p1: tuple, p2: tuple):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def sides(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    return [('p1p2', a), ('p2p3', b), ('p3p1', c)]


p1 = (0, 0)
p2 = (0, 4)
p3 = (3, 0)

triangle = sides(p1, p2, p3)
minside = triangle[0]

for side in triangle:
    if side[1] < minside[1]:
        minside = side

print(f"Сторона {minside[0]} - наименьшая и равна {minside[1]}")
