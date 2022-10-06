def max2(n1, n2):
    if n1 >= n2:
        c = n1
    if n2 > n1:
        c = n2
    return(c)
    pass


# Тестируем функцию
print(max2(5, 6))
print(max2(-10, -12))
print(max2(2.5, 2.6))
print(max2(-2.5, 0))
print(max2(0, -2.5))
