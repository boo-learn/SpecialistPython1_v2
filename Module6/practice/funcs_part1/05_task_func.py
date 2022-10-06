# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    if p1 == p2 or p1 == p2 or p2 == p3:
        return False
    else:
        tan1 = abs((p2[1] - p1[1]) / (p2[0] - p1[0]))
        tan2 = abs((p3[1] - p1[1]) / (p3[0] - p1[0]))
        if tan1 == tan2:
            return False
        else:
            return True


def square(l1, l2, l3):
    p = (l1 + l2 + l3) / 2
    return (p * (p - l1) * (p - l2) * (p - l3)) ** 0.5


def per(l1, l2, l3):
    return (l1 + l2 + l3)


# points = ((10, 12), (14, 18), (12, 12))
# points = ((1, 1), (2, 2), (3, 3))
# points = ((-1, -1), (2, 2), (3, 3))
points = ((1, 9), (1, 1), (1, 1))
l1 = distance(points[0][0], points[0][1], points[1][0], points[1][1])
l2 = distance(points[0][0], points[0][1], points[2][0], points[2][1])
l3 = distance(points[2][0], points[2][1], points[1][0], points[1][1])
if can_triangle(points[0], points[1], points[2]):
    print(f' сторона 1 = {l1:.2f}')
    print(f' сторона 2 = {l2:.2f}')
    print(f' сторона 3 = {l3:.2f}')
    print(f'площадь = {square(l1, l2, l3):.2f}')
    print(f'периметр = {per(l1, l2, l3):.2f}')
else:
    print(f' сторона 1 = {l1:.2f}')
    print(f' сторона 2 = {l2:.2f}')
    print(f' сторона 3 = {l3:.2f}')
    print('треугольник не существует')

