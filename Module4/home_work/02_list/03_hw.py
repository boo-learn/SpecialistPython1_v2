# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random

number = int(input("Введите количество элементов: "))
numbers = []
i = 1
summa = 0

while i <= number:
    numbers.append(random.randint(-100, 100))
    i += 1
for el in numbers:
    if el > 0 and el % 2 == 0:
        summa += el

print(numbers)
print(summa)
