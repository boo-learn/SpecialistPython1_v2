# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2) + ((y2 - y1) ** 2) ** 0.5


# TODO: your code here
def distance(xa, ya, xb, yb, xc, yc):
    AB = ((xb - xa) ** 2) + ((yb - ya) ** 2) ** 0.5
    BC = ((xc - xb) ** 2) + ((yc - yb) ** 2) ** 0.5
    AC = ((xc - xa) ** 2) + ((yc - ya) ** 2) ** 0.5
    min_distance = AB

    if AB > BC:
         min_distance = BC

    if BC > AC:
        min_distance = AC


    return min_distance


print(distance(10,10,20,40,30,20))


print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
