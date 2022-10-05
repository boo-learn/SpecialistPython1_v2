# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input('Введи число чисел:'))
numbers = []

for i in range(1, n):
    numbers.append(random.randint(-100, 100))

summ = 0
for num in numbers:
    if num>0:
        summ+=num
print(numbers)
print(summ)
