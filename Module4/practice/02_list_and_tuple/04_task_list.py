# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
some_list = [4, 1, 5, 4, 10, 4, -8, 3, -7]
sum_elements = 0
for i in some_list:
    if i > 0:
        sum_elements += i
print(sum_elements)
