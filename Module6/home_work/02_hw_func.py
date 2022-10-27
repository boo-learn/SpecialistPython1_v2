# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def line(p1, p2, p3):
    ab = distance(*p1, *p2) #распаковка
    bc = distance(*p2, *p3)
    ac = distance(*p1, *p3)
    if max(ab, bc, ac) == ab:
        return 'AB'
    if max(ab, bc, ac) == bc:
        return 'BC'
    if max(ab, bc, ac) == ac:
        return 'AC'


print("Самый короткий отрезок:", line((10, 12), (14, 18), (12, 12)))  # Выводим название отрезка, например “АС”.
