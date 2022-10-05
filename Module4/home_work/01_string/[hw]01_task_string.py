# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ", . . . , ,"
points = text.count(".")
commas = text.count(",")
if points > commas:
    print("Больше точек")
elif points < commas:
    print("Больше запятых")
else:
    print("Одинаково")
