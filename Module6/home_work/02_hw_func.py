# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

xa, ya = 5, -2
xb, yb = 0, 3.5
xc, yc = -10, -22.1

segments = [ ("AB", distance(xa, ya, xb, yb)), ("AC", distance(xa, ya, xc, yc)), ("BC", distance(xc, yc, xb, yb))]
# не нашел пока функцию, которая искала бы минимальное значение по второму элементу кортежей
# поэтому делаю перебором

min_len = segments[0][1]
min_name = segments[0][0]

for segment in segments:
    if segment[1] < min_len:
        min_len = segment[1]
        min_name = segment[0]
print("Самый короткий отрезок:", min_name)  # Выводим название отрезка, например “АС”.
print(segments)
