# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here


# Не забудьте протестировать вашу функцию
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p1[0], p1[1], p3[0], p3[1])
    c = distance(p2[0], p2[1], p3[0], p3[1])
    return a + b > c and a + c > b and b + c > a


def find_square_perimetr(p1, p2, p3):
    if not can_triangle(p1, p2, p3):
        print("По заданным точкам нельзя построить треугольник")
        return
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p1[0], p1[1], p3[0], p3[1])
    c = distance(p2[0], p2[1], p3[0], p3[1])
    p = a + b + c
    half_p = p / 2
    s = (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5
    return p, s
