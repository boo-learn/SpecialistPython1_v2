# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
for count in range(first_number, second_number):
    if count % 3 == 0:

    print(count)
