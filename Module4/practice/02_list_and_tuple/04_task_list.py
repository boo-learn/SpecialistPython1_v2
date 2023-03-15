# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
number_list = [-10, 0, 1, 5, -7, -9, 8, 4]
numbers_sum = 0
for number in number_list:
    if number > 0:
        numbers_sum = numbers_sum + number
print(numbers_sum)
