# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

from random import randint

number = [randint(-10, 10) for i in range(10)]
print(number)
print(sum(number))
