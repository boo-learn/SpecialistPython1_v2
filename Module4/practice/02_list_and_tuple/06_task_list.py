# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("first_number: "))  # Первое число
second_number = int(input("second_number: "))  # Второе число

if first_number > second_number:
    first_number, second_number = second_number, first_number
number_division_3 = []

i = first_number
while i <= second_number:
    if i % 3 == 0:
        number_division_3.append(i)
    i += 1

print(number_division_3)

