# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
   res = (x1-x2)**2+(y1-y2)**2
   return (res**0.5)

def min3(n1, n2, n3):
    n_min = n1
    if n_min > n2:
        n_min = n2
    if n_min > n3:
        n_min = n3
    return n_min


def distance2(p1, p2, p3):
    sizeAB = distance(*p1, *p2)
    sizeAC = distance(*p1, *p3)
    sizeBC = distance(*p2, *p3)
    return min3(sizeAB, sizeBC, sizeAC)


res = distance2((10, 11), (5, 4), (12, 9))
print("Самый короткий отрезок:",res)

print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
