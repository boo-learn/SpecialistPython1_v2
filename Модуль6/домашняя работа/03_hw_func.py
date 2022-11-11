# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here

from dz6modN1 import dist

# def dist(x1, y1, x2, y2):
#     d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#     return d

p_x1 = 2
p_y1 = 1
p_x2 = 3
p_y2 = 1
r1 = 9
r2 = 2

if dist(p_x1, p_y1, p_x2, p_y2) + r2 < r1:
    print("Окружность 2 полностью вложена")

elif dist(p_x1, p_y1, p_x2, p_y2) + r1 < r2:
    print("Окружность 1 полностью вложена")

else:
    print("Окружность не вложена")
