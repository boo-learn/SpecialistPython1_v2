# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def circle(point1, point2, r1, r2):
    if r1 > r2:
        r1, r2 = r2, r1

    return r2 >= r1 + distance(*point1, *point2)


point1 = (10, 10)
point2 = (10, 11)
r1 = 1
r2 = 2

print(circle(point1, point2, r1, r2))
