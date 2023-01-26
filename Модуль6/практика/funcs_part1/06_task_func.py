# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    # TODO: your code here
    pass

# Не забудьте протестировать вашу функцию
def point_in(x1, y1, x0, y0, r):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5 <= r


print(point_in(2, 2, 6, 2, 4))
