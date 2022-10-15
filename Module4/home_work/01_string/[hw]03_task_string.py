# Посчитайте количество согласных букв в данной строке.

text = "внгутж  олдор.югн"
consonants = "бвгджзйклмнпрстфхцчшщ"
i = 0
count = 0
i_consonants = 0

while i_consonants < len(consonants):
    while i < len(text):
        if text.lower()[i] == consonants[i_consonants]:
            count += 1
        i += 1
    i = 0
    i_consonants += 1

print(count, "согласных букв")
