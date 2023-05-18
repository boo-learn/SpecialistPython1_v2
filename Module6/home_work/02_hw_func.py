# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def min_len_line(p1, p2, p3):
    ab = distance(*p1, *p2)
    ac = distance(*p1, *p3)
    bc = distance(*p2, *p3)
    if ab < ac and ab < bc:
        return "AB"
    if ac < ab and ac < bc:
        return "AC"
    return "BC"


result = min_len_line((10, 12), (14, 8), (12, 12))
print(f"Самый короткий отрезок: {result}") 

