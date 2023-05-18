# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.

from math import *


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
