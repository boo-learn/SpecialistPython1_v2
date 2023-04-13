# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def get_min_side_name(ab, ac, bc):
    print(locals())
    if ab <= ac and ab <= bc:
        return "AB"
    elif ac <= ab and ac <= bc:
        return "AC"
    else:
        return "BC"


a = (1, 1)
b = (1, 2)
c = (6, 11)

print("Самый короткий отрезок:", get_min_side_name(dist(*a, *b), dist(*a, *c), dist(*b, *c)))
