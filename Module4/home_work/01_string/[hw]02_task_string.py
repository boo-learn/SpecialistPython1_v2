# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = input('text: ')
words = text.lower().split()
for word in words:
    if word[0] == 'б':
        conclusion = word
        break
    else:
        conclusion = ''
if conclusion == '':
    print('слов на б нет')
else:
    print(word)
