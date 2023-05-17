# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

numbers = [-10, -5, 0, 3, 7]
sum_number = 0
for number in numbers:
    if number > 0:
        sum_number += number
print(sum_number)
