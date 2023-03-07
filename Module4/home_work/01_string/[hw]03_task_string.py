# Посчитайте количество согласных букв в данной строке.

text = "Посчитайте количество согласных букв в данной строке."
consonants = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
low_text = text.lower()
counter = 0
for letter in low_text:
    for find_consonants in consonants:
        if find_consonants == letter:
            counter += 1
print(counter)
