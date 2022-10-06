# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input('Число 1: '))  # Первое число
second_number = int(input('Число 2: '))  # Второе число
numbers_3 = []
i = min(first_number, second_number)
print(i, max(first_number, second_number))
while i <= max(first_number, second_number):
    print(i)
    if i % 3 == 0:
        numbers_3.append(i)
        i += 3
    else:
        i += 1
print(numbers_3)
