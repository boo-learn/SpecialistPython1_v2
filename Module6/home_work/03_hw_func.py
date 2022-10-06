# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def circle(a, b, r1, r2):
    dist = distance(*a, *b)
    return dist - (r1 + r2) < r1 or dist - (r1 + r2) < r2


cent_1 = (2, 3)
cent_2 = (6, 7)
R1 = 3
R2 = 1

if circle(cent_1, cent_2, R1, R2):
    print('Да')
else:
    print('Нет')
