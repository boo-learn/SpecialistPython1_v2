# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
n = int(input("Введите n: "))
count = 0
numbers = []
positive_numbers = 0
negative_numbers = 0

import random

while count < n:
    numbers.append((random.randint(-100, 100)))
    count +=1

for number in numbers:

    if number > 0 and number%2 == 0:
        positive_numbers += number
print(numbers)
print(positive_numbers)
