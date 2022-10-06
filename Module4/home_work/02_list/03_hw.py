# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input("Введите количество элементов: "))
i = 0
count = 0

while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1

for el in numbers:
    if el > 0 and el % 2 == 0:
        count += el

print(numbers)
print(count)
