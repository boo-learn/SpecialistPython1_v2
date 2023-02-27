# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

number_list = [5, 7, -9, -10, 0, 3]
sum_positive_numbers = 0

for i_number in number_list:
    if i_number > 0:
        sum_positive_numbers += i_number
print("Сумма значений равна", sum_positive_numbers)
