# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here



import random

n = int(input('Введите длину списка из n элементов: '))
numbers = []
count = 0  # счетчик
while count < n:
    num2 = random.randint(-100, 100)
    numbers = num2
    count = count + 1
    print(numbers)
