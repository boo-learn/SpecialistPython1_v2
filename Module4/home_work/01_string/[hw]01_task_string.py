# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "....,,,"

point_sum = text.count(".")
comma_sum = text.count(",")

if point_sum > comma_sum:
    print("Точек больше")
elif point_sum < comma_sum:
    print("Запятых больше")
else:
    print("одинаково")
