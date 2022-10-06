# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    n_fibonacсi = 0
    if n == 2:
        n_fibonacсi = 1
    elif n > 2:
        i = 1
        n_minus1 = 0
        n_minus2 = 1
        while i < n:
            n_fibonacсi = n_minus1 + n_minus2
            i += 1
            n_minus1, n_minus2 = n_fibonacсi, n_minus1
    return n_fibonacсi

#вторая элегантнее, но медленнее
def fibonacci2(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n>2:
        return fibonacci2(n-1)+fibonacci2(n-2)
