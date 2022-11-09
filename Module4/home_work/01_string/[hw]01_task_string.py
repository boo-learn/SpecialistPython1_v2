# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Введите текст: ")
count_point = text.count(".")
count_comma = text.count(",")
if count_point > count_comma:
    print("точек больше")
elif count_point < count_comma:
    print("запятых больше")
else:
    print("одинаково")
