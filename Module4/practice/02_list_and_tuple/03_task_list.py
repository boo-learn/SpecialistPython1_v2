# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input("n: "))
randomlist = random.sample(range(- 10, 10), n)
print(f"Список: {randomlist}. Сумма: {sum(randomlist)}")
