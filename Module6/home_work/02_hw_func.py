# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    pass


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

ab = distance(5, 7, 9, 12)
bc = distance(9, 14, 9, 12)
ac = distance(12, 7, 11, 12)

print(ab)
print(bc)
print(ac)

min_n = ab
i = 0
for n in (ab, bc, ac):
    if ab < bc and ab < ac:
      min_n = ab
    elif bc < ab and bc < ac:
       min_n = bc
    else: min_n = ac
i = i + 1
#print(min_n)
if min_n == ab:
    print("Самый короткий отрезок ab, равный", ab)
elif min_n == bc:
    print("Самый короткий отрезок bc, равный", bc)
else:
    print("Самый короткий отрезок ac, равный", ac)

print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
