# Посчитайте количество согласных букв в данной строке.

text = "В теории, теория и практика неразделимы. На практике это не так."
vowels = "ауоыэяюёие"
i = 0
count = 0
while i < len(text):
    if vowels.count(text[i]) == 0 and text[i].isalpha():
        count += 1
    i += 1
print('Число согласных: ', count)
