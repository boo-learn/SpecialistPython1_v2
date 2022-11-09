# Напишите функцию находящую n-ое число Фибоначчи.
def fib(n):
    if n < 1:
        return n % 2
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


print(fib(15))
print(fib(1))
print(fib(10))
