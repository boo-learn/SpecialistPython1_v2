# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = ...

dots_num = text.count(".")
comma_num = text.count(",")

if dots_num == comma_num:
    print("одинаково")
else:
    print("." if dots_num > comma_num else ",")'''
