# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
res_list = []
for num in range(first_number + 1, second_number):
    if num % 3 == 0 and num != 0:
        res_list.append(num)
print(res_list)
