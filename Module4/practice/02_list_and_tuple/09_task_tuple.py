# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here

tup1 = (2, 4, -6, 8, 32)
tup2 = (2, 0, -6, 12)
tup3 = (11, 23, -6, 2, 4)

result = []
for n1 in tup1:
    for n2 in tup2:
        if n1 == n2:
            for n3 in tup3:
                if n2 == n3:
                    result.append(n1)

print(result)
