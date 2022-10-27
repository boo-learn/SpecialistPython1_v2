# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    coordinatesx = (x1, x2)
    coordinatesy = (y1, y2)
    dist = ((float(coordinatesx[0]) - float(coordinatesx[1])) ** 2 + (
                float(coordinatesy[0]) - float(coordinatesy[1])) ** 2) ** 0.5
    return dist


# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
