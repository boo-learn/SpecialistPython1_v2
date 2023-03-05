# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
max_element = -999
for element in tup:
    if max_element < element:
        max_element = element
print(max_element)

# TODO: your code here
