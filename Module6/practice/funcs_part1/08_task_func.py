# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    if n == 0:
        fibonacci_number = 0
    elif n == 1:
        fibonacci_number = 1
    else:
        previous_previous_number = 0
        previous_number = 1
        fibonacci_number = 1
        current_position = 2
        while current_position < n:
            fibonacci_number += previous_number
            previous_previous_number = previous_number
            previous_number = fibonacci_number - previous_previous_number
            current_position += 1

    return fibonacci_number


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
