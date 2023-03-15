# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input("first: "))     # Первое число
second_number = int(input("second: "))    # Второе число
i = first_number
numbers = []

while i < second_number:
    i += 1
    if i%3 == 0:
        numbers.append(i)
print(numbers)
