# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
n = int(input("n="))
numbers = []
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1

sum = 0
for elem in numbers:
    if elem > 0 and elem % 2 == 0:
        sum += elem

print(numbers)
print(sum)
