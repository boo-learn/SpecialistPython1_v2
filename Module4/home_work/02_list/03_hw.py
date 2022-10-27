# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

first_number = -100     # Первое число
last_number = 100

max_el = first_number
summa_el = 0

for el in range(first_number, last_number):
    if el >= 0:
        if el > max_el:
            max_el = el
            summa_el = summa_el + max_el
print(summa_el)
