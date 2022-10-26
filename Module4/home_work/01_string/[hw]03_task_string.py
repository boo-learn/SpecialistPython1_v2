# Посчитайте количество согласных букв в данной строке.

text = "ааа ввв ббб ооо ууу"

i = 0
summa_consonant = 0
summa_no = 0

while i < len(text):
    if text[i] == "б" or text[i] == "в" or text[i] == "г" or text[i] == "д"  or text[i] == "ж":
        summa_consonant = summa_consonant + 1
    i = i + 1
print(summa_consonant)
