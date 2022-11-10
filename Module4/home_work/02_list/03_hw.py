# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("Количество чисел "))
arr = []
summa = 0
for ind in range(0, n):
    arr.append(random.randint(-100, 100))
    summa += arr[ind]
print(summa)
