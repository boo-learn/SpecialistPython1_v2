# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())


def heron_formula(ab, bc, ca):
    p = (ab + bc + ca) * 0.5
    s = (p * (p - ab) * (p - bc) * (p - ca)) ** 0.5
    return s


side_ab = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
side_bc = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
side_ca = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5

if (side_ab < side_bc + side_ca) \
        and (side_bc < side_ab + side_ca) \
        and (side_ca < side_ab + side_bc):
    s_triangle = heron_formula(side_ab, side_bc, side_ca)
    print(f"{s_triangle:.2f}")
else:
    print("Треугольника не существует")


# Не забудьте протестировать вашу функцию
