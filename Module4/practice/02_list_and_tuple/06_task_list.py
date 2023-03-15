# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input('Первое число: '))     # Первое число
second_number = int(input('Второе число: '))    # Второе число

numbers = []

if first_number < second_number:
    n = first_number
    while first_number <= n <= second_number:
        if n % 3 == 0:
            numbers.append(n)
        n += 1
else:
    n = second_number
    while second_number <= n <= first_number:
        if n % 3 == 0:
            numbers.append(n)
        n += 1
print(numbers)
