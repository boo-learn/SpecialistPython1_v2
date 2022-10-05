# Посчитайте количество согласных букв в данной строке.

text = "В теории, теория и практика неразделимы. На практике это не так. Но не факт."
consonants = "йцкнгшщзхъфвпрлджчсмтьб"
consonants_counter = 0
i = 0
while i < len(consonants):
    consonants_counter += text.lower().count(consonants[i])
    i += 1
print(consonants_counter)
