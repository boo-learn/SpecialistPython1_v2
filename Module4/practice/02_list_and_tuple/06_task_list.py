# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

mylist = []
a = int(input('A: '))
b = int(input('B: '))
while a <= b:
    if a % 3 == 0:
        mylist.append(a)
    a += 1
print(mylist)
