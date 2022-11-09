# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.
import random

n = int(input("Кол-во элементов в списке: "))
numbers = []
numbers_sum = 0

for i in range(n):
    random_numbers = random.randint(-10, 10)
    numbers.append(random_numbers)

for number in numbers:
    if number > 0:
        numbers_sum += number

print("Полученный список: ", numbers)
print("Сумма положительных чисел списка: ", numbers_sum)
