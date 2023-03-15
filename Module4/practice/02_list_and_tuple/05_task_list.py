# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

# TODO: your code here
fruits = ["яблоко", "банан", "киви", "арбуз", "картошечка", "марковка"]
long_index = 0
long_index_start = 0
num = 0
leng_fr = 0
final_fr = ""
space = " "
looong_str = ""

for leng in fruits:
    long_index = len(leng)
    if long_index_start < long_index:
        long_index_start = long_index
        looong_str = leng
print(long_index_start)

for list in fruits:
    num += 1
    leng_fr = len(list)
    if leng_fr < long_index_start:
        final_fr = (space * (long_index_start - len(list)) ) + list
    else:
        final_fr = looong_str

    print(num, final_fr)

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
