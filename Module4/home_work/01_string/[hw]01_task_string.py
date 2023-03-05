# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "Шла Саша по шоссе и сосала, сушку. Дело было в сентябре,было ей не скушно."
count_periods = text.count(".")
count_commas = text.count(",")
if count_periods > count_commas:
    print("Больше точек.")
elif count_periods < count_commas:
    print("Больше запятых.")
else:
    print("Одинаково.")
