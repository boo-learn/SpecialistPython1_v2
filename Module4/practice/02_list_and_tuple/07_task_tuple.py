# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
tup = (2, 4, 6, -4, 12, 0, 5)
max_num_here = tup[0]
for element in tup:
    if element > max_num_here:
        max_num_here = element
print(max_num_here)
