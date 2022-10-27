# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    count_el = 0
    max_el = 0
    for el in args:
        max_el += el
        count_el += 1
    return max_el / count_el


print(average(3, 4, 5, 6, 7))
print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
