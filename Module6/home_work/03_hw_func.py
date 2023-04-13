# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


p1 = 4, 4
p2 = 4, 2
r1 = 8
r2 = 6
distance_enters_circles = distance(*p1, *p2)
min_radius = min(r1, r2)
max_radius = max(r1, r2)
if distance_enters_circles + min_radius <= max_radius:
    print("окружность целиком внутри другой")
else:
    print("окружность не целиком внутри другой")
