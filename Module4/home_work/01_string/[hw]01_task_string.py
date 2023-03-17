# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = str(input())

dots = text.count(".")
commas = text.count(",")

if dots > commas:
    print("Точек больше")
elif dots < commas:
    print("Запятых больше")
else:
    print("Одинаково")
