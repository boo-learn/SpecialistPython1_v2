# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]
for line_by_line, parentheses in enumerate(fruits, 1):
    print(f'{line_by_line}: {parentheses}')

