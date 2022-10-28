# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def circle_in_circle(x1, y1, x2, y2, r1, r2):
    dist = distance(x1, y1, x2, y2)
    min_r = min(r1, r2)
    max_r = max(r1, r2)
    if dist + min_r <= max_r:
        print("Внутри")
    else:
        print("Убежал")
    return
