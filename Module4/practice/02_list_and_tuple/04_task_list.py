# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

'''
import random

num_list = [random.randrange(-10, 10) for _ in range(int(input()))]
num_sum = 0

for number in num_list:
    if number > 0:
        num_sum += number
print(num_sum)
'''
