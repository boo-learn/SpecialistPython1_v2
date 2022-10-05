# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

f_number = int(input("f_number : "))  # Первое число
s_number = int(input("s_number : "))  # Второе число
my_list = []
for i in range(f_number, s_number + 1):
    my_list.append(i)
print(my_list)
my_new_list = []
for j in my_list:
    if j % 3 == 0:
        my_new_list.append(j)
print(my_new_list)


