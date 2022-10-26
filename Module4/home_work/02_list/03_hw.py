# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

n = int(input("Введите n:"))
numbers = []
i = 0
while i < n:
    a = random.randint(-100, 100)
    numbers.append(a)
    i += 1
print("Весь список:", numbers)
total = 0
for number in numbers:
    if number % 2 == 0 and number > 0:
        total += number
print("Cумма положительных чисел,кратно 2:", total)
