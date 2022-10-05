# Посчитайте количество согласных букв в данной строке.
text = input("Введите произвольный текст: ")
consonants = "чсмтьбфвпрлджцкнгшщзхъ"

consonants_counter = 0
i = 0
while i < len(consonants):
    consonants_counter += text.lower().count(consonants[i])
    i += 1

print(consonants_counter)
