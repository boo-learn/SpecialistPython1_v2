# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random

random_numbers = []
n = 50
for i in range(n):
    random_numbers.append(random.randint(-100, 100))

print(random_numbers)
square_root_numbers = []
for num in random_numbers:
    if num > 0 and (num**(1/2)).is_integer():
        square_root_numbers.append(int(num**(1/2)))

print(square_root_numbers)
