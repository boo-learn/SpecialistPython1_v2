# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона
def can_triangle(p1, p2, p3):
    return abs((p1[0] - p2[0]) / (p2[0] - p3[0])) != \
           abs((p1[1] - p2[1]) / (p2[1] - p3[1]))

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def perim_area(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p1, p3)
    perimeter = a + b + c
    p = perimeter / 2
    area = (p * (p - a) * (p - b) * (p - c))
    return perimeter, area

tr1 = ((10, 12), (14, 18), (12, 12))
tr2 = ((10, 10), (14, 14), (12, 12))

print(tr1)
if can_triangle(*tr1):
    print(perim_area(*tr1))

print(tr2)
if can_triangle(*tr2):
    print(perim_area(*tr2))
else:
    print("треугольник построить нельзя, но все-таки выводим результат функции:")
    print(perim_area(*tr2))

# Не забудьте протестировать вашу функцию
