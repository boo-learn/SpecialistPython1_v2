# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return length


def min_len(a, b, c):
    dist_ab = distance(*a, *b)
    dist_bc = distance(*b, *c)
    dist_ac = distance(*a, *c)
        if dist_ab < dist_bc < dist_ac:
        return "AB "
    elif dist_ac < dist_ab < dist_bc :
        return "AC "
    else:
        return "BC "

    
min_length = min_len((2, 15), (5, 2), (5, 15))
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
