# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def can_triangle(p1: tuple, p2: tuple, p3: tuple) -> bool:
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p2[0], p2[1], p3[0], p3[1])
    c = distance(p3[0], p3[1], p1[0], p1[1])
    return a + b > c or a + c > b or b + c > a

def triangle_perimetr(p1: tuple, p2: tuple, p3: tuple) -> float:
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p2[0], p2[1], p3[0], p3[1])
    c = distance(p3[0], p3[1], p1[0], p1[1])
    return a + b + c

def triangle_area(p1: tuple, p2: tuple, p3: tuple) -> float:
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p2[0], p2[1], p3[0], p3[1])
    c = distance(p3[0], p3[1], p1[0], p1[1])
    pp = (a + b + c) / 2
    return (pp * (pp - a) * (pp - b) * (pp - c))**0.5

p1 = (10, 12)
p2 = (14, 18)
p3 = (12, 12)
if can_triangle(p1, p2, p3):
    print(f"triangle_perimetr {triangle_perimetr(p1, p2, p3)}")
    print(f"triangle_area {triangle_area(p1, p2, p3)}")
else: print("Треугольник не существует")

# Не забудьте протестировать вашу функцию
