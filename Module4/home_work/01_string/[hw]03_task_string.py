# Посчитайте количество согласных букв в данной строке.

text = input('Введите текст:')
vowels = ['а' 'о' 'у' 'ы' 'и' 'е' 'ё' 'э' 'ю''я']
a = text.count('a')
o = text.count('о')
u = text.count('у')
yi = text.count('ы')
i = text.count('и')
e = text.count('е')
ye = text.count('ё')
ee = text.count('э')
yu = text.count('ю')
ya = text.count('я')
print(f"Согласных: {len(text) - (a + e + i + o + u + yi + ye + ee + yu + ya)}")
