# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
n = int(input("Введите n: "))

for __ in range(n):
    numbers.append(random.randint(-100, 100))

print(numbers)
# TODO: your code here
