# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
n = int(input("Кол-во чисел "))
my_list = []
summ = 0
while n > 0:
    a = int(input())
    my_list.append(a)
    n -= 1

for el in my_list:
    summ += el

print(summ)
