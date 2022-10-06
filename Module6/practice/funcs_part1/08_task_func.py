# Напишите функцию находящую n-ое число Фибоначчи.
def fibbonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonachi(n - 1) + fibbonachi(n - 2)

print(fibbonachi(20))
