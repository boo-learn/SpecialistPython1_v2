# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

i = first_number
while i <= second_number:
    if i % 3 == 0:
        print(i)
    i += 1
    
