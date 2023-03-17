# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    dist = ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5
    return dist <= r


print(point_in_circle(1, 1, 2, 2, 5))
print(point_in_circle(7, 8, 10, 10, 5))
print(point_in_circle(2, 2, 8, 8, 1))
print(point_in_circle(-1, -1, -5, -2, 0.5))



