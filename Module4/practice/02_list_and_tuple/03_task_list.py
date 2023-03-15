# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# import random

count_elements = int(input("Количество элементов"))
i = 0
s = 0
my_list = []
while i < count_elements:
        element = int(random.randint(-10,10))
        my_list.append(element)
        print("Элемент массива", my_list[i])
        i += 1
print("Сумма",sum(my_list))

