# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input('text: ')
dot = text.count('.')
comma = text.count(',')
if dot > comma:
    print('точек больше')
elif comma > dot:
    print('запятых больше')
else:
    print('одинаково')
