# Напишите функцию находящую n-ое число Фибоначчи.
def fib(n):
    if 1 <= abs(n) <= 2:
        return 1
    if n < 0 and n % 2 == 0:
        return -(fib(-n - 2) + fib(-n - 1))
    else:
        return fib(abs(n) - 2) + fib(abs(n) - 1)


print(fib(15))
print(fib(1))
print(fib(-5))
