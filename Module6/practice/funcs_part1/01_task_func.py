# Напишите функцию, возвращающую наибольшее из четырех чисел

def max2(a, b):
    if a < b:
        return b
    else:
        return a


def max4(n1, n2, n3, n4):
    if max2(n1, n2) > max2(n3, n4):
        return max2(n1, n2)
    else:
        return max2(n3, n4)


# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
