# Посчитайте количество согласных букв в данной строке.

word = input("Введите строку: ")
vow = 0
cons = 0
for i in word:
    letter = i.lower()
    if letter == "а" or letter == "у" or \
            letter == "о" or letter == "ы" or \
            letter == "э" or letter == "ю" or \
            letter == "я" or letter == "е" or \
            letter == "и" or letter == "ё":
        vow += 1
    else:
        cons += 1
print("Гласные звуки %i\nСогласные звуки %i" % (vow, cons))
