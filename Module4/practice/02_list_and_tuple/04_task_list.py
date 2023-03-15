# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

elements = [1, 7, 9, -9, 5, -3]

result = 0
for i_element in elements:
    if i_element > 0:
        result = result + i_element
print(result)
