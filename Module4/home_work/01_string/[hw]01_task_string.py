# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"
text = input("Введите текст с точками и запятыми: ")

point = text.count(".")
comma = text.count(",")
if point > comma and point != 0:
    print("Больше точек")
elif comma > point and comma != 0:
    print("Больше запятых")
elif comma == point and point != 0 and comma != 0 :
    print("Знаков равное количество")
elif comma == 0 and point == 0:
    print("Знаки препинания отсутствуют")

