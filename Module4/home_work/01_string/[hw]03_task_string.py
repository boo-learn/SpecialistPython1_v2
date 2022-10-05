# Посчитайте количество согласных букв в данной строке.

text = "Посчитайте количество согласных букв в данной строке."
consonants = "бвгджзйклмнпрстфхцчшщ"
i = 0
count = 0

while i < len(consonants):
    count += text.lower().count(consonants[i])
    i += 1
print(count)

