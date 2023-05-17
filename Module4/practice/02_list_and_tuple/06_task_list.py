# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

div_3 = []

i = first_number
while i <= second_number:
    if i % 3 == 0:
        div_3.append(i)
    i += 1
print(div_3)

# TODO: your code here
