# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(*arg):
    max=arg[0]
    for num in arg:
       if num > max: max = num

    return max
# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
