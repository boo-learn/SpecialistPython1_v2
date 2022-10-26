# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

tups = (2, 4, 6, -4, 12, 0, 5)

tup_max = 0



for tup in tups:
    if tup > tup_max:
        tup_max = tup
print(tup_max)
