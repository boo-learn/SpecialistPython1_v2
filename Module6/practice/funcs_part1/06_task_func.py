# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    return abs(x - xc) < r and abs(y - yc) < r


point = (10, 10)
center = (5, 5)
radius = 2

if point_in_circle(*point, *center, radius):
    print("Точка находится внутри окружности")
else:
    print("Точка не находится внутри окружности")


# Не забудьте протестировать вашу функцию
