# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# import random
n = int(input("Введите количество элементов для выдачи: "))
numbers = [random.randint(-100, 100) for value in range(n)]
print(numbers)
i = 0
num_positive = 0
for i in numbers:
    if i > 0 and i % 2 == 0:
        num_positive += i
print(num_positive)
