# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def find_short(AB, AC, BC):
    l1 = distance(*AB, *AC)
    l2 = distance(*AB, *BC)
    l3 = distance(*BC, *AC)
    distances = [l1, l2, l3]
    short = min(distances)
    print(f"Самый короткий отрезок: {short}")


find_short((0, 7), (0, 0), (2, 0))
