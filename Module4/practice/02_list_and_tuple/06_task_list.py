# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: 'first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
n = 3
for i in range(first_number, second_number + 1):
    if(i % n == 0):
        print(i)'
