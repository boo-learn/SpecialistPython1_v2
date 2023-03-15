# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
my_list = [66, -5, 0, 1, 4]
i = 0
summa = 0
for summ in my_list:
    summa = summa + int(my_list[i])
    i = i + 1
print(summa)
