# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Введите текст: ")
numb_points = text.count(".")
numb_commas = text.count(",")
if numb_points > numb_commas:
    print("Точек больше")
elif numb_points < numb_commas:
    print("Запятых больше")
elif numb_points == numb_commas:
    print("Одинаково")
