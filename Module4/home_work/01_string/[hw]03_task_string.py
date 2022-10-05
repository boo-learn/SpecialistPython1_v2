# Посчитайте количество согласных букв в данной строке.

text = "В теории, теория и практика неразделимы. На практике это не так."
consonants = "бвгджзйклмнпрстфхцчшщ"

cons_counter = 0
i = 0
while i < len(consonants):
    cons_counter += text.lower().count(consonants[i])
    i += 1

print(cons_counter)

