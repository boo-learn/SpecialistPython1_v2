# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = 5

numbers = []
i = 1
while i <= n:
    numbers.append(random.randint(-100, 100))
    i += 1

total = 0
for el in numbers:
    if el > 0 and el % 2 == 0:
        total += el
print(numbers)
print(total)
