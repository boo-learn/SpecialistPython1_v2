# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.
numbers = 1, 3, 5, -10, 7
sum_positive_numbers = 0

for number in numbers:
    if number > 0:
        sum_positive_numbers += number

print(sum_positive_numbers)
