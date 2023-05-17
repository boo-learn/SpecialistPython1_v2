# Посчитайте количество согласных букв в данной строке.

text = ...
vowels = "ауоыэяюёие"
count = 0

for char in text:
    if char.lower() not in vowels and char.isalpha():
        count += 1

print(count)
