# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Введите текст:")

point_count = text.count(".")
coma_count = text.count(",")

if point_count > coma_count:
    print("В тексте больше точек")
elif point_count < coma_count:
    print("В тексте больше запятых")
else:
    print("Одинаково")
