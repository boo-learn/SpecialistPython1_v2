# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

numbers = []
n = random.randint(3, 20)
i = 0
s_positive = 0
while i <= n:
    number = random.randint(-100, 100)
    if 0 < number and number % 2 == 0:
        s_positive += number
    numbers.append(number)
    i += 1

print(numbers)
print(s_positive)
