# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = [2, 5, 8, - 10, 8, -2]

summa_plus = 0
for number in numbers:
    if number > 0:
        summa_plus += number
print(summa_plus)
