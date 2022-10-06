# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("введите a: "))  # Первое число
second_number = int(input("введите b: "))  # Второе число
numbers = []
if first_number > second_number:
    temp_number = first_number
    first_number = second_number
    second_number = temp_number
n = first_number
while n < second_number:
    if n % 3 == 0:
        numbers.append(n)
    n += 1
print(numbers)
