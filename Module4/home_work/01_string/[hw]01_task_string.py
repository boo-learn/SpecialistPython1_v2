# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "Не. следует, однако, забывать, что. консультация, ..с широким. активом"
find_dots = 0
find_commas = 0
for symbol in text:
    if symbol == ".":
        find_dots += 1
    elif symbol == ",":
        find_commas += 1

if find_dots < find_commas:
    print("Запятых: ", find_commas)
    print("Точек: ", find_dots)
    print("Запятых больше")
elif find_dots > find_commas:
    print("Запятых: ", find_commas)
    print("Точек: ", find_dots)
    print("Точек больше")
else:
    print("Запятых: ", find_commas)
    print("Точек: ", find_dots)
    print("Одинаково")
