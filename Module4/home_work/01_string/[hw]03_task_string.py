# Посчитайте количество согласных букв в данной строке.

text = "Посчитайте количество согласных букв в данной строке."
count = 0
for i in range(len(text)):
    if text[i].lower() not in 'аеёуоыэяюи' and text[i].isalpha():
        count += 1
print("Количество согласных", count)
