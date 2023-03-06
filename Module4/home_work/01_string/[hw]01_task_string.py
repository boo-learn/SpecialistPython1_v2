# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ...
text = input("Введите текст: ")

num_points = text.count(".")
num_commas = text.count(",")

if num_commas > num_points:
    print("Больше запятых")
elif num_commas == num_points:
    print("Запятых и точек одинаковое количество")
else:
    print("Больше точек")
