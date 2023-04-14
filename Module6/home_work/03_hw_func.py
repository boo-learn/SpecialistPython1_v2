# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def is_circle_inside(x1, y1, x2, y2, r1, r2):
    value = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 + r2
    return value <= r1


if (is_circle_inside(4, 4, 4, 3, 3, 2)):
    print("Внутри")
else:
    print("Не поместился!")
