# Посчитайте количество согласных букв в данной строке.

text = "I was searching my source to make a big desk yesterday."

count = 0
text1 = text.lower()
vowels = set("aeiouy")
for letter in text1:
    if letter in vowels:
        count += 1
print("Количество гласных равно: ", count)
