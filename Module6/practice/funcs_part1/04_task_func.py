# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками


def sum2(a,b):
        return (a+b)

def distance(x1, y1, x2, y2):
   res = (x1-x2)**2+(y1-y2)**2
   return (res**0.5)


def can_triangle(p1, p2, p3):
    side1 = distance(p1[0], p1[1], p2[0], p2[1])
    side2 = distance(p2[0], p2[1], p3[0], p3[1])
    side3 = distance(p1[0], p1[1], p3[0], p3[1])
    if side1 < sum2(side2,side3) or side2 < sum2(side1, side3) or side3 < sum2(side2,side1):
        return "Да"
    else: return "Нет"

print(can_triangle((10, 12), (14, 18), (12, 12)))
