# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

my_list = [2, -2, 3, 5, -7]
tot=0
for val in my_list:
    if val>0:
        tot+=val
print(tot)
