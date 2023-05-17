# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первая граница диапазона чисел: "))     # Первое число
second_number = int(input("Вторая граница диапазона чисел: "))    # Второе число
list_num = []

for i in range(first_number, second_number+1):
    if i%3==0:
        list_num.append(i)

print("Кратные 3-м числа: ", list_num)
