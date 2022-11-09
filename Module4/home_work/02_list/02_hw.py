# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

n = int(input("Число элементов в списке: "))
numbers = []

for i in range(n):
    random_number = random.randint(-100, 100)
    numbers.append(random_number)

print(numbers)
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
