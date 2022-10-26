# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("a:"))  # Первое число
second_number = int(input("b:"))  # Второе число

numbers = [first_number]
i = 0
for i in numbers:
    i += 1
    if first_number < i <= second_number:
        numbers.append(i)
for number in numbers:
    if number % 3 == 0:
        print(number)

# TODO: your code here
