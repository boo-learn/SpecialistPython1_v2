# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    
    def dist(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return (distance)


x1 = int(input("координата x1= "))
y1 = int(input("координата y1= "))
x2 = int(input("координата x2= "))
y2 = int(input("координата y2= "))
print(dist(x1, y1, x2, y2))



# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
