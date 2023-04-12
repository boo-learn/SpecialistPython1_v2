# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

from random import randint
summ=0
numbers = []
for i in range(20):
    numbers.append(randint(-10, 10))
print(numbers)
for number in numbers:
    if number>0:
        summ+=number
print(summ)
