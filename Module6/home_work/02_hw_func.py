# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def min_distance(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p2, *p3)
    c = distance(*p1, *p3)
    #print(f"a={a} b={b} c={c}")
    # min_dst = a
    # for element in (a, b, c):
    #     if element < min_dst:
    #         min_dst = element
    # return min_dst
    # second way:
    if a <= b and a <= c:
        return f"AB has min distance: {a} (AB={a} BC={b} AC={c})"
    elif b <= a and b <= c:
        return f"BC has min distance: {b} (AB={a} BC={b} AC={c})"
    else:
        return f"AC has min distance: {c} (AB={a} BC={b} AC={c})"


# # Пример вызова функции
#print(distance(10, 12, 14, 18))
print(min_distance((10, 12), (14, 18), (12, 12)))
print(min_distance((10, 12), (10, 11), (12, 12)))
print(min_distance((10, 12), (10, 18), (12, 18)))
print(min_distance((10, 12), (8, 12), (12, 12)))

