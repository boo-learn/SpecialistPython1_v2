# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
max_num = 0

for num in tup:
    if max_num < num:
        max_num = num

print(max_num)
