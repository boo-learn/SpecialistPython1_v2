# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    def max2(n1, n2, n3, n4):
    all_numb=[n1,n2,n3,n4]
    max_el = all_numb[0]
    for el in all_numb:
        if el>max_el:
            max_el = el
    return max_el
a = 5
b = 6
c = 12
d = 7
print(max2(a, b, c, d))



# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
