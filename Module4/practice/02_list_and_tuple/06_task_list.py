# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input("First Num: "))     # Первое число
second_number = int(input("Second Num: "))    # Второе число

#first_number = 0
# second_number = 20
i = 0
j = 0
if second_number > first_number:
    i = first_number
    j = second_number

else:
    i = second_number
    j = first_number
while i < j:
    if i % 3 == 0 and i != 0:
        print(i)
    i += 1
