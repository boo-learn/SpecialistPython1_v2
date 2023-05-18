# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
n = int(input("n: "))
i = 0
summa = 0
for i in range(n):
    random_number = random.randint(-100, 101)
    numbers.append(random_number)
    if random_number > 0 and random_number % 2 == 0:
        summa += random_number
print(numbers)
print(summa)
