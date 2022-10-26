# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

check_string = "....,,,,,,,"
zpt=check_string.count(",")
tchk=check_string.count(".")
if zpt>tchk:
    print("Запятых больше на:",zpt-tchk)
elif zpt<tchk:
    print("Точек больше на:",tchk-zpt)
else:
    print("Точек и Зяпятых одинаково")
