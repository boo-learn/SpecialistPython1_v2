# Посчитайте количество согласных букв в данной строке.

text = "Мама мыла раму очень быстро"
text=text.lower()
consonants = "бвгджзйклмнпрстфхцчшщ"
n = len(consonants)

i = 0
summa_consonants = 0

while i < n:
    amount = text.count(consonants[i])
    i += 1
    summa_consonants += amount
print("Количество согласных: ", summa_consonants)
