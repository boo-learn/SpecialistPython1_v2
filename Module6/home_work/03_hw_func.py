# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def circles(x1,y1,x2,y2,r1,r2):
    return ((r2-r1)**2 > (x2-x1)**2 + (y2-y1)**2)

#проверка
print(circles(1,2,1,2,2,4))
print(circles(5,2,4,2,5,4))
