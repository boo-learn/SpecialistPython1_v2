# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

from lib import distance

xa = int(input("xa: "))
ya = int(input("ya: "))
xb = int(input("xb: "))
yb = int(input("yb: "))
xc = int(input("xc: "))
yc = int(input("yc: "))

a = distance(xa,ya,xb,yb)
print(a)
b = distance(xb,yb,xc,yc)
print(b)
if a > b:
    print("Самый короткий отрезок BC")
else:
    print("Самый короткий отрезок AB")
