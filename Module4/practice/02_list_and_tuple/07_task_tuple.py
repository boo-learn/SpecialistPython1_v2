# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
greater_value = 0
for el in tup:
    if el > greater_value:
        greater_value = el
print(greater_value)
