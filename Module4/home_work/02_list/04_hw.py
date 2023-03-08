# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]


import random

num_of_numbers = int(input("Введите количество чисел для добавления в список: "))
# num_of_numbers = [2, -5, 8, 9, -25, 25, 4]
numbers = []
sqrt_numbers = []

for number in range(1, num_of_numbers + 1):
    numbers.append(random.randint(-100, 100))
print(numbers)

for number in numbers:
    if number > 0:
        number = number ** 0.5
        if number * 10 % 10 == 0:
            sqrt_numbers.append(int(number))

print(sqrt_numbers)
