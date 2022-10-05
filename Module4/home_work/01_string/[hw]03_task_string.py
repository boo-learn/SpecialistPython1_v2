# Посчитайте количество согласных букв в данной строке.
text = "Бюджетные риски делятся на явные и неявные"
notvowels = "бвгджзклмнпрстфхцчшщ"
notvowels_counter = 0
i = 0
while i < len(notvowels) :
    notvowels_counter += text.lower().count(notvowels[i])
    i += 1
print(notvowels_counter)
