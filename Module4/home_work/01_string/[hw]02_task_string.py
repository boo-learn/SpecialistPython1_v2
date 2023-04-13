# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = input()

l = text.split()

found = False
string=""

for el in l:
    if el[0] == 'б':
        found = True
        string = el
        break

print(string) if found else print ("слов на б нет")
