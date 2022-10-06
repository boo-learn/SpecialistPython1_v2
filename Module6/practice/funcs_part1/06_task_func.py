# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def point_in_circle(x, y, xc, yc, r):
    return distance((x, y), (xc, yc)) < r


# Не забудьте протестировать вашу функцию

vals1 = (1, 2, 3, 4, 5)
vals2 = (0, 0, 5, 5, 3)
vals3 = (-1, -2, 3, 4, 10)
vals4 = (0, 0, 0, 0, 0)

print(point_in_circle(*vals1))
print(point_in_circle(*vals2))
print(point_in_circle(*vals3))
print(point_in_circle(*vals4))

