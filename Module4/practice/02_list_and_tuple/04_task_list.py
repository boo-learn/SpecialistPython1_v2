# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random

n = int(input("n: "))
randomlist = random.sample(range(- 10, 10), n)

summ = 0

for element in randomlist:
    if element > 0:
        summ += element

print(f"Список: {randomlist}. Сумма положительных элементов: {summ}")

