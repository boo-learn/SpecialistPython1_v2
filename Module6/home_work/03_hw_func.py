# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here

def is_one_circle_inside_another(x1, y1, r1, x2, y2, r2):

    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

   
    if distance + min(r1, r2) <= max(r1, r2):
        return "Окружность находится внутри "#True
    else:
        return "Окружность НЕ находится внутри"#False

#Проверка
x1, y1, r1 = 0, 0, 5
x2, y2, r2 = 0, 0, 10
print(is_one_circle_inside_another(x1, y1, r1, x2, y2, r2))  # Да

x1, y1, r1 = 0, 0, 5
x2, y2, r2 = 20, 20, 5
print(is_one_circle_inside_another(x1, y1, r1, x2, y2, r2))  # Нет
