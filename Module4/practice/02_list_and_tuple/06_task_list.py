# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

for number in range(first_number, second_number + 1):
    if number % 3 == 0:
        print(number)
