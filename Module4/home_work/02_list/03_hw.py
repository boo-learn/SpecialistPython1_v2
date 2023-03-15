# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

n = int(input("n: "))
i = 0
numbers = []
sum = 0

while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1

for word in numbers:
    if word > 0 and word % 2 ==0:
        sum += word
print(numbers)
print(sum)
