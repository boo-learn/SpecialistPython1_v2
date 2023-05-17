# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

fruits = ["яблоко", "банан", "киви", "арбуз"]

len_frut_name = [0]
#len_frut_name.append(1)
#print (len_frut_name)
#len_frut_name.sort()
#print(len_frut_name)



for frut in (fruits):
    len_frut_name.append(len(frut))
#print(len_frut_name)
len_frut_name.sort(reverse=True)

#print(len_frut_name)

max_len = len_frut_name[0]
#print(max_len)

i = 0
for frut in (fruits):
   if len(frut) > 0:
      #  len_frut_name = len_frut_name +
  #  print(len(frut))
   # print(frut)
    i +=1
    print(i,frut.rjust(max_len, " "))


# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
