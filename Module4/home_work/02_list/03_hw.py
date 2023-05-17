# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("n: "))

numbers = []
i = 0
positive_event_count = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    if numbers[i] > 0 and numbers[i] % 2 == 0:
        positive_event_count += 1
    i += 1

print("positive_event_count: ", positive_event_count)
