# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random

random_numbers = []
n = 50
for i in range(n):
    random_numbers.append(random.randint(-100, 100))

summa = 0
for num in random_numbers:
    if num > 2 and num % 2 == 0:
        summa = summa + num
print(summa)
