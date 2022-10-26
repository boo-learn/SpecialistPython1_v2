# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "Aaaaa, Bbbbb, Ccccccc."

i = 0
comma_word = 0
point_word = 0

while i < len(text):
    if text[i] == ",":
        comma_word = comma_word + 1
    elif text[i] == ".":
        point_word = point_word + 1
    i = i + 1
print(comma_word)
print(point_word)
if comma_word > point_word:
    print("больше запятых")
else:
    print("больше точек")


