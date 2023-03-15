# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
line1 = [5, [1, 2], 2, "r", 4, "ee"]
line2 = [4, "we", "ee", 3, [1, 2]]
line3 = [5, "a", "ee", [1, 2], "r", 3, -2]
same = []
for i in line1:
    if i in same:
        continue
    for j in line2:
        if j == same:
            continue
        for k in line3:
            if i == j == k:
                same.append(k)
                break

print(same)
