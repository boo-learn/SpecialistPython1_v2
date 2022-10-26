# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("first: "))
second_number = int(input("second: "))
if first_number > second_number:
    first_number, second_number = second_number, first_number
new_number = first_number
result = []
while new_number < second_number:
    if new_number % 3 == 0:
        result.append(new_number)
    new_number += 1
print(result)

# TODO: your code here
