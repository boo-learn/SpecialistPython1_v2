# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = [2, 4, 0, -10, 2, -5, 0, -5, 1, 7]
sum = 0

for number in numbers:
    if number > 0:
        sum = sum + number
print(sum)
