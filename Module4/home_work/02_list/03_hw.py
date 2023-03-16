# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
n = 10
i = 0
numbers = []
while i < 10:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)

summ = 0
for num in numbers:
    if num > 0:
        summ += num
print("Positive numbers sum is: ", summ)
