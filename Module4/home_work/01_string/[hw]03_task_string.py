# Посчитайте количество согласных букв в данной строке.

text = ...
text = "Посчитайте количество согласных букв в данной строке."
text = text.lower()
cons = "чсмтьбфвпрлджцкнгшщзхъ"

summa = 0
i = 0

while i < len(cons):
    summa += text.count(cons[i])
    i += 1
print ("Согласных",summa)
