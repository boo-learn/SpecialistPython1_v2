# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Введите текст: ")
p = text.count(".")
c = text.count(",")
if p > c:
    print("Точек больше")
elif p < c:
    print("Запятых больше")
else:
    print("Одинаково")
print(p,c)
