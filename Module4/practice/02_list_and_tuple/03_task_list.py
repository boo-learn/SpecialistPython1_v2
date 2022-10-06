# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.
import random

n = int(input("Введите количество элементов в списке: "))
numbers = []
total = 0
i = 0

while i < n:
    numbers.append(random.randint(-10, 10))
    i += 1

for el in numbers:
    total += el

print(numbers)
print(total)
