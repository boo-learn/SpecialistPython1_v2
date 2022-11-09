# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
my_list = [2, 5, 7, 13, 0, -2]
total = 0
for element in my_list:
    if element > 0:
        total += element
print(total)
