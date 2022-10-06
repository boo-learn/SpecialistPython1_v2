# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


a = 10, 12
b = 14, 18
c = 12, 12

segments = (distance(*a, *b), distance(*a, *c), distance(*b, *c))
segment_names = ("AB", "AC", "BC")
min_index = 0
min_length = segments[0]

for i, segment in enumerate(segments):
    if segment < min_length:
        min_index = i
        min_length = segment

print(f"Самый короткий отрезок: {segment_names[min_index]}")
