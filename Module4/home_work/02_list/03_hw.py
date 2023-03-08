# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

num_of_numbers = int(input("Введите количество чисел для добавления в список: "))
numbers = []

sum_positive_num = int()

for number in range(1, num_of_numbers + 1):
    numbers.append(random.randint(-100, 100))
print(numbers)

for number in numbers:
    if number > 0 and number % 2 == 0:
        sum_positive_num += number


print("Сумма всех положительных чисел кратных 2 равна: ", sum_positive_num)
