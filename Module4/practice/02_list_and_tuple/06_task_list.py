# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

a = int(input("Введите число: "))     # Первое число
b = int(input("Введите число: "))    # Второе число
(a,b)=(a,b) if a>b else (b,a)
num_list=[]
while b <= a:
    if b % 3 == 0:
        num_list+=[b]
    b+=1
print(num_list)
