# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

numbers = [-1, 2, 3, -4, 5]
numbers_sum = 0
for elem in numbers:
    if elem > 0:
        numbers_sum += elem
print(numbers_sum)

