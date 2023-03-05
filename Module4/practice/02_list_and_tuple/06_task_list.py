# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число:"))     # Первое число
second_number = int(input("Второе число:"))    # Второе число
numbers_list_1 = [first_number, second_number]
i = int(1)
a = first_number
b = second_number - 1
result = 0
while a < b:
    a += 1
    x = a
    numbers_list_1.insert(i,x)
    i += 1
for i in numbers_list_1:
    if i%3 == 0:
        result += 1


print('Всего чисел кратных трем', result)
