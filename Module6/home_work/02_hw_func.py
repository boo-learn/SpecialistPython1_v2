# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


#points = ((10, 12), (14, 18), (12, 12))
#points = ((1, 1), (2, 2), (3, 3))
points = ((-1, -1), (2, 2), (3, 3))
#points = ((1, 9), (1, 1), (1, 1))
L_AB = distance(*points[0], *points[1])
L_BC = distance(*points[1], *points[2])
L_AC = distance(*points[0], *points[2])

side = [(L_AB, 'AB'), (L_BC, 'BC'), (L_AC, 'AC')]
print(side)
min_side = side[0]
for el in side:
    if el[0] < min_side[0]:
        min_side = el
print(f"Самый короткий отрезок {min_side[1]} длиной {min_side[0]:.2f}", )  # Выводим название отрезка, например “АС”.

