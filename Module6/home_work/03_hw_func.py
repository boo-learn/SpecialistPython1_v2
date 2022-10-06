# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def nesting(x1, y1, x2, y2, r1, r2):
    return (r1 < r2 and distance(x1, y1, x2, y2) + r1 <= r2) or \
           (r1 > r2 and distance(x1, y1, x2, y2) + r2 <= r1) or \
           (r1 == r2 and distance(x1, y1, x2, y2) = 0)


print(nesting(5, 6, 7, 8, 7, 21))
