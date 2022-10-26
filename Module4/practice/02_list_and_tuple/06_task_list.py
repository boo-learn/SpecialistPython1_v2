# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

first_number = int(input("введите число 1 "))     # Первое число
second_number = int(input("введите число 2 "))    # Второе число

lists = [first_number, second_number]

i = 0
sum = 0

for list in lists:
    sum = sum + list
    i = i + 1
print(sum)
