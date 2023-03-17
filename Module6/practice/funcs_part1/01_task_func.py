# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    if n1 > n2:
        nx = n1
    else:
        nx = n2
    if n3 > n4:
        ny = n3
    else:
        ny = n4
    if nx > ny:
        return nx
    return ny


# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
