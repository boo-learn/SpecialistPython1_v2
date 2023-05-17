# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup1 = (2, 4, -6)
tup2 = (2, "Василия", -6, 4)
tup3 = 2, 4, -6
counter_doubles = 0
lst = []

for i in tup1:
    for j in tup2:
        for k in tup3:
            if i == j == k and i not in lst:
                counter_doubles += 1
                lst.append(i)

print(counter_doubles)
