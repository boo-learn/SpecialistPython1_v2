# Напишите функцию, возвращающую наибольшее из двух чисел

def max2(a, b):

    return a if a > b else b




# Тестируем функцию
print(max2(5, 6))
print(max2(-10, -12))
print(max2(2.5, 2.6))
print(max2(-2.5, 0))
print(max2(0, -2.5))
