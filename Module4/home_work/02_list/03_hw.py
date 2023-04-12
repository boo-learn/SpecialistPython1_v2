# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("Введите значение n: "))
numbers = []
for _ in range(n):
    numbers.append(random.randint(-100, 100))

total = 0
for number in numbers:
    if number > 0 and number % 2 == 0:
        total += number

print("Случайно сгенерированная последовательность из", n, "чисел в диапазоне [-100:100]:")
print(numbers)
print("Сумма всех кратных двум положительных чисел последовательности: ", total)

