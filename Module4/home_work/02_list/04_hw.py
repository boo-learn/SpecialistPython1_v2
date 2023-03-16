# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
numbers = [2, -5, 8, 9, -25, 25, 4]
new_numbers = []

for number in numbers:
    if number > 0 and number ** 0.5 % 1 == 0:
        new_numbers.append(number ** 0.5)
print(new_numbers)
