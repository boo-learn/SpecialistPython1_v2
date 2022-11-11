# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def circles(radius2, radius1, coord_x2, coord_x1, coord_y2, coord_y1):
    return ((radius2 - radius1) ** 2 > (coord_x2 - coord_x1) ** 2 + (coord_y2 - coord_y1) ** 2)

print(circles(6,86,77,45,43,56))
