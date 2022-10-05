# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

if first_number > second_number:
    first_number, second_number = second_number, first_number

numbers = []
for i in range(first_number, second_number + 1):
    if i % 3 == 0:
        numbers.append(i)

print(numbers)
