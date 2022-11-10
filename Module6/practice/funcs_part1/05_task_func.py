# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def can_triangle(coord):
    x1, y1 = coord[0]
    x2, y2 = coord[1]
    x3, y3 = coord[2]
    area_triangle = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if area_triangle != 0:
        return True
    else:
        return False


def square_triangle(coord):
    x1, y1 = coord[0]
    x2, y2 = coord[1]
    x3, y3 = coord[2]
    square = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return square


def perimeter_triangle(coord):
    x1, y1 = coord[0]
    x2, y2 = coord[1]
    x3, y3 = coord[2]
    ab = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    bc = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    ac = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    perimeter = ab + bc + ac
    return perimeter


coordinates = [(10, 12), (14, 18), (12, 12)]
if can_triangle(coordinates):
    print(f"Периметр треугольника равен: {perimeter_triangle(coordinates)}")
    print(f"Площадь треугольника равна: {square_triangle(coordinates)}")
else:
    print("Треугольник по заданным точкам треугольник построить нельзя")


# Не забудьте протестировать вашу функцию
