# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    total = 0
    for val in args:
        total += val
    return total/len(args)


print(average(3, 4, 8), sum([3, 4, 8])/3)
print(average(1, 4, 5, -3, 8, 4), sum([1, 4, 5, -3, 8, 4])/6)
print(average(-10, 12, 6.3, -5.5, 7, 0.2), sum([-10, 12, 6.3, -5.5, 7, 0.2])/6)
