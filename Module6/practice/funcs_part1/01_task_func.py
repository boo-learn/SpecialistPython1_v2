# Напишите функцию, возвращающую наибольшее из четырех чисел

def max4(n1, n2, n3, n4):
    def max_my(a,b):
        return a if a>b else b
    #return max((n1, n2, n3, n4))
    return max_my(max_my(n1,n2),max_my(n3,n4))

print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))
