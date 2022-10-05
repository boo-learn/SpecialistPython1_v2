# Посчитайте количество согласных букв в данной строке.

text = "Посчитайте количество согласных букв в данной строке."

consonants = 'бвгджзйклмнпрстфхцчшщ'
count = 0
for text_symb in text.lower():
    for cons in consonants:
        if text_symb == cons:
            count += 1
print(count)

