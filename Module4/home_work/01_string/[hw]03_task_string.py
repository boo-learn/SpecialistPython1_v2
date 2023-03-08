# Посчитайте количество согласных букв в данной строке.

text = ...
text = input("Введите текст строки: ")
f = filter(str.isalpha, text)
new_text = "".join(f).lower()
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
sogls = 0

for letter in new_text:
    if letter in vse_gls:
        sogls += 0
    else:
        sogls += 1

print("В строке", sogls, "согласных букв")
