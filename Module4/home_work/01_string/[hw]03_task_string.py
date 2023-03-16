# Посчитайте количество согласных букв в данной строке.

print('Посчитаем количество согласных букв в строке.')
text = input('Введите текст: ')
vowels = list('аеёиоуыэюя')
number = sum([text.count(i) for i in vowels])
print(number)



