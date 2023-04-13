# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


points = [3, 1, 3, 9, 1, 5]

a = distance(points[0], points[1], points[2], points[3])
b = distance(points[2], points[3], points[4], points[5])
c = distance(points[4], points[5], points[0], points[1])

if a <= b and a <= c:
    print(f'Самый короткий отрезок АВ.')
elif b < c:
    print(f'Самый короткий отрезок ВC.')
else:
    print(f'Самый короткий отрезок CA.')


# TODO: your code here
print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
