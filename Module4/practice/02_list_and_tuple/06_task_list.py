# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите первое число: "))     # Первое число
second_number = int(input("Введите первое число: "))    # Второе число
count_number = first_number
while count_number <= second_number:
    if count_number % 3 == 0 and count_number != 0:
        print(count_number)
    count_number += 1

# TODO: your code here
