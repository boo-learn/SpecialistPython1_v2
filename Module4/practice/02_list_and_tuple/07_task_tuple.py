# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

max_numb = 0
for number in tup:
    if number > max_numb:
        max_numb = number
print(max_numb)
