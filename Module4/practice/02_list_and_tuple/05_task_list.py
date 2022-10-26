# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0
length = []
for fruit in fruits:
    n = len(str(fruit))
    length.append(n)
    i += 1
    if n < max(length):
        print(i, (max(length) - n) * " " + fruit)
    else:
        print(i, fruit)

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
