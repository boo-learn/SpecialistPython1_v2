# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    sum_p1p2 = p1 + p2
    sum_p2p3 = p3 + p2
    sum_p1p3 = p1 + p3
if not (sum_p1p2 + sum_p2p3) > sum_p1p3 and (sum_p1p2 + sum_p1p3) > sum_p2p3 and (sum_p2p3 + sum_p1p3) > sum_p1p2:
    return "НЕТ"
return "ДА"
# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))



# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
