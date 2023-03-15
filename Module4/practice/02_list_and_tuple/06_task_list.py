# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

while first_number <= second_number:
    if first_number % 3 == 0:
        print(first_number)
    first_number += 1

