# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
n = int(input("n = "))
i = 0
my_list = []
while i <= n:
    my_list.append(random.randint(-100, 100))
    i += 1

print(my_list)

