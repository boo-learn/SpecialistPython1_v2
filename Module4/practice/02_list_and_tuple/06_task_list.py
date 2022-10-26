# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO:
first_number = int(input())
second_number = int(input())
list_nums=[first_number]
i=first_number
while i<second_number:
    list_nums.append(i+1)
    i+=1
print(list_nums)
new_list=[0]
for num in list_nums:
    if num%3==0:
        new_list.append(num)
new_list.pop(0)
print(new_list)
