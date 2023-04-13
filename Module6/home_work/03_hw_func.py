# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def is_circle_in_circle(x1, y1, r1, x2, y2, r2):
    flag = False
    if x1 == x2 and y1 == y2 and r1 == r2:                      # вариант полного совпадения
        flag = True
    if r1 > r2:
        if abs(x1 - x2) + r2 < r1 and abs(y1 - y2) + r2 < r1:   # первая окружность больше
            flag = True
    else:
        if abs(x1 - x2) + r1 < r2 and abs(y1 - y2) + r1 < r2:   # вторая окружность больше
            flag = True
    return flag


circle1 = (10, 10, 10)
circle2 = (10, 11, 15)

if is_circle_in_circle(*circle1, *circle2):
    print("Одна из окружностей находится внутри другой")
else:
    print("Окружности НЕ находятся одна в другой")
