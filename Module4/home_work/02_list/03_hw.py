# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
n = int(input("n : "))
my_list = []
for x in range(1, n):
    my_list.append(random.randint(-100, 100))
print(my_list)
pos_total = 0
for num in my_list:
    if num > 0:
        pos_total += num
print(pos_total)
