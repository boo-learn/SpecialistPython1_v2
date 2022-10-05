# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random

n = int(input("n : "))
my_list = []
for x in range(1, n+1):
    my_list.append(random.randint(-10, 10))
print(my_list)
total_pos = 0
for num in my_list:
    if num > 0:
        total_pos += num

print(total_pos)
