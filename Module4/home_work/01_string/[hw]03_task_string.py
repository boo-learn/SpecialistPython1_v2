# Посчитайте количество согласных букв в данной строке.

vowels_letter = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")
text = "Посчитайте количество согласных букв в данной строке"

text = text.casefold().replace(" ", "")
dict_letter = dict.fromkeys(vowels_letter, 0)
count_letter = 0

for letter in text:
    if letter not in dict_letter:
        count_letter += 1
print(count_letter)
