# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here

def distance(p1: tuple, p2: tuple):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def sides(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    return [a, b, c]


def can_triangle(s: list):
    return s[0] < s[1] + s[2] and s[1] < s[0] + s[2] and s[2] < s[0] + s[1]


def area(s: list):
    p = (s[0] + s[1] + s[2]) / 2
    return (p * (p - s[0]) * (p - s[1]) * (p - s[2])) ** 0.5


def perimeter(s: list):
    return s[0] + s[1] + s[2]


# Пример вызова функции
p1 = (0, 0)
p2 = (0, 4)
p3 = (3, 0)
s = sides(p1, p2, p3)
if can_triangle(s):
    print('Area:', area(s))
    print('Perimeter:', perimeter(s))
# Не забудьте протестировать вашу функцию
