# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random

numbers = []
summ_pozitive = 0
n = int(input("Введите кол-во целых чисел для списка: "))
for i in range(0,n):
    numbers.append(random.randint(-100, 100))
for number in numbers:
    if number > 0 and number%2==0:
        summ_pozitive += number
print(numbers)
print(summ_pozitive)
