# Посчитайте количество согласных букв в данной строке.
text = "В теории, теория и практика неразделимы. На практике это не так."
cons = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

cons_counter = 0
i = 0
while i < len(cons.lower()):
    cons_counter += text.lower().count(cons.lower()[i])
    i += 1

print(cons_counter)
