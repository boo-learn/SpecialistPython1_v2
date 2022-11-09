# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.
import random

first_number = int(input("Начало диапазона: "))     # Первое число
second_number = int(input("Конец диапазона: "))    # Второе число
n = int(input("Кол-во элементов в диапазоне: "))                # Желаемое кол-во чисел в диапазоне
num_range = []
final_list = []

for i in range(n):
    random_numbers = random.randint(first_number, second_number)
    num_range.append(random_numbers)

for number in num_range:
    if number % 3 == 0:
        final_list.append(number)

print("Числа из диапазона, кратные 3: ", final_list)
