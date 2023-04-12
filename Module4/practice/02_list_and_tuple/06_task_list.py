# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

result = []  # Список для хранения чисел кратных трем
for i in range(first_number, second_number + 1):
    if i % 3 == 0:
        result.append(i)

print(result)
