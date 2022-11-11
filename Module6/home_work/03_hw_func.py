# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def check_circles(c1_x, c1_y, c1_r, c2_x, c2_y, c2_r):
    return dist(c1_x, c1_y, c2_x, c2_y) + min(c1_r, c2_r) <= max(c1_r, c2_r)


# x1 x2 r
circle1 = (0,0,5)
circle2 = (0,3,2.1)
if check_circles(*circle1,*circle2):
    print("Окружность вложенная")
else:
    print("Окружность не вложенная")
