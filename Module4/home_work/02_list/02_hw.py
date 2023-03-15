# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

n = int(input("Количество цифр "))
arr = []
for ind in range(1, n + 1):
    arr.append(random.randint(-100, 100))
print(arr)

# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
