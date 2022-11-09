# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
num_list = []
max_number = 0
i = 0

for i_tup in tup:
    if max_number < i_tup:
        max_number = i_tup
        num_list = [i, max_number]
    i += 1
print("Самый большой элемент кортежа номер:", num_list[0], "со значением:", num_list[1])
