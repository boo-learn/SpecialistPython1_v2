# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def circle_intersect(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 - r2) ** 2:
        return True
    return False


point_circle_x1 = int(input("x1: "))
point_circle_y1 = int(input("y1: "))
circle_r1 = int(input("R1: "))
point_circle_x2 = int(input("x2: "))
point_circle_y2 = int(input("y2: "))
circle_r2 = int(input("R2: "))
if circle_intersect((point_circle_x1, point_circle_y1, circle_r1), (point_circle_x2, point_circle_y2, circle_r2)):
    print("Одна окружность целиком внутри другой")
else:
    print("Окружности не пересекаются")
