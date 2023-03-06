# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
numbers = [10, -15, 2, 25, -85, -68, 12]

summa_plus_elements = 0
for number in numbers:
    if number > 0 and number%2 == 0:
        summa_plus_elements += number
print(summa_plus_elements)
