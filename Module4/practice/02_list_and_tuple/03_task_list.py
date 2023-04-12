# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input("Введите значение n: "))
numbers = []
i = 0
while i < n:
    numbers.append(random.randint(-10, 10))
    i += 1

total = 0
for number in numbers:
    total += number
print(numbers)
print("Сумма всех значений", total)
