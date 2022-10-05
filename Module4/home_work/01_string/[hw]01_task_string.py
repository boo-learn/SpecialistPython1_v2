# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ...
number_of_dots = text.count('.')
number_of_commas = text.count(',')

if number_of_dots > number_of_commas:
    print("Больше точек")
elif number_of_commas > number_of_dots:
    print("Больше запятых")
else:
    print("Точек и запятых одинаково")
