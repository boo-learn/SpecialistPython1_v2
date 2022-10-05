# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input("n : "))
my_list = []
for x in range(1, n):
    my_list.append(random.randint(-10, 10))
print(my_list)

print(sum(my_list))

