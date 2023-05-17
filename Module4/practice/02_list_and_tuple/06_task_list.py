# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число


if first_number > second_number:
    tmp = second_number
    first_number = second_number
    second_number = tmp

i = first_number
while i < second_number:
    if i % 3 == 0: print(i)
    i += 1
