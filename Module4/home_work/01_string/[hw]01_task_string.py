# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input ('Введите текст:')
num_commas = text.count(',')
num_points = text.count('.')

if num_commas == num_points:
    print('Одинаково')
    
if num_commas > num_points:
    print('Запятых больше')
    
if num_commas < num_points:
    print('Точек больше')
