# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here

first_number = int(input("первое число: "))  # Первое число
second_number = int(input("второе число: "))  # Второе число
num_list = []
for num in range(first_number, second_number + 1):
    if num % 3 == 0:
        print(num, end=" ")
