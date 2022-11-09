# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

first_number = int(input())  # Первое число
second_number = int(input())  # Второе число
for el in range(first_number, second_number):
    if el % 3 == 0:
        print(el)

