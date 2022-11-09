# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here

max_el = (2, 4, 6, -4, 12, 0, 5)
max_num = 0
for el in max_el:
    if el > max_num:
        max_num = el
print(max_num)
