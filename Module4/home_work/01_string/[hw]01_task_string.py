# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "Несмотря на то, что доктора лечили его, пускали кровь и давали пить лекарства, он всё-таки выздоровел."
dots = 0
commas = 0
i = 0

while i < len(text):

    if text[i] == ",":
        commas += 1

    elif text[i] == ".":
        dots += 1
    i += 1

if commas > dots:
    print("запятых больше")
elif dots > commas:
    print("точек больше")
else:
    print("одинаково")
