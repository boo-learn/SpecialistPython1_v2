# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint


import random

num_of_numbers = int(input("Введите количество чисел для добавления в список: "))
numbers = []

for number in range(1, num_of_numbers + 1):
    numbers.append(random.randint(-100, 100))

print(numbers)
