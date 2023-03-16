# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

n = int(input('Введите количество элементов: '))
BEGINNING = -100
FINISH = 100
numbers = []
i = 1

while i <= n:
    numbers.append(random.randint(BEGINNING, FINISH))
    i += 1

print('Список произвольных элементов:')
print(numbers)

total = 0

for j in numbers:
    if j > 0 and j % 2 == 0:
        total += j
print()
print('Сумма всех положительных элементов списка, кратных 2, равна: ', total)
