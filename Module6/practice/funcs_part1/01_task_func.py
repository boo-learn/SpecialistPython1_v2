# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    
    n_max = n1
    if n_max < n2:
        n_max = n2
    if n_max < n3:
        n_max = n3
    if n_max < n4:
        n_max = n4
    return n_max

# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
