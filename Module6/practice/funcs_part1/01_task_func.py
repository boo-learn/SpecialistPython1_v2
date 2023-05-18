# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4: int | float) -> int | float:
    if n1 > n2:
        n1, n2 = n2, n1    
    if n3 > n4:
        n3, n4 = n4, n3
    if n2 > n4:
        n2, n4 = n4, n2
    return n4


# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
