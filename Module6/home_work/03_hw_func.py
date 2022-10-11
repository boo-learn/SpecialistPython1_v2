# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def is_one_circle_in_another(x1, y1, x2, y2, r1, r2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 - r2) ** 2


center1 = 1, 1
center2 = 0, 0
r1 = 1
r2 = 3

print(is_one_circle_in_another(*center1, *center2, r1, r2))
