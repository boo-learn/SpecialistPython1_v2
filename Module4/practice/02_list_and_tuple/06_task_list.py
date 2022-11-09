# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число: "))     # Первое число
second_number = int(input("Второе число: "))    # Второе число
numbers_list = []
numbers_list_carat_3 = []
i = 0

if first_number > second_number:
    first_number, second_number = second_number, first_number
while first_number < second_number - 1:
    first_number += 1
    numbers_list += [first_number]
for number in numbers_list:
    if number % 3 == 0:
        numbers_list_carat_3 += [number]
print("Числа из диапазона кратные 3:", numbers_list_carat_3)
