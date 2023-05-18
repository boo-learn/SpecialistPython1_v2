# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4)


# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
