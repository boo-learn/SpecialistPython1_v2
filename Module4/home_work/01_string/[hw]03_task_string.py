# Посчитайте количество согласных букв в данной строке.

text = "В теории, теория и практика неразделимы. На практике это не так."
consonants = "Б, В, Г, Д, Ж, З, Й, К, Л, М, Н, П, Р, С, Т, Ф, Х, Ц, Ч, Ш, Щ"
vocabulary = consonants.replace(", ","")
vocabulary = tuple(vocabulary)
# конечно можно было сразу подать кортеж с буквами, но это первое из гугла и было интересно попробовать
#print(vocabulary)
i = 0
for symbol in text:
    if symbol.upper() in vocabulary:
        #print(symbol, end='|')
        i += 1
print("Found", i, "symbols in text.")
