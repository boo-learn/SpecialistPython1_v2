# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = str(input())

words = text.split(" ")
word_b = ""

for word in words:
    if word.startswith("б"):
        word_b = word
        print(word_b)
        break
if word_b == "":
    print("слов на б нет")

