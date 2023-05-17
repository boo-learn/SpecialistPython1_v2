# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.
from random import randint

numbers = [randint(-10, 10) for i in range(10)]

print(numbers)
print(sum(number for number in numbers if number > 0))

