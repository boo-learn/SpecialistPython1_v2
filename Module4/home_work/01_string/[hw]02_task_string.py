# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = "В человеке должно быть все прекрасно и лицо и одежда и душа и мысли"
text = text.lower()
for i in text.split():
    if i.startswith("б"):
        print(i)
    else:
        print("Слова нет", end=" ")
