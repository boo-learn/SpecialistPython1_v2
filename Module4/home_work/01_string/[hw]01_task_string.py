# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

print('Посчитаем количество точек и запятых в тексте, и определим кого из них больше.')

text = input('Введите текст: ')
count_points = 0
count_commas = 0
for index_1 in text:
    if index_1 == '.':
        count_points += 1
print('Количество точек в тексте: ', count_points)

for index_2 in text:
    if index_2 == ',':
        count_commas += 1
print('Количество запятых в тексте: ', count_commas)

if count_points > count_commas:
    print('Точек в тексте больше.')
elif count_commas > count_points:
    print('Запятых в тексте больше.')
else:
    print('В тексте одинаковое количество точек и запятых.')
