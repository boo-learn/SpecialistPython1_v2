# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
number_range = list(range(first_number, second_number+1))

for i_number in number_range:
    if i_number % 3 == 0:
        print(i_number)
