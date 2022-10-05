# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

max_elem = 0
for elem in tup:
    if elem > max_elem:
        max_elem = elem
print(max_elem)
