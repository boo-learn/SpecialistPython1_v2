# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

numbers = [5, 4, 0, -3, 10, 7, 3, -2, 9]

sum_positive = 0
for number in numbers:
    if number > 0:
        sum_positive = sum_positive + number
print(sum_positive)
