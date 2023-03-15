# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
numbers = [56, 66, -1, 54, 85, 2, -45, 58, -8]
summa =0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0 and numbers[i] > 0:
       summa += numbers[i]
print("Сумма= ", summa)
