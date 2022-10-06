# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random
numbers = []
n = int(input("Введите n: "))
i = 0
sum_ = 0
while i < n:
    numbers.append(random.randint(-10, 10))
    i += 1
for num in numbers:
    sum_ += num
print(numbers)
print("Сумма", sum_)
