# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число


index = first_number
while index < second_number:
    if index % 3 == 0:
        print(index)
    index = index +1

