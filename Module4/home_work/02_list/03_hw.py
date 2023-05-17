# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
from random import randint

numbers = [randint(-100, 100) for i in range(int(input("n: ")))]

print(sum([(number) for number in numbers if number > 0 and number % 2 == 0]))
