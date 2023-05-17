# Посчитайте количество согласных букв в данной строке.

text = "буря мглою небо кроет"
vowels = "ауоыэяюёие"

count_vowels = 0
for one_vowels in vowels:
    count_vowels += text.count(one_vowels)

print("consonants: ", len(text) - count_vowels - text.count(" "))
