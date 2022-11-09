# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("Число элементов в списке: "))
numbers = []
sum_positive = 0

for i in range(n):
    random_number = random.randint(-100, 100)
    numbers.append(random_number)
print(numbers)

for number in numbers:
    if number > 0 and number % 2 == 0:
        sum_positive += number

print(sum_positive)
