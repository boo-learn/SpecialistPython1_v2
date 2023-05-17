# Посчитайте количество согласных букв в данной строке.
text = input("Введите слово или фразу для поиска: ")

consonant = 'б в г д ж з й к л м н п р с т ф х ц ч ш щ'
consonant_counter = 0

for word in text:
    if word in consonant.split():
        consonant_counter += 1

print(consonant_counter)

