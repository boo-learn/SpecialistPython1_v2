# Напишите функцию, возвращающую наибольшее из двух чисел

def max2(num1: int | float, num2: int | float) -> int | float:
    if num1 > num2:
        return num1
    else:
        return num2


# Тестируем функцию
print(max2(5, 6))
print(max2(-10, -12))
print(max2(2.5, 2.6))
print(max2(-2.5, 0))
print(max2(0, -2.5))
