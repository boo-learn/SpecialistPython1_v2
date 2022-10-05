# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ...
text = "tfgsn/sdrthy./asdg./fglhnm,m,////..,,.,,"
if text.count(",")>text.count("."):
    print("запятых")
elif text.count(",")<text.count("."):
    print("точек")
else:
    print("одинаково")
