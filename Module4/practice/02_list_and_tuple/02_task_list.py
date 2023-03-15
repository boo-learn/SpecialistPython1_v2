# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

# TODO: your code here
fruits = ["яблоко", "банан", "киви", "ананас", "груша"]
# i=1
# for fruit in fruits:
#      print(i, fruit)
#      i += 1

# result = list(enumerate(fruits, 1))
# print(result)
for num, fruit in enumerate(fruits, 1):
    print(num, fruit)
