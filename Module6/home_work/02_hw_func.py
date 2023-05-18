# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def get_min_line(*args: tuple) -> str:
    min_distance = distance(*args[0], *args[1])
    min_line = f"{args[0]} - {args[1]}"
    for arg1 in args:
        for arg2 in args:
            if arg2 != arg1:
                if distance(*arg1, *arg2) < min_distance:
                    min_distance = distance(*arg1, *arg2)
                    min_line = f"{arg1} - {arg2}"
    return min_line


p1 = (1, 1)
p2 = (1, 6)
p3 = (1, 3)
print("Самый короткий отрезок:", get_min_line(p1, p2, p3))
