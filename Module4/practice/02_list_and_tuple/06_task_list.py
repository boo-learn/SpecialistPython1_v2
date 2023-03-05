# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
for i in range(first_number, second_number + 1):
    if i % 3 == 0:
        print(i)
