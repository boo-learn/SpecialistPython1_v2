# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def distance(x1, y1, x2, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d


def can_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def get_triangle_perimeter(a, b, c):
    return a + b + c


def get_triangle_area(a, b, c):
    p = 0.5 * get_triangle_perimeter(a, b, c)           # Полупериметр для формулы Герона
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


p1 = (10, 10)
p2 = (12, 17)
p3 = (3, 13)

side_a = distance(*p1, *p2)
side_b = distance(*p1, *p3)
side_c = distance(*p2, *p3)

if can_triangle(side_a, side_b, side_c):
    print("Треугольник существует")
    print("Периметр треугольника: ", get_triangle_perimeter(side_a, side_b, side_c))
    print("Площадь треугольника: ", get_triangle_area(side_a, side_b, side_c))
else:
    print("Треугольник НЕ существует")



# Не забудьте протестировать вашу функцию
