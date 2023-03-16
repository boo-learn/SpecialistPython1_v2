# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []
n = int(input("Введите количество элементов: "))
i = 0
summ = 0

while i != n:
    numbers.append(random.randint(-100, 100))
    i += 1

print("Сгенерированный список:", numbers)

for number in numbers:
    if number > 0 and number % 2 == 0:
        summ += number

print("Cумма всех положительных элементов кратных двум:", summ)
