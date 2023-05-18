# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return distance

A = [1, 3]
B = [5, 9]
C = [2, 6]

AB = distance(*A, *B)
BC = distance(*B, *C)
AC = distance(*A, *C)

min_line = 0

if AB < BC and AB < AC:
    min_line = 'AB'
elif BC < AB and BC < AC:
    min_line = 'BC'
else:
    min_line = 'AC'
# TODO: your code here
print("Самый короткий отрезок:", min_line)  # Выводим название отрезка, например “АС”.

print(AB)
print(BC)
print(AC)
