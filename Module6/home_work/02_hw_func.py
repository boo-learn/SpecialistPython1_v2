# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

a = (random.randint(-100, 100), random.randint(-100, 100))
b = (random.randint(-100, 100), random.randint(-100, 100))
c = (random.randint(-100, 100), random.randint(-100, 100))

lines_len = [distance(*a, *b), distance(*b, *c), distance(*a, *c)]

print(lines_len)

if lines_len[0] <= lines_len[1] and lines_len[0] <= lines_len[2]:
    shortest = "AB"
elif lines_len[1] <= lines_len[0] and lines_len[1] <= lines_len[2]:
    shortest = "BC"
else:
    shortest = "AC"

print("Самый короткий отрезок:", shortest)  # Выводим название отрезка, например “АС”.
