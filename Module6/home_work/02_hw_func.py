# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


A = (2, 3)
B = (6, 7)
C = (0, 9)

if distance(*A, *B) < distance(*B, *C) and distance(*A, *B) < distance(*C, *A):
    minimum = 'AB'

elif distance(*A, *C) < distance(*B, *C) and distance(*A, *C) < distance(*A, *B):
    minimum = 'AC'
else:
    minimum = 'BC'

print("Самый короткий отрезок:", minimum)
