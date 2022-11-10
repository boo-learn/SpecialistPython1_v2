# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


xa = int(input("Координата x точки A:"))
ya = int(input("Координата y точки A:"))
xb = int(input("Координата x точки B:"))
yb = int(input("Координата y точки B:"))
xc = int(input("Координата x точки C:"))
yc = int(input("Координата y точки C:"))

# 1 вариант
# ab = distance(xa, ya, xb, yb)
# bc = distance(xb, yb, xc, yc)
# ca = distance(xc, yc, xa, ya)
#sides = [ab, bc, ca]

sides = [distance(xa, ya, xb, yb), distance(xb, yb, xc, yc), distance(xc, yc, xa, ya)]
print(sides)
shortest_side = sides[0]

for side in sides:
    if side <= shortest_side:
        shortest_side = side

print("Самый короткий отрезок:", shortest_side)  # Выводим название отрезка, например “АС”.
'''
координаты равнобедренного треугольника для проверки:
(4, 2), (6, 5), (8, 2)
'''
