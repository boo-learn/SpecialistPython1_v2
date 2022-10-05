# Посчитайте количество согласных букв в данной строке.

text = "Вася бил баклуши."
consonants = "бвгджзйклмнпрстфхцчшщ"

consonants_counter = 0
i = 0
while i < len(consonants):
    consonants_counter = consonants_counter + text.lower().count(consonants[i])
    i = i + 1

print(consonants_counter)

