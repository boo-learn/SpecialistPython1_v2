# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = [2, -5, 0, 4, -7, 6, 8]

summa = 0
for number in numbers:
    if number > 0:
        summa += number
print(summa)
