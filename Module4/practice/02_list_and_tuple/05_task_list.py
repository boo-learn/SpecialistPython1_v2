# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

index = 1
max_len = 0

for word in fruits:
    if max_len < len(word):
        max_len = len(word)
for word in fruits:
    num_gaps = " " *  (max_len - len(word))
    print(index, num_gaps, word)
    index += 1

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
