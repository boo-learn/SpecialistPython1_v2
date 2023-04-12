# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Введите произвольный текст: ")
count_dot = text.count('.')
count_comma = text.count(',')

if count_dot > count_comma:
    print("Больше точек")
elif count_dot < count_comma:
    print("Больше запятых")
else:
    print("Одинаково")
