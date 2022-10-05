# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []

total = 0
n = int(input("Enter number values: "))
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    if numbers[i] > 0 and numbers[i] % 2 == 0:
        total += numbers[i]
    i += 1

print(numbers)
print(total)
