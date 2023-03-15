# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа


tup = (2, 4, 6, -4, 12, 0, 5)
big = tup[0]

for bigger in tup:
    if big < bigger:
        big = bigger

print(big)
