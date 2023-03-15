# Посчитайте количество согласных букв в данной строке.

text = input("Введите строку: ")
consonants = "бвгджзйклмнпрстфхцчшщ"
sum = 0

for glob in text:
    for word in consonants:
        if glob == word:
            sum += 1
print("Согласных букв:", sum)
