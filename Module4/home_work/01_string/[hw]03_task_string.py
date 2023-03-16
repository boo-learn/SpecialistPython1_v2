# Посчитайте количество согласных букв в данной строке.

text = "Посчитайте количество согласных букв в данной строке."
#text="lskdfhalsh"

vowels = "аеёиоуэюя"
f = filter(str.isalpha, text)
clear_letter_low = "".join(f).lower()
vowels_count = 0
for letter in vowels:
    vowels_count += clear_letter_low.count(letter)
consonant = len(clear_letter_low) - vowels_count
print("В данной строке согласных букв: ", consonant)
