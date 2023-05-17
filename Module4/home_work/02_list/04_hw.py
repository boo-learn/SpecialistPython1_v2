# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

from random import randint

init_list = [randint(-100, 100) for i in range(int(input("n: ")))]
sqrt_list = []

for number in init_list:
    if number > 0 and number ** 0.5 % 1 == 0:
        sqrt_list.append(int(number ** 0.5))
print(init_list)
print(sqrt_list)
