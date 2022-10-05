# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input("Введите кол-во элементов n в списке:"))
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)
for num in numbers:
    if num >= 0 and num % 2 == 0:
        print(num, end=" ")
