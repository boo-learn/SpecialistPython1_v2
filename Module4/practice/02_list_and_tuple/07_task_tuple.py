# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here

n_max = float('-inf')
for n in tup:
    if n > n_max:
        n_max = n

print(n_max)
