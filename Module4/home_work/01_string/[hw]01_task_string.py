# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = 'яблоко,.банан,киви,.'
print(text.count('.'))
print(text.count(','))
if text.count('.') > text.count('.'):
    print("Больше . ")
elif  text.count('.') == text.count(','):
     print("Одинаково")
else:
     print("Больше ,")
