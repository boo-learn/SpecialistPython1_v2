# Посчитайте количество согласных букв в данной строке.

text = ...
text = text.lower()
number_of_consonant = 0

vowels = ['а', 'ё', 'у', 'е', 'ы', 'я', 'о', 'э', 'и', 'ю']
for letter in text:
    if letter.isalpha() and letter not in vowels:
        number_of_consonant += 1
print(number_of_consonant)
