# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

tup = (2, 4, 6, -4, 12, 0, 5)
max_val=tup[0]
for val in tup:
    max_val=val if val>max_val else max_val
print(max_val)
