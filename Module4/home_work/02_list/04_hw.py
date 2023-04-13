# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random

numbers = []
squares = []

num_elems = 25 #int(input("Кол-во элементов:"))

for i in range(num_elems):
    numbers.append(random.randint(-100, 100))

print(numbers)

for elem in  numbers:
    if elem > 0:
        sq = elem**0.5
        if  not (sq - int(sq)):
            squares.append(int(sq))

print(squares)
