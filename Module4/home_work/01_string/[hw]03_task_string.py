# Посчитайте количество согласных букв в данной строке.

text = "Теория мертва без практики живой."
vowels = "бвгджзйклмнпрстфхцчшщ"

vowels_counter = 0
i = 0
while i < len(vowels):
    vowels_counter += text.lower().count(vowels[i])
    i += 1

print(vowels_counter)
