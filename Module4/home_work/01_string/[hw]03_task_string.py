# Посчитайте количество согласных букв в данной строке.

text = "выарвор авпор авогапо апоао карот"

letters = ("б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ")
count_letters = 0

for letter in letters:
    count_letters += letters.count(letter)

print(count_letters)
