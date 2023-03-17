# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):

    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

point_a = (2, 3)
point_b = (7, -3)
point_c = (5, 1)

dic = { 'AB':0, 'CB':0, 'AC':0 }
dic['AB'] = distance(*point_a, *point_b)
dic['CB'] = distance(*point_c, *point_b)
dic['AC'] = distance(*point_a, *point_c)
dic_min = sorted(dic.values())
dic_min_sorted = {}

for i in dic_min:
    for k in dic.keys():
        if dic[k] == i:
            dic_min_sorted[k] = dic[k]
            break
print(dic_min_sorted)
print("Самый короткий отрезок:", list(dic_min_sorted.keys())[0], list(dic_min_sorted.values())[0])
