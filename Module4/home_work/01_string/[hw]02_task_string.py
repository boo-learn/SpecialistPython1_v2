# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = "Представьте у вас есть файл с данными которые вы хотите обработать в Pandas " \
       "Хочется быть уверенным что память не закончится Как оценить использование памяти " \
       "с учетом размера файла Все эти оценки могут как занижать так и завышать использование памяти " \
       "На самом деле оценивать использование памяти просто не стоит"

words = text.split(" ")

pr = False

for word in words:
       if word[0] == "б" or word[0] == "Б":
              print(word)
              pr = True
              break

if not pr:
       print("слов на б нет")
