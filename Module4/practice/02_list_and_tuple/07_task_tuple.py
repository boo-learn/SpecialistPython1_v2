# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

max_number = tup[0]

for number in tup:
    if number > max_number:
        max_number = number
print("Самый большой: ", max_number)
