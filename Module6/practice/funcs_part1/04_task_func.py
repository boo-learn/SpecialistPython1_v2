# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(a, b, c):
    side_ab = round(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5, 2)
    side_ac = round(((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5, 2)
    side_bc = round(((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2) ** 0.5, 2)
    print(side_ab, side_bc, side_ac)

    return "Треугольник существует" if side_ab + side_bc > side_ac and side_bc + side_ac > side_ab and side_ab + side_ac > side_bc else "Треугольник не существует"

# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
