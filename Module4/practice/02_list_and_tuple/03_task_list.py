# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.
import random

n = int(input("n: "))
numbers = []
numbers_sum = 0

for i in range(n):
    random_numbers = random.randint(-10, 10)
    numbers.append(random_numbers)

for number in numbers:
    numbers_sum += number

print(numbers_sum)
