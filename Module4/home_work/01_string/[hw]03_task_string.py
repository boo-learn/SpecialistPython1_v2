# Посчитайте количество согласных букв в данной строке.

check_string = "Посчитайте количество согласных букв в данной строке"
slovo=check_string.lower()
i=0
total=0
while i<len(check_string):
    simv=slovo[i:i+1]
    i+=1
    if simv=="б"or"в"or"г"or"д"or"ж"or"з"or"й"or"к"or"л"or"м"or"н"or"п"or"р"or"с"or"т"or"в":
        total+=1
print(total)
