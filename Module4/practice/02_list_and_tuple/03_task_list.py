# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random
n = int(input())
i = 0
n_list = []
total = 0
while i < n:
    n_list.append(random.randint(-10, 10))
    i += 1
for el in n_list:
    total +=el
print(total)


