# Посчитайте количество согласных букв в данной строке.

text = "В теории, теория и практика неразделимы. На практике это не так."
consonants = "бвгджзклмнпрстфхцчшщй"
text = text.lower()
count = 0
i = 1

while i <= len(consonants):
    count += text.count(consonants[i - 1])
    i += 1
print('Количество согласных', count)

